# SMILES-Based Chemical Compound Filter and Analyzer for Drug Discovery Pipeline

A Python tool for processing large chemical compound datasets in drug discovery workflows. This project reads SMILES strings, applies customizable filters, computes elemental counts, and outputs curated results along with convenient summaries.

---

### 🚀 Features

- **Flexible filtering:** Keep compounds with activity scores above a user-defined threshold (default: 0.5).  
- **Element counting:** Calculates the number of carbon (C), nitrogen (N), and oxygen (O) atoms directly from SMILES.  
- **Top-compound summary:** Prints the top five compounds by activity, including names and SMILES.  
- **Efficient I/O:** Designed to handle very large CSV datasets with streaming reads.  
- **Fully tested:** Unit tests ensure reliability across edge cases.  

---

## 📦 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/chemical_compounds.git
   cd chemical_compounds
   ```

2. **Install UV**

   Follow the [UV installation guide](https://docs.astral.sh/uv/getting-started/installation/) or install via pip:


3. **Sync dependencies**

   ```bash
   uv sync
   ```


---

## 📁 Project Structure

```text
chemical_compounds/
├── data/                  # Input CSVs (compound_scores.csv, compound_names.csv)
├── output/                # Generated outputs (usable_compounds.csv)
├── drug_discovery/       # Core library code
│   ├── __init__.py
│   ├── main.py          # main function
│   ├── const.py          # consts used in the project
│   └── utils.py          # util funcs 
├── tests/                 # Unit tests
│   └── test_*.py
├── pyproject.toml       # Pin project dependencies
└── README.md              # Project documentation
```

- **Entry point:** `drug_discovery/main.py`  
- **CLI invocation:** `uv run main -- [options]`

---

## ⚙️ Usage

After syncing dependencies, run:

```bash
uv run main --threshold 0.7 --show-top
```

- **`--threshold`**: Minimum activity score (default `0.5`).  
- **`--show-top`**: Include this flag to print the top five compounds to the console.  
- **Output file**: `output/usable_compounds.csv` with columns:
  - `smiles`
  - `activity_score`
  - `C`, `N`, `O`

Alternatively, invoke via Python module:

```bash
python -m drug_discovery.main --threshold 0.7 --show-top
```

Sample console output:

```text
1. Aspirin - 0.92
   CC(=O)OC1=CC=CC=C1C(=O)O
2. Ibuprofen - 0.89
   CC(C)CC1=CC=C(C=C1)C(C)C(=O)O
...
```

---

## 🛠️ Development

Use UV for your developer commands:

1. **Type checking:**  
   ```bash
   uv run mypy
   ```
2. **Testing:**  
   ```bash
   uv run pytest
   ```

Contributions, issues, and pull requests are welcome!

