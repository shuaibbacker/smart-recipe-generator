import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class RecipeGenerator:
    def _init_(self):
        self.api_key = os.getenv("API_KEY")

    def get_url(self):
        return f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"

    def get_recipe(self, ingredients, preferences):
        url = self.get_url()
        body = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": f"I have the following ingredients: {ingredients}. Suggest possible recipes."}]
                }
            ]
        }

        response = requests.post(url, headers={"Content-Type": "application/json"}, json=body)
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text']

def main():
    st.title("Smart Recipe App")
    ingredients = st.text_input("Enter ingredients (comma-separated)")
    if st.button("Get Recipe"):
        generator = RecipeGenerator()
        recipe = generator.get_recipe(ingredients, "")
        st.write(recipe)

if __name__ == "_main_":
    main()