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
