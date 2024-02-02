from dotenv import load_dotenv, dotenv_values
import os

load_dotenv('../../.env')

API_KEY = os.getenv('API_KEY')
COMPILED_INSTANCE_FILE = 'compiled_instance.json'
INSTANCE_FILE = 'instance.json'
BASE_MODRINTH_URL = 'https://api.modrinth.com/v2'