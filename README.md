# Data Guru Bot

A Telegram bot powered by Google's Gemini AI that helps users prepare for data science interviews. The bot provides expert guidance across multiple domains including machine learning, statistics, deep learning, NLP, computer vision, and more.

## 🌟 Features

- **Comprehensive Interview Preparation**: Covers multiple domains in data science
- **AI-Powered Responses**: Uses Google's Gemini AI for accurate and detailed answers
- **Interactive Learning**: Dynamic conversation flow with follow-up capabilities
- **Domain-Specific Guidance**: Specialized prompts for different areas of expertise

## 📋 Topics Covered

- General Interview Preparation
- AI Industry Questions
- Data Analysis
- Statistics
- Machine Learning
- Deep Learning
- Natural Language Processing
- Computer Vision
- Generative AI

## 🚀 Setup and Installation

### Prerequisites

- Python 3.10 or higher
- Telegram Bot Token (from [BotFather](https://telegram.me/BotFather))
- Google API Key (for Gemini AI)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/Krish-Goyani/Data_Guru_Bot
cd data-guru-bot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in the root directory:
```env
BOT_TOKEN=your_telegram_bot_token
GOOGLE_API_KEY=your_google_api_key
```

5. Run the bot:
```bash
python bot.py
```

## 🤖 Bot Commands

- `/start` or `/help` - Display welcome message and available commands
- `/general_interview` - Get general interview preparation questions and tips
- `/ai_general` - Get AI industry-specific questions
- `/data_analysis` - Data analysis interview questions
- `/statistics` - Statistics concept questions
- `/machine_learning` - Machine learning algorithm questions
- `/deep_learning` - Deep learning architecture questions
- `/nlp` - Natural Language Processing questions
- `/computer_vision` - Computer Vision questions
- `/generative_ai` - Generative AI questions

## 💡 Usage Examples

1. Start the bot:
```
/start
```

2. Select a topic:
```
/machine_learning
```

3. Ask specific questions:
```
What is the difference between bagging and boosting?
```

---
Made with ❤️ for the data science community
