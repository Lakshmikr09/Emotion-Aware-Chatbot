import requests
import json
from datetime import datetime
import os

API_URL = "http://127.0.0.1:8000/chat"
session_id = None  # to keep track of each conversation

# Folder to store conversation logs
LOG_FOLDER = "chat_logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

# Generate a timestamped log file name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_path = os.path.join(LOG_FOLDER, f"chat_{timestamp}.json")

conversation_history = []  # list to store all turns

print("🧠 Emotion-Aware Chatbot (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"quit", "exit"}:
        print("💾 Saving conversation...")

        # Save the entire conversation to JSON
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(conversation_history, f, indent=4, ensure_ascii=False)

        print(f"✅ Chat saved to: {log_path}")
        print("Chat ended. Goodbye!")
        break

    data = {"text": user_input}
    if session_id:
        data["session_id"] = session_id

    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            bot_reply = result['reply']
            emotion = result['detected_emotion']

            # Display chat
            print(f"Bot ({emotion}): {bot_reply}\n")

            # Add to conversation history
            conversation_history.append({
                "user": user_input,
                "bot": bot_reply,
                "emotion": emotion,
                "sentiment": result['sentiment'],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            # Keep session memory
            session_id = result.get("session_id", session_id)

        else:
            print("❌ Error:", response.status_code, response.text)

    except Exception as e:
        print("⚠️ Connection error:", e)
