import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

coinmarketcap_key = os.getenv("coinmarketcap_key")