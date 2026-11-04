import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("Missing SauceDemo credentials in environment variables")