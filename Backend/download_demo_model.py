# download_demo_model.py
# Downloads a demo Hugging Face emotion model into models/emotion_classifier
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import os

MODEL_NAME = "bhadresh-savani/distilbert-base-uncased-emotion"
OUT_DIR = "models/emotion_classifier"

os.makedirs(OUT_DIR, exist_ok=True)

print("Downloading model:", MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Saving model to", OUT_DIR)
model.save_pretrained(OUT_DIR)
tokenizer.save_pretrained(OUT_DIR)
print("Done. The model is saved in", OUT_DIR)
