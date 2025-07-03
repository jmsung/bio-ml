import sys
import csv
from pathlib import Path
import pytest
from typing import Generator

import drug_discovery.const as const
import drug_discovery.utils as utils
from drug_discovery.main import main

@pytest.fixture(autouse=True)
def setup_environment(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Generator[None, None, None]:
    """
    Patch file paths, sys.argv, and core utility functions to provide a controlled test environment.
    """
    # Ensure CLI sees no extra args by default
    monkeypatch.setattr(sys, 'argv', ['prog'])

    # Redirect output CSV to a temp file
    output_file = tmp_path / 'usable.csv'
    monkeypatch.setattr(const, 'FILEPATH_USABLE_COMPOUNDS', str(output_file))

    # Stub out directory preparation to no-op
    monkeypatch.setattr(utils, 'prepare_output_directory', lambda p: None)

    # Provide a small set of test compound entries
    entries = [
        {'smiles': 'CCC',     'activity_score': 0.6},
        {'smiles': 'CCCCCC',  'activity_score': 0.7},
        {'smiles': 'NNN',     'activity_score': 0.8},
    ]
    monkeypatch.setattr(utils, 'iter_compound_scores', lambda path: iter(entries))

    # Simple atom-counting stub based on character counts
    def fake_count(smiles: str) -> dict[str, int]:
        return {
            'C': smiles.count('C'),
            'N': smiles.count('N'),
            'O': smiles.count('O'),
        }
    monkeypatch.setattr(utils, 'count_atoms', fake_count)

    # Default threshold override
    monkeypatch.setattr(const, 'DEFAULT_THRESHOLD', 0.5)

    yield


def test_main_default_threshold(tmp_path: Path) -> None:
    """
    Without --show-top, main() should filter by threshold and carbon count,
    then write the remaining entries to the output CSV without printing.
    """
    # Run the CLI entry point
    main()

    # Read back and verify CSV contents
    output_path = Path(const.FILEPATH_USABLE_COMPOUNDS)
    rows = list(csv.DictReader(output_path.open()))

    # 'CCCCCC' has 6 carbons (filtered), so only 'CCC' and 'NNN' remain
    smiles_list = [r['smiles'] for r in rows]
    assert smiles_list == ['CCC', 'NNN']
    # Verify activity scores were preserved and are > threshold
    scores = [float(r['activity_score']) for r in rows]
    assert all(s > 0.5 for s in scores)


def test_main_show_top(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    """
    With --show-top, main() should also print the top compounds by score,
    using names from utils.load_names().
    """
    # Prepare a name mapping for printed output
    name_map: dict[str, str] = {'NNN': 'NitrogenRich', 'CCC': 'Carbocycle'}
    monkeypatch.setattr(utils, 'load_names', lambda path: name_map)

    # Simulate passing --show-top flag
    monkeypatch.setattr(sys, 'argv', ['prog', '--show-top'])

    # Run the entry point
    main()

    # Capture printed output
    printed = capsys.readouterr().out.strip().splitlines()

    # Only lines starting with a digit correspond to our printed entries
    entries = [line for line in printed if line and line[0].isdigit()]

    # Expected order: highest score first ('NNN'), then 'CCC'
    assert entries[0].startswith('1. NitrogenRich - 0.8')
    assert entries[1].startswith('2. Carbocycle - 0.6')
