import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    WEB_URL = os.getenv("WEB_URL")
config = Config()