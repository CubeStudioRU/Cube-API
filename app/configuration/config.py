from dotenv import load_dotenv, dotenv_values
import os

load_dotenv('../../.env')

API_KEY = os.getenv('API_KEY')