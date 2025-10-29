import os
from dotenv import load_dotenv
from src.utils.logger import setup_logger

# Setup logger
logger = setup_logger(__name__)

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the application"""
    
    # Telegram Bot Token
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7564176119:AAH04VEHRhzoV9AAQs0wFK-RjQ1OSCcA0Dw")
    
    # Fireworks API Key
    FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")
    
    # Fireworks API URL
    FIREWORKS_API_URL = "https://api.fireworks.ai/inference/v1/completions"
    
    # Default AI model
    DEFAULT_MODEL = "accounts/fireworks/models/mixtral-8x7b-instruct"
    
    # Logging level
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Maximum message length for Telegram
    MAX_MESSAGE_LENGTH = 4096
    
    @classmethod
    def validate(cls):
        """Validate configuration settings"""
        if not cls.TELEGRAM_BOT_TOKEN or cls.TELEGRAM_BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN":
            logger.error("TELEGRAM_BOT_TOKEN is not set properly")
            return False
        
        if not cls.FIREWORKS_API_KEY or cls.FIREWORKS_API_KEY == "YOUR_FIREWORKS_API_KEY":
            logger.warning("FIREWORKS_API_KEY is not set properly, some features may not work")
        
        return True
