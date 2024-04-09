import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Modern Messaging App", page_icon="📱")

# Title
st.title("Modern Messaging App")

# Sidebar with user input
with st.sidebar:
    st.header("User Details")
    username = st.text_input("Enter your username")
    selected_contact = st.selectbox("Select a contact", ["Contact 1", "Contact 2", "Contact 3"])

# Main content area
st.write(f"Logged in as: {username}")

# Chat area
st.subheader(f"Chatting with {selected_contact}")

# Input box for message
message = st.text_area("Type your message")

# Button to send message
if st.button("Send"):
    if message != "":
        st.success(f"Message sent: {message}")
    else:
        st.warning("Message cannot be empty!")


