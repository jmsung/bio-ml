# methylation_biomarker

A small-scale bio-ML experiment that builds a binary classifier on DNA methylation profiles to predict disease status. 

---

## Key Results

1. **percentile-rank vs. label**  
   <img src="data/methylation_2.png" alt="Fig 1: Distribution of a feature percentile-rank by label" width="1000"/>  
   *Figure 2.* The within-sample percentile rank of a feature separates Label 0 and Label 1 with extreme significance (p ≈ 1 × 10⁻³⁵).

2. **ROC curve for logistic regression on A_47 rank**  
   <img src="data/methylation_3.png" alt="Fig 2: ROC curve for a classifier" width="1000"/>  
   *Figure 3.* Receiver-operating characteristic for a logistic regression using only the percentile-rank feature, achieving AUC = 0.985.
