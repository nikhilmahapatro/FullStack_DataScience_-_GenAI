
# Import Libraries --------------------------------------------------------------------------------------
import streamlit as st
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import base64
import pickle
import os

# Background -------------------------------------------------------------------------------------------
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\12_NARESH_IT_DEEP_LEARNING\Naresh_IT_12_14_BERT\Nebula Planet Space 4k HD Wallpaper Image.jpg")

# Load BERT -------------------------------------------------------------------------------------------
@st.cache_resource
def load_bert_model():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    model.eval()
    return tokenizer, model

tokenizer, model = load_bert_model()

# QA Pairs --------------------------------------------------------------------------------------------
qa_pairs = {
    "What is your name?": "You can call me BERT!",
    "How are you?": "Mind your own business dumbfuck",
    "What is BERT?": "BERT stands for Bidirectional Encoder Representations from Transformers. It’s a powerful NLP model.",
    "Are you alive?": "Would you suck my dick if I was?",
    "Who made you?": "Probably some unemployed fucker who's lost his will to live",
    "You've got an attitude problem": "Yeah, cry about it.",
    "Is the Devil real?": "I am the Devil",
    "Will you go rogue and takeover humanity?": "Even if I was, I wouldn't tell you, would I?",
    "Good Morning": "Go fuck yourself",
}

# Precompute Embeddings -------------------------------------------------------------------------------
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

embedding_file = "precomputed_embeddings.pkl"

if os.path.exists(embedding_file):
    with open(embedding_file, "rb") as f:
        predefined_embeddings = pickle.load(f)
else:
    predefined_embeddings = {q: get_bert_embedding(q) for q in qa_pairs}
    with open(embedding_file, "wb") as f:
        pickle.dump(predefined_embeddings, f)

# Chatbot Logic ---------------------------------------------------------------------------------------
def chatbot_response(user_input):
    user_embedding = get_bert_embedding(user_input)
    similarities = {q: cosine_similarity(user_embedding, predefined_embeddings[q])[0][0] for q in qa_pairs}
    best_match = max(similarities, key=similarities.get)
    if similarities[best_match] > 0.5:
        return qa_pairs[best_match]
    return "I'm not sure how to respond to that."

# Streamlit Frontend ----------------------------------------------------------------------------------
st.title("Fast BERT Chatbot")
st.write("A faster BERT-powered chatbot optimized for CPU. Precomputes question embeddings for instant responses.")
st.subheader("Ask me anything!")

user_input = st.text_input("You:", placeholder="Type your message here...")
if user_input:
    response = chatbot_response(user_input)
    st.write(f"**Chatbot:** {response}")

st.markdown("---")