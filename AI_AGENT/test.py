import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    models = openai.Model.list()
    print("Models retrieved successfully.")
except Exception as e:
    print("Error:", e)
