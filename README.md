

## 🧠 Personalized Mental Health Support Chatbot
This project is an AI-powered Personalized Mental Health Support Chatbot that provides emotionally intelligent responses based on user input. 
It uses a fine-tuned emotion detection model to understand emotions such as joy, sadness, fear, anger, love, and surprise, and then generates context-aware supportive replies through a lightweight LLM (Gemma 2b) integrated with Streamlit for the user interface.

## 🚀 Features

- 🗣️ Emotion Detection: Accurately identifies user emotions using a fine-tuned transformer model.
- 💬 Personalized Replies: Generates empathetic and relevant responses using a local LLM (TinyLlama or Llama3).
- 🌈 Streamlit Interface: Clean and interactive web app for real-time user interaction.
- ⚡ Lightweight Model Support: Runs efficiently on systems with limited memory (using Gemma 2B).
- 🔒 Offline Capable: Works locally without requiring internet or external API calls.

## Tech Stack

- Programming Language: Python
- Frontend: Streamlit
- Model Framework: PyTorch
- Emotion Detection: Transformer-based model (emotion-clf)
- Conversational Model: Gemma 2B(via Ollama)
- Libraries: Transformers, Torch, Streamlit, Ollama

## Installation 

- Clone Repository:
```bash
git clone https://github.com/rohit-kun27/AI_Personalized_Mental_Health_Chatbot.git
cd AI_Personalized_Mental_Health_Chatbot
```
- Download the Model:</br>
  [Google Drive Link](https://drive.google.com/drive/folders/1fBO8GNT-swoC8zRs_Q18cmyMtRXKFJxB?usp=drive_link)

- Install Dependencies:
```bash
pip install -r requirements.txt
```
- Run Streamlit app:
 ```bash
python -m streamlit run app.py
```

## How It Works
- User inputs a message expressing feelings or concerns.
- The chatbot analyzes the text and predicts the dominant emotion.
- Based on the detected emotion, the LLM (Gemma 2B) generates a supportive and empathetic response.
- The reply is displayed on the Streamlit chat interface.


