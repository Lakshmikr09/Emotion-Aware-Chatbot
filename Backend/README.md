Emotion-Aware Chatbot — Backend
---------------------------------

This package contains a beginner-friendly backend for an Emotion-Aware Chatbot
using FastAPI. It includes:
- src/inference.py  : model loading, emotion prediction, sentiment, reply generation
- src/app.py        : FastAPI server exposing /chat and health endpoints
- download_demo_model.py : helper script that downloads a demo HF model to models/
- requirements.txt
- Dockerfile

Notes:
- The repo does NOT include large model weights. Use download_demo_model.py to fetch a demo model from Hugging Face.
- If you don't want to download a model, the backend will fall back to a safe rule-based classifier so the API still works.
- The chatbot avoids repeating the same template reply within a single session (session = a simple server-side UUID).
- To run locally, create a virtualenv, install requirements, run `python download_demo_model.py` (optional), then `uvicorn src.app:app --reload`.
