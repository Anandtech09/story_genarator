import streamlit as st

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
client = OpenAI(
    api_key = os.getenv("api_key")
)



def get_comedy(word):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a story artist assistant, skilled in creating story with a word."},
            {"role": "user", "content": word}
        ]
    )
    return response.choices[0].message.content

# Streamlit app
st.title("Story Generator")

# User input
comedy_p = st.text_input("Enter a word", "")

# Button to generate comedy
if st.button("Generate Comedy"):
    if comedy_p:
        comedy = get_comedy(comedy_p)
        st.write(comedy)
    else:
        st.write("Please enter a word to generate comedy.")