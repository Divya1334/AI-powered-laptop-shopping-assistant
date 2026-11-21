
import streamlit as st
from backend.agent import chat_with_agent

st.set_page_config(
    page_title="AI Shopping Assistant",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ AI Shopping Assistant")
st.caption("Find your perfect laptop with AI assistance!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Customer input
user_input = st.chat_input(
    "Ask me about laptops..."
)

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Finding the best laptops for you..."):

            try:
                response = chat_with_agent(user_input)

                st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:
                st.error(f"Something went wrong: {e}")
