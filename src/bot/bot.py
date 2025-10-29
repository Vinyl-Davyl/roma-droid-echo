import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Import services
from src.services.ai_service import get_ai_response, summarize_content
from src.utils.logger import setup_logger
from src.utils.helpers import format_message

# Setup logger
logger = setup_logger(__name__)

class RomaDroidBot:
    """Main bot class for ROMA Droid Echo"""
    
    def __init__(self, token):
        """Initialize the bot with token"""
        self.token = token
        self.application = None
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send welcome message when the command /start is issued"""
        user = update.effective_user
        await update.message.reply_html(
            f"Hello {user.mention_html()}! 👋\n\n"
            f"Welcome to ROMA Droid Echo, your gateway to the Sentient ecosystem.\n\n"
            f"I can help you learn about Sentient, ROMA, and interact with AI capabilities.\n\n"
            f"Type /help to see available commands."
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send help information when the command /help is issued"""
        help_text = (
            "🤖 *ROMA Droid Echo Commands* 🤖\n\n"
            "*/start* - Start the bot\n"
            "*/help* - Show this help message\n"
            "*/about* - Learn about ROMA and Sentient\n"
            "*/summarize* [URL or text] - Summarize content\n"
            "*/ask* [question] - Ask ROMA about anything\n"
            "*/resources* - Get useful Sentient resources\n"
            "*/contact* - Get contact information\n\n"
            "You can also just send me a message to chat directly!"
        )
        await update.message.reply_markdown(help_text)
    
    async def about_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send information about ROMA and Sentient"""
        about_text = (
            "*About ROMA and Sentient* 🌐\n\n"
            "*ROMA* (Recursive Open Meta Agent) is a framework for building autonomous AI agents "
            "that can recursively improve themselves.\n\n"
            "*Sentient* is building a decentralized ecosystem for AI, where ROMA agents can operate "
            "autonomously, collaborate, and evolve.\n\n"
            "ROMA Droid Echo serves as your bridge to this ecosystem, providing easy access to "
            "Sentient's capabilities through a simple chat interface.\n\n"
            "Learn more with /resources"
        )
        await update.message.reply_markdown(about_text)
    
    async def resources_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send useful resources about Sentient"""
        resources_text = (
            "*Useful Sentient Resources* 📚\n\n"
            "• [ROMA GitHub Repository](https://github.com/sentient-agi/ROMA)\n"
            "• [Recursive Open Meta Agent Blog](https://blog.sentient.xyz/posts/recursive-open-meta-agent)\n"
            "• [Sentient Website](https://www.sentient.xyz/)\n"
            "• [Sentient Synthetic](https://sentient-synthetic.vercel.app/)\n\n"
            "Explore these resources to learn more about the Sentient ecosystem!"
        )
        await update.message.reply_markdown(resources_text, disable_web_page_preview=True)
    
    async def contact_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send contact information"""
        contact_text = (
            "*Contact Information* 📬\n\n"
            "• [Sentient Twitter](https://twitter.com/sentientAGI)\n"
            "• [Sentient Discord](https://discord.gg/sentient)\n"
            "• [Sentient GitHub](https://github.com/sentient-agi)\n\n"
            "For more information, visit [sentient.xyz](https://www.sentient.xyz/)"
        )
        await update.message.reply_markdown(contact_text, disable_web_page_preview=True)
    
    async def summarize_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Summarize content from URL or text"""
        # Get the text after the command
        if not context.args:
            await update.message.reply_text(
                "Please provide a URL or text to summarize.\n\n"
                "Example: /summarize https://blog.sentient.xyz/posts/recursive-open-meta-agent"
            )
            return
        
        query = ' '.join(context.args)
        await update.message.reply_text("🔍 Analyzing and summarizing content... Please wait.")
        
        try:
            summary = await summarize_content(query)
            await update.message.reply_text(f"📝 *Summary*:\n\n{summary}", parse_mode='Markdown')
        except Exception as e:
            logger.error(f"Error in summarize command: {e}")
            await update.message.reply_text(
                "Sorry, I couldn't summarize that content. Please check your input and try again."
            )
    
    async def ask_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Answer questions using AI"""
        if not context.args:
            await update.message.reply_text(
                "Please ask a question.\n\n"
                "Example: /ask What is ROMA?"
            )
            return
        
        query = ' '.join(context.args)
        await update.message.reply_text("🧠 Thinking... Please wait.")
        
        try:
            response = await get_ai_response(query)
            await update.message.reply_text(response)
        except Exception as e:
            logger.error(f"Error in ask command: {e}")
            await update.message.reply_text(
                "Sorry, I couldn't process your question. Please try again later."
            )
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle regular messages as AI queries"""
        query = update.message.text
        
        # Don't respond to empty messages or very short ones
        if not query or len(query) < 2:
            return
        
        await update.message.reply_text("🧠 Processing your message... Please wait.")
        
        try:
            response = await get_ai_response(query)
            await update.message.reply_text(response)
        except Exception as e:
            logger.error(f"Error in message handler: {e}")
            await update.message.reply_text(
                "Sorry, I couldn't process your message. Please try again later."
            )
    
    def setup(self):
        """Set up the bot with all handlers"""
        # Create the Application
        self.application = Application.builder().token(self.token).build()
        
        # Register command handlers
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(CommandHandler('about', self.about_command))
        self.application.add_handler(CommandHandler('summarize', self.summarize_command))
        self.application.add_handler(CommandHandler('ask', self.ask_command))
        self.application.add_handler(CommandHandler('resources', self.resources_command))
        self.application.add_handler(CommandHandler('contact', self.contact_command))
        
        # Register message handler for non-command messages
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
        return self
    
    def run(self):
        """Run the bot"""
        logger.info("Starting ROMA Droid Echo bot...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)