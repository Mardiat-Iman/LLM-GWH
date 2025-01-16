#file to serve as GPT connection
import streamlit as st
from openai import OpenAI
import requests

api_key = st.secrets["api_key"]
#Developer quickstart-from homepge of openAI

client = OpenAI(api_key = "api_key")

#function to generate text
def generate_text(prompt):
    completion = client.chat.completions.create(
         model = "gpt-4o",
         store=True, #remove this if it doesn't work
         messages=[
        {"role": "user", "content": prompt}
        ]
    ) 
    return completion.choices[0].message.content

#function to generate image from prompts using DALL-E
def generate_image(prompt):
    response = client.images.generate(
         model = "dall-e-3",
           prompt = "a white siamese cat",
           size="1024x1024",
           quality="standard",
           n=1,
    )
    image_url = response.data[0].url

    image_response = requests.get(image_url)

    with open("cat.png", 'wb') as file:
        file.write(image_response.content)