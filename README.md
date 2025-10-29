![1DFB164B-F97E-4BA8-8D88-B8B0A1CFD52F](https://github.com/user-attachments/assets/54fa9414-e0d4-4dd9-8fd7-00ac5ef1c279)
# ROMA Droid Echo
![ROMA Droid Echo](https://img.shields.io/badge/ROMA-Droid%20Echo-blue) <br/>
A Telegram bot that connects users to the Sentient ecosystem, providing a minimalist text AI interface for chatting and summarizing content related to ROMA (Recursive Open Meta Agent).<br/>


## 🤖 About

ROMA Droid Echo solves the problem of accessibility, fragmentation, and complexity in AI and decentralized ecosystems by offering:

- **A unified, chat-based interface** for interacting with Sentient
- **Low-barrier access** to decentralized AI tools
- **Smart summarization** to combat information overload
- **A minimalist design** that prioritizes ease of use
- **A bridge between Web2 and Web3**, meeting users where they already are

This bot serves as a gateway to the Sentient ecosystem, allowing users to learn about ROMA, ask questions, and summarize content through a familiar chat interface.

## 🚀 Features

- **AI Chat**: Ask questions about ROMA, Sentient, and related topics
- **Content Summarization**: Summarize articles, blog posts, and other content
- **Resource Access**: Quick access to Sentient ecosystem resources
- **Simple Interface**: Easy-to-use commands and natural language interaction

## 📋 Commands

- `/start` - Start the bot
- `/help` - Show help message
- `/about` - Learn about ROMA and Sentient
- `/summarize [URL or text]` - Summarize content
- `/ask [question]` - Ask ROMA about anything
- `/resources` - Get useful Sentient resources
- `/contact` - Get contact information

## 🛠️ Setup

### Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- A Fireworks AI API Key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ROMA-Driod.git
   cd ROMA-Driod
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy `.env.example` to `.env` (if not already present)
   - Update the `.env` file with your Telegram Bot Token and Fireworks API Key

4. Run the bot:
   ```bash
   python -m src.main
   ```

## 🏗️ Project Structure

```
ROMA-Driod/
├── src/
│   ├── bot/
│   │   ├── __init__.py
│   │   └── bot.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── ai_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── logger.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── __init__.py
│   └── main.py
├── data/
├── logs/
├── .env
├── requirements.txt
└── README.md
```

## 🔄 How It Works

1. **User Interaction**: Users interact with the bot through Telegram
2. **Command Processing**: The bot processes commands and messages
3. **AI Integration**: For questions and summarization, the bot uses Fireworks AI API
4. **Response Generation**: The bot generates and sends responses back to the user

## 🔗 Related Links

- [ROMA GitHub Repository](https://github.com/sentient-agi/ROMA)
- [Recursive Open Meta Agent Blog](https://blog.sentient.xyz/posts/recursive-open-meta-agent)
- [Sentient Website](https://www.sentient.xyz/)
- [Sentient Synthetic](https://sentient-synthetic.vercel.app/)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Sentient AGI](https://www.sentient.xyz/) for creating ROMA
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library
- [Fireworks AI](https://fireworks.ai/) for providing the AI API
