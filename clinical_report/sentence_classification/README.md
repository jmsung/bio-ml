## Task 1: Sentence Classification

### Goal
Classify sentences into:
- Adverse Effect
- Positive Outcome
- Neutral Observation

### What to Do
- Load the provided classification_data.csv file (1000 examples).
- Fine-tune a transformer model (e.g., DistilBERT).
- Preprocess text (tokenization, padding/truncation).
- Encode labels and split data into train/validation sets.
- Evaluate with accuracy and F1 score.
- Generate predictions on new example sentences.

### Example
```
Sentence: "Patient reported mild headache after taking DrugA."
Predicted Category: Adverse Effect
```

## Provided Datasets
- [`classification_data.csv`](./data/classification_data.csv)
    - Columns: `id`, `text`, `label`

## Notebook
[`notebooks/classification_data.ipynb`](notebooks/classification_data.ipynb)

---

## Results

After just one epoch of fine-tuning, the pretrained DistilBERT model achieves perfect validation performance (Accuracy = F1 = AUC = 1.0) for all 3 classes.

### Training vs. Evaluation Loss  
![Training vs. Evaluation Loss](./results/figs/training_vs_eval_loss.png)

### One-vs-Rest ROC Curves  
![ROC curves](./results/figs/roc_curves.png)