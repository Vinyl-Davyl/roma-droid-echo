import os
import logging
from dotenv import load_dotenv
from src.bot.bot import RomaDroidBot
from src.utils.logger import setup_logger

# Load environment variables
load_dotenv()

# Setup logger
logger = setup_logger(__name__)

def main():
    """Main function to start the bot"""
    # Get bot token from environment variable
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    # Fallback to hardcoded token if not found (not recommended for production)
    if not token:
        logger.warning("TELEGRAM_BOT_TOKEN not found in environment variables. Using fallback token.")
        token = "7564176119:AAH04VEHRhzoV9AAQs0wFK-RjQ1OSCcA0Dw"  # Fallback token
    
    # Check if token is valid
    if not token or token == "YOUR_TELEGRAM_BOT_TOKEN":
        logger.error("Please set your Telegram bot token in the .env file or as an environment variable.")
        return
    
    try:
        # Initialize and run the bot
        bot = RomaDroidBot(token).setup()
        logger.info("ROMA Droid Echo bot initialized successfully")
        bot.run()
    except Exception as e:
        logger.error(f"Error starting the bot: {e}")

if __name__ == "__main__":
    main()