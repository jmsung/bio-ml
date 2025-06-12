# methylation_biomarker

A small-scale bio-ML experiment that builds a binary classifier on DNA methylation profiles to predict disease status. 

---

## Key Results

1. **Global feature distributions**  
   <img src="data/methylation_1.png" alt="Fig 1: Boxplot of all methylation features across samples" width="1000"/>  
   *Figure 1.* Boxplots showing the range and variability of each methylation feature across the entire cohort.

2. **A_47 percentile-rank vs. label**  
   <img src="data/methylation_2.png" alt="Fig 2: Distribution of A_47 percentile-rank by label" width="1000"/>  
   *Figure 2.* The within-sample percentile rank of feature **A_47** separates Label 0 and Label 1 with extreme significance (p ≈ 1 × 10⁻³⁵).

3. **ROC curve for logistic regression on A_47 rank**  
   <img src="data/methylation_3.png" alt="Fig 3: ROC curve for A_47-based classifier" width="1000"/>  
   *Figure 3.* Receiver-operating characteristic for a logistic regression using only the A_47 percentile-rank feature, achieving AUC = 0.985.
