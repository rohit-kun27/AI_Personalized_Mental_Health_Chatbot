import streamlit as st
from transformers import pipeline 
import ollama 

emotion_clf = pipeline("text-classification",
                       model="./emotion_model",
                       tokenizer="./emotion_model")


label_map = {
    'LABEL_0': 'anger',
    'LABEL_1': 'fear',
    'LABEL_2': 'joy',
    'LABEL_3': 'love',
    'LABEL_4': 'sadness',
    'LABEL_5': 'surprise'
}

def predict_emotion(text: str)-> str:
    # Will predict the emotions....
    result = emotion_clf(text)[0]
    return label_map[result['label']]
    

def generate_response(emotion:str,user_text:str) -> str: 
    prompt =(
        f"The user seems {emotion}."
        f"User said: \"{user_text}\"."
        "Respond kindly with Short , and Empathic Message."
    )
    out=ollama.chat(
        model="gemma:2b",
        messages=[{"role": "user", "content": prompt}]
    )
    return out["message"]["content"].strip()   


#Streamlit Code....
    
st.set_page_config(page_title="Mental-Health Companion", page_icon="💬")

st.title("💬 Mental-Health Companion")
st.caption("Emotion-aware Generative AI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_msg = st.chat_input("Hey how you feel today…")
if user_msg:
    # store user message
    st.session_state.history.append(("user", user_msg))

    # detect emotion and generate reply
    emotion = predict_emotion(user_msg)
    bot_msg = generate_response(emotion, user_msg)

    # store bot reply
    st.session_state.history.append(("bot", bot_msg))

# render conversation
for speaker, msg in st.session_state.history:
    with st.chat_message("user" if speaker == "user" else "assistant"):
        st.markdown(msg)
    