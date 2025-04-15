import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

COMMAND_TIMEOUT = 60  # seconds
