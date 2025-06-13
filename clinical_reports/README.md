# clinical_reports
NLP task to analyze clinical trial reports.

## Background

Helix AI (fictional company) is a leading pharmaceutical company leveraging Natural Language Processing (NLP) to analyze clinical trial reports. We want to automate the extraction of key insights from unstructured text.

You will simulate a real-world task by building NLP models to:
- Classify sentences from clinical trials.
- Extract important entities (Drug Name, Symptom, Dosage).

## Tasks Overview

You will:
- Fine-tune a **transformer model** for **sentence classification**.
- Train an **NER model** for extracting key entities.

You should work in **Python**, focusing on **modeling and coding only** — no deployment required.

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

## Task 2: Named Entity Recognition (NER)

### Goal
Extract these entities:
- Drug Name (e.g., “Aspirin”)
- Symptom (e.g., “nausea”)
- Dosage (e.g., “50mg”)

### What to Do
- Load the provided ner_data.conll dataset (IOB format).
- Fine-tune a token classification model (e.g., DistilBERT), or use spaCy.
- Train on token-level annotations.
- Evaluate using entity-level precision, recall, and F1 score.

### Example
```
Sentence: "Patients were given 50mg of Aspirin and developed rash."
Predicted Entities:
- Drug Name: Aspirin
- Dosage: 50mg
- Symptom: rash
```

## Provided Datasets
- `classification_data.csv`
    - Columns: `id`, `text`, `label`

    [classification_data.csv](attachment:7bced411-3427-4c6b-875e-4191676f47f3:classification_data.csv)
    
- `ner_data.conll`
    - IOB-tagged format for NER (Token + Tag)
    
    [ner_data.csv](attachment:46d5bad6-7467-4ced-ba24-c137e7baf1ca:ner_data.csv)
    
## Sample NLP Modelling Notebook
```python
# Baseline NLP Modeling Notebook

# 1. Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
import torch
from datasets import Dataset

# 2. Load Classification Dataset
classification_df = pd.read_csv("/mnt/data/classification_data.csv")

# 3. Encode Labels
label_encoder = LabelEncoder()
classification_df['label_encoded'] = label_encoder.fit_transform(classification_df['label'])

# 4. Train-Test Split
train_texts, val_texts, train_labels, val_labels = train_test_split(
    classification_df['text'].tolist(),
    classification_df['label_encoded'].tolist(),
    test_size=0.2,
    random_state=42
)

# 5. Tokenization
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

train_encodings = tokenizer(train_texts, truncation=True, padding=True)
val_encodings = tokenizer(val_texts, truncation=True, padding=True)

# 6. Dataset Class
torch.backends.cuda.matmul.allow_tf32 = True

class ClassificationDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = ClassificationDataset(train_encodings, train_labels)
val_dataset = ClassificationDataset(val_encodings, val_labels)

# 7. Model
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=len(label_encoder.classes_))

# 8. Training Arguments
training_args = TrainingArguments(
    output_dir="/tmp/results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=1,
    weight_decay=0.01,
    logging_dir="/tmp/logs",
    logging_steps=10,
    save_strategy="no",
    load_best_model_at_end=False,
)

# 9. Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

# 10. Train
trainer.train()

# 11. Evaluation
metrics = trainer.evaluate()
print(metrics)
```