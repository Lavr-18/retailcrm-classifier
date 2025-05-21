import os
from dotenv import load_dotenv

load_dotenv()

RETAILCRM_API_KEY = os.getenv("RETAILCRM_API_KEY")
RETAILCRM_API_URL = os.getenv("RETAILCRM_API_URL")

# Настройки логгирования
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "app.log")
