#file to serve as GPT connection
import streamlit as st


api_key = st.secrets["api_key"]
#Developer quickstart-from homepge of openAI
from openai import OpenAI
client = OpenAI(api_key = "api_key")
completion = client.chat.completions.create(
    model = "gpt-4o",
    store=True, #remove this if it doesn't work
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
print(completion.choices[0].message.content)