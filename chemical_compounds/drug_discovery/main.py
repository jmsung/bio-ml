"""
Entry point for the SMILES-Based Compound Filter and Analyzer.
"""
import argparse
from pathlib import Path
from . import const
from . import utils
from typing import Dict, Any
import csv

def main() -> None:
    """
    CLI entrypoint. Parses args, filters compounds, writes output, and shows top results.
    """
    parser = argparse.ArgumentParser(
        description="Filter and analyze compounds based on SMILES and activity scores."
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=const.DEFAULT_THRESHOLD,
        help="Minimum activity score to include (default: 0.5)",
    )
    parser.add_argument(
        "--show-top",
        action="store_true",
        help="Print top 5 compounds by activity score",
    )
    args = parser.parse_args()

    print(f"🔍 Running filter with threshold = {args.threshold}")
    scores_path = Path(const.FILEPATH_COMPOUND_SCORES)
    names_path  = Path(const.FILEPATH_COMPOUND_NAMES)
    output_path = Path(const.FILEPATH_USABLE_COMPOUNDS)

    print(f"📄 Reading compound scores from: {scores_path}")
    utils.prepare_output_directory(output_path.parent)

    # Stream, filter, and collect usable compounds
    usable: list[Dict[str, Any]] = []
    for entry in utils.iter_compound_scores(scores_path):
        if entry['activity_score'] < args.threshold:
            continue
        atoms = utils.count_atoms(entry['smiles'])
        if atoms['C'] >= 6:
            continue
        usable.append({
            'smiles': entry['smiles'],
            'activity_score': entry['activity_score'],
            **atoms,
        })

    print(f"✅ Filtered down to {len(usable)} usable compounds")

    # Write to CSV
    fieldnames = ['smiles', 'activity_score', 'C', 'N', 'O']
    with output_path.open('w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in usable:
            writer.writerow(row)
    print(f"💾 Output written to: {output_path}")

    # Optionally print top results
    if args.show_top:
        print("\n🌟 Top compounds:")
        names = utils.load_names(names_path)
        top5 = sorted(
            usable, key=lambda r: r['activity_score'], reverse=True
        )[:5]
        for idx, comp in enumerate(top5, start=1):
            name = names.get(comp['smiles'], 'Unknown')
            print(f"{idx}. {name} - {comp['activity_score']}\n   {comp['smiles']}")

if __name__ == '__main__':
    main()
