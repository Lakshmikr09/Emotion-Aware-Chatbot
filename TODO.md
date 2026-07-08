# TODO: Improve Emotion Detection in Chatbot

## Tasks
- [x] Modify load_models() in inference.py to load the actual DistilBERT emotion classifier model from local files
- [x] Update predict_emotion() to handle the 6-label model (sadness, joy, love, anger, fear, surprise) and map to 4 expected labels (happy, sad, angry, stressed)
- [x] Test the improved emotion detection functionality

## Mapping Logic
- joy -> happy
- sadness -> sad
- anger -> angry
- love -> happy (positive emotion)
- fear -> stressed (anxiety-related)
- surprise -> neutral or happy (depending on context, but map to happy for simplicity)
