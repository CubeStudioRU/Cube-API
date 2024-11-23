import os

from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')
CURSEFORGE_API_KEY = os.getenv('CURSEFORGE_API_KEY')

COMPILED_CLIENT_INSTANCE_FILE = './instance/compiled_client_instance.json'
COMPILED_SERVER_INSTANCE_FILE = './instance/compiled_server_instance.json'
INSTANCE_FILE = './instance/instance.json'

BASE_CURSEFORGE_URL = 'https://api.curseforge.com/v1'
BASE_MODRINTH_URL = 'https://api.modrinth.com/v2'
