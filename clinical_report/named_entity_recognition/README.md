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
- `ner_data.conll`
    - IOB-tagged format for NER (Token + Tag)
    
    [ner_data.csv](attachment:46d5bad6-7467-4ced-ba24-c137e7baf1ca:ner_data.csv)
    