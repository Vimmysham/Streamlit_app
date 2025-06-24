import streamlit as st 
import random, time
from huggingface_hub import InferenceClient

def response_genrator(prompt):
    client = InferenceClient(
        "microsoft/Phi-3-mini-4k-instruct",
        token="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",
    )

    response = "".join(message.choices[0].delta.content for message in client.chat_completion(
        messages = [{"role":"user","content":prompt}],
        max_tokens = 500,
        stream=True,
    )) # type: ignore
    return response
st.title("Simple Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role":"user","content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    response = response_genrator(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role" : "assistant","content": response})