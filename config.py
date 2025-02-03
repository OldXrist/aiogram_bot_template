import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot token from Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Database settings
DB_PATH = "data/bot.db"

# Admins list (Telegram user IDs)
ADMINS = list(map(int, os.getenv("ADMIN_IDS").split(',')))

# Logging level
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
