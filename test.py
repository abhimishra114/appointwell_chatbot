import streamlit as st
import spacy

# Load pre-trained NLP model (e.g., spaCy)
nlp = spacy.load("en_core_web_sm")

# Function to predict intent based on user input
def predict_intent(text):
    # Tokenize and preprocess the text
    doc = nlp(text)
    # Perform intent classification (you can replace this with your own model)
    # Here, we're just checking if the text contains certain keywords related to medical topics
    medical_keywords = ["healthcare", "medicine", "doctor", "hospital", "medical"]
    for token in doc:
        if token.lower_ in medical_keywords:
            return "medical_query"
    return "general_query"

# Main Streamlit app
st.title("Medical Assistance Chatbot")

# User input prompt
user_input = st.text_input("Ask a question")

# Button to submit the input
submit_button = st.button("Submit")

# Handle user input and predict intent
if submit_button and user_input:
    intent = predict_intent(user_input)
    if intent == "medical_query":
        # Handle medical query (e.g., fetch results from API)
        st.success("Fetching results for medical query...")
    else:
        st.warning("Please provide input related to medical assistance, doctors, etc.")
