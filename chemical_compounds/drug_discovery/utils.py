#!/usr/bin/env python3
"""
Utility functions for SMILES processing and filtering.
"""
import os
import shutil
import csv
from pathlib import Path
from typing import Iterator, Dict, Any
from collections import Counter
import ast

from rdkit import Chem

from . import const


def prepare_output_directory(directory: Path) -> None:
    """
    Ensure a clean output directory: deletes if exists, then creates.
    """
    if directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True, exist_ok=True)


def count_atoms(smiles: str, include_h: bool = False) -> Dict[str, int]:
    """
    Count C, N, O atoms in a SMILES string using RDKit.
    """
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return {"C": 0, "N": 0, "O": 0}
    if include_h:
        mol = Chem.AddHs(mol)
    symbols = [atom.GetSymbol() for atom in mol.GetAtoms()]
    counts = Counter(symbols)
    return {element: counts.get(element, 0) for element in ("C", "N", "O")} 


def iter_compound_scores(filepath: Path) -> Iterator[Dict[str, Any]]:
    """
    Stream rows from a CSV of compound scores, converting activity_score to float.
    """
    with filepath.open(newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['activity_score'] = float(row.get('activity_score', 0.0))
            yield row


def load_names(filepath: Path) -> Dict[str, str]:
    """
    Load mapping from each SMILES string to its compound name.
    The CSV’s `smiles` column is expected to contain a Python-style list,
    e.g. "['CCO', 'COC']". We literal_eval it and then assign name→each SMILES.
    """
    mapping: Dict[str, str] = {}
    with filepath.open(newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row.get('name', '').strip()
            raw = row.get('smiles', '[]')
            try:
                smiles_list = ast.literal_eval(raw)
            except (ValueError, SyntaxError):
                # fallback: treat the entire string as a single SMILES
                smiles_list = [raw.strip()]
            for smi in smiles_list:
                smi = smi.strip()
                if smi:
                    mapping[smi] = name
    return mapping
