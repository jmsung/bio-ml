# Differential Expression Analysis

In this exercise, you'll work with gene expression data to identify differentially expressed genes between treatment and control conditions.

## Task:
### For each gene, compute the log fold change to determine whether the gene is significantly differentially expressed in the treatment condition compared to the control condition

1. Download a gene expression dataset from the provided AWS S3 URI
2. Calculate the log fold change for each gene comparing treatment vs. control conditions
3. Determine which genes are significantly differentially expressed

## Deliverables:
- A single pandas DataFrame containing the columns:
  - gene: the identifier for a given gene
  - logFC: the log fold change value
  - p_val/measure_of_confidence: the statistical significance

## Implementation

### 📁 Project Structure
```
diff_expression/
├── notebok/
│   └── diff_expr.ipynb          # Main analysis notebook
├── data/                        # Downloaded data files
│   └── test_data.h5ad
├── result/                      # Analysis outputs (auto-cleaned)
│   ├── differential_expression_results.csv
│   ├── volcano_plot.html
│   ├── top_genes_histograms.html
│   ├── top_genes_summary.html
│   ├── top_20_significant_genes.csv
│   ├── upregulated_genes.csv
│   ├── downregulated_genes.csv
│   └── analysis_summary.csv
├── .env                         # AWS credentials (not tracked)
├── requirements.txt
└── README.md
```

### 🚀 Features Implemented

#### Core Requirements ✅
- **Data Download**: Secure S3 download with credential management
- **Log Fold Change Calculation**: Treatment vs control comparison
- **Statistical Testing**: T-tests with p-value computation
- **Results Export**: DataFrame with gene, logFC, p_val columns

#### Enhanced Features 🌟
- **Outlier Detection & Removal**: IQR-based outlier filtering for robust analysis
- **Interactive Visualizations**: 
  - Volcano plots with significance thresholds
  - Expression distribution histograms for top genes
  - Mean expression comparison charts
- **Data Management**: 
  - Automatic file existence checking
  - Clean result directory management
  - Comprehensive file organization
- **Statistical Robustness**:
  - Multiple outlier detection methods (IQR, Z-score, Percentile)
  - Configurable significance thresholds
  - Detailed outlier reporting

### 📊 Analysis Pipeline

1. **Environment Setup**: Load AWS credentials from `.env` file
2. **Data Management**: Check existing data, download if needed
3. **Data Exploration**: Comprehensive dataset overview
4. **Differential Expression**: 
   - Outlier detection and removal
   - Log fold change calculation
   - Statistical significance testing
5. **Visualization**:
   - Interactive volcano plot
   - Top genes expression histograms
   - Summary comparison charts
6. **Results Export**: Multiple output formats for further analysis

### 🔧 Usage

#### Prerequisites
```bash
# Install dependencies
conda env update -f environment.yml
# or
pip install -r requirements.txt
```

#### Configuration
Create `.env` file in the `diff_expression/` directory:
```bash
AWS_ACCESS_KEY_ID=your_aws_access_key_here
AWS_SECRET_ACCESS_KEY=your_aws_secret_key_here
DATA_URI=s3://your-bucket-name/path/to/your/data.h5ad
```

#### Running Analysis
1. Open `notebok/diff_expr.ipynb` in Jupyter/Cursor
2. Run cells sequentially
3. Results automatically saved to `result/` directory

### 🎯 Key Results

The analysis generates:
- **Main Deliverable**: `differential_expression_results.csv` with 61,198 genes
- **Interactive Plots**: HTML files for data exploration
- **Filtered Results**: Top significant genes with statistical metrics
- **Summary Statistics**: Analysis overview and outlier reports

## 📊 Key Results & Visualizations

### Volcano Plot
Interactive visualization showing the relationship between fold change and statistical significance for all genes.

![Volcano Plot](result/volcano_plot.png)

**📈 [View Interactive Version](result/volcano_plot.html)**
- **Red dots**: Significantly upregulated genes (logFC > 1, p < 0.05)
- **Blue dots**: Significantly downregulated genes (logFC < -1, p < 0.05)
- **Gray dots**: Non-significant genes
- **Dashed lines**: Significance thresholds (p = 0.05, |logFC| = 1)

### Expression Distribution Analysis
Histograms comparing treatment vs control expression levels for top differentially expressed genes.

![Gene Expression Histograms](result/gene_histograms.png)

**📊 [View Interactive Version](result/top_genes_histograms.html)**
- **Clean data** (main histograms): After outlier removal using IQR method
- **Outlier traces** (darker colors): Identified outlier cells shown separately
- **Statistical info**: LogFC and p-values displayed in subplot titles
- **Color coding**: Treatment (red), Control (teal), Outliers (dark variants)

### Mean Expression Comparison
Bar chart comparing mean expression levels between treatment and control groups.

![Expression Summary](result/expression_summary.png)

**📋 [View Interactive Version](result/top_genes_summary.html)**
- **Side-by-side comparison** of mean expression levels
- **Outlier-robust means**: Calculated after removing statistical outliers
- **Hover information**: Includes logFC, p-values, and outlier counts
- **Top 5 genes**: Most statistically significant differentially expressed genes

### Sample Results Summary
```
📊 Example Analysis Output:
- Total genes analyzed: 61,198
- Significantly different genes: X,XXX
  - Upregulated in treatment: XXX
  - Downregulated in treatment: XXX
- Outliers removed: X,XXX cells (improved statistical power)
- P-value threshold: < 0.05
- Fold change threshold: |logFC| > 1.0
```

### Top Differentially Expressed Genes
| Gene | LogFC | P-value | Direction | Biological Relevance |
|------|-------|---------|-----------|---------------------|
| GENE1 | +2.34 | 1.2e-15 | Up | [Add biological context] |
| GENE2 | -1.89 | 3.4e-12 | Down | [Add biological context] |
| GENE3 | +1.67 | 5.6e-10 | Up | [Add biological context] |
| ... | ... | ... | ... | ... |

### 📸 Image Generation
The notebook automatically generates both interactive HTML plots and static PNG images:
- **PNG files**: For direct display in README and presentations
- **HTML files**: For interactive exploration with hover data and zooming
- **High resolution**: PNG images saved with 2x scale factor for crisp display

*Note: Both static (PNG) and interactive (HTML) versions are saved to the `result/` directory*

## Attribution

**🤖 Code Development**: This implementation was assisted by **Cursor IDE** with **Claude-4-Sonnet** AI model

**👨‍💻 Review & Validation**: Code reviewed and validated by **Jongmin**

**📋 Implementation Details**:
- AI-assisted development for efficient coding and best practices
- Human oversight for biological relevance and statistical accuracy
- Comprehensive testing and validation of results
- Enhanced features beyond basic requirements for production-ready analysis
