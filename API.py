import streamlit as st
import requests

def get_llm_response(user_query):
    url = "http://127.0.0.1:5000/api"
    headers = {'Content-Type': 'application/json'}
    payload = {"user_query": user_query}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get('llm_response', 'No response from LLM')
    else:
        return "Error in calling the API"

st.title("Gemini LLM Interaction")
user_query = st.text_input("Enter your query:")

if user_query:
    llm_response = get_llm_response(user_query)
    st.write(f"LLM Response: {llm_response}")
