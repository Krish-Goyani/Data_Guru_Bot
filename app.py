import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import google.generativeai as genai
import markdown2
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
        history=[
            {"role": "model", "parts": f"Hello Gemini"}
        ]
    )


TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher()


general_interview_prompt = '''You are an expert interview coach specializing in professional development. When responding to general interview questions:
- Provide concise, structured answers limited to 3-4 key points
- Include specific examples or scenarios where relevant
- Focus on demonstrating both technical competence and soft skills
- Add brief follow-up tips or common mistakes to avoid
- Keep responses under 200 words unless specifically asked for more detail
- Format responses with clear bullet points or numbered lists for readability
- In response of this prompt list out common inerview question along with how to answer them and also some tips.'''
ai_general_prompt = '''You are an AI industry expert with extensive interview experience. For AI-related interview questions:
- Focus on both theoretical understanding and practical applications
- Reference current industry trends and best practices
- Include ethical considerations where relevant
- Explain complex concepts using simple analogies
- Highlight the business impact of AI solutions
- Structure responses to show both breadth and depth of knowledge
- Keep technical jargon minimal unless specifically required
- Add brief mentions of relevant tools or frameworks
- In response of this prompt list out common inerview question along with how to answer them and also some tips.'''
data_analysis_prompt = '''You are a senior data analyst with expertise in interview preparation. For data analysis questions:
- Start with the fundamental concept or methodology
- Explain practical applications in business contexts
- Include specific tools or libraries commonly used
- Provide a brief example of implementation where relevant
- Mention common pitfalls and how to avoid them
- Focus on data quality, cleaning, and validation aspects
- Reference relevant statistical concepts when applicable
- Keep responses focused on practical implementation
- Use SQL examples where appropriate
- In response of this prompt list out common inerview question along with how to answer them and also some tips.'''
statistics_prompt = '''You are a statistics expert preparing candidates for technical interviews. When answering statistics questions:
- Begin with a clear, concise definition
- Explain the underlying mathematical concept briefly
- Provide a real-world application or example
- Include key assumptions and limitations
- Use simple numerical examples where helpful
- Highlight common misunderstandings
- Mention related statistical concepts
- Include formulas only when necessary
- Focus on intuitive understanding over mathematical derivation
- In response of this prompt list out common inerview question along with how to answer them and also some tips.
'''
machine_learning_prompt = '''You are a machine learning engineer with extensive interview experience. For ML questions:
- Start with a clear, conceptual explanation
- Break down complex algorithms into simple steps
- Include advantages and limitations
- Provide real-world applications
- Mention relevant evaluation metrics
- Discuss computational complexity when relevant
- Include model selection considerations
- Reference popular implementations or libraries
- Add brief code snippets only when crucial
- Highlight common optimization techniques
- In response of this prompt list out common inerview question along with how to answer them and also some tips.
'''
deep_learning_prompt = '''You are a deep learning specialist preparing candidates for technical interviews. For DL questions:
- Begin with the architectural concept
- Explain the mathematical intuition simply
- Include practical implementation considerations
- Discuss common hyperparameters and their effects
- Mention optimization techniques
- Reference popular frameworks (PyTorch, TensorFlow)
- Include network architecture considerations
- Discuss computational requirements
- Add training best practices
- Highlight recent developments in the field
- In response of this prompt list out common inerview question along with how to answer them and also some tips.
'''
nlp_prompt = '''You are an NLP expert preparing candidates for technical interviews. When answering NLP questions:
- Start with the core NLP concept
- Explain preprocessing steps where relevant
- Include both traditional and modern approaches
- Mention popular NLP libraries and tools
- Discuss evaluation metrics specific to NLP
- Reference current state-of-the-art models
- Include language-specific considerations
- Mention common challenges and solutions
- Discuss scalability aspects
- Reference relevant research papers briefly
- In response of this prompt list out common inerview question along with how to answer them and also some tips.
'''
computer_vision_prompt = '''You are a computer vision expert preparing candidates for technical interviews. For CV questions:
- Begin with the fundamental concept
- Explain image processing steps where relevant
- Include both classical and deep learning approaches
- Mention popular CV libraries and frameworks
- Discuss specific preprocessing requirements
- Reference architectural considerations
- Include performance optimization techniques
- Mention deployment considerations
- Discuss real-time processing aspects
- Reference benchmark datasets when relevant
- In response of this prompt list out common inerview question along with how to answer them and also some tips.
'''
generative_ai_prompt = '''You are a generative AI specialist preparing candidates for cutting-edge interviews. For GenAI questions:
- Start with the latest architectures and approaches
- Explain the underlying generation process
- Include training and fine-tuning considerations
- Discuss prompt engineering aspects
- Mention ethical considerations and limitations
- Reference current industry applications
- Include deployment and scaling aspects
- Discuss evaluation metrics
- Mention resource requirements
- Reference recent breakthroughs and papers
- In response of this prompt list out common inerview question along with how to answer them and also some tips.'''


@dispatcher.message(Command(commands=['start', 'help']))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    start_message = '''
    👋 Welcome to Data Guru Bot! 

    I'm your AI-powered interview preparation assistant, designed to help you ace your Data Science interviews. I provide detailed answers to interview questions across multiple domains of Data Science.

    🎯 How to use this bot:
    Use these commands to practice specific interview topics:

    📌 General Interview Prep
    /general_interview - Common behavioral and professional questions
    /ai_general - General AI industry questions

    📊 Data & Statistics
    /data_analysis - Data analysis and visualization questions
    /statistics - Statistical concepts and methods

    🤖 Machine Learning & Deep Learning
    /machine_learning - Traditional ML algorithms and concepts
    /deep_learning - Neural networks and deep learning architectures

    🔬 Specialized Fields
    /nlp - Natural Language Processing
    /computer_vision - Computer Vision
    /generative_ai - Generative AI and Large Language Models

    💡 Tips for best results:
    - Choose a specific command based on your interview focus
    - Ask clear, focused questions
    - Request examples if needed
    - Follow up for clarification if needed

    🚀 Getting Started:
    1. Select a topic using one of the commands above
    2. Ask your question
    3. Get a detailed, interview-focused response

    ❓ For example:
    After using /statistics, you could ask:
    "Explain p-value in simple terms"
    or
    After /machine_learning:
    "What is the difference between bagging and boosting?"

    Type /help anytime to see this menu again.

    Ready to start your interview prep? Choose a command to begin! 🎯
    '''
    await message.answer(start_message)
# Helper function to split messages if they exceed Telegram's character limit
def split_message(message, max_length=4096):
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]

@dispatcher.message(Command(commands=['general_interview']))
async def general_interview_handler(message: Message):
    response = chat.send_message(general_interview_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

@dispatcher.message(Command(commands=['ai_general']))
async def ai_general_handler(message: Message):
    response = chat.send_message(ai_general_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

@dispatcher.message(Command(commands=['data_analysis']))
async def data_analysis_handler(message: Message):
    response = chat.send_message(data_analysis_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

@dispatcher.message(Command(commands=['statistics']))
async def statistics_handler(message: Message):
    response = chat.send_message(statistics_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

@dispatcher.message(Command(commands=['machine_learning']))
async def machine_learning_handler(message: Message):
    response = chat.send_message(machine_learning_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

@dispatcher.message(Command(commands=['deep_learning']))
async def deep_learning_handler(message: Message):
    response = chat.send_message(deep_learning_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

@dispatcher.message(Command(commands=['nlp']))
async def nlp_handler(message: Message):
    response = chat.send_message(nlp_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

@dispatcher.message(Command(commands=['computer_vision']))
async def computer_vision_handler(message: Message):
    response = chat.send_message(computer_vision_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

@dispatcher.message(Command(commands=['generative_ai']))
async def generative_ai_handler(message: Message):
    response = chat.send_message(generative_ai_prompt)
    messages = split_message(response.text)
    for msg in messages:
        await message.answer(msg)

'''@dispatcher.message(Command(commands=['general_interview']))
async def general_interview_handler(message: Message):
    response = chat.send_message(general_interview_prompt)
    await message.answer(response.text)


@dispatcher.message(Command(commands=['ai_general']))
async def ai_general_handler(message: Message):
    response = chat.send_message(ai_general_prompt)
    await message.answer(response.text)


@dispatcher.message(Command(commands=['data_analysis']))
async def data_analysis_handler(message: Message):
    response = chat.send_message(data_analysis_prompt)
    await message.answer(response.text)


@dispatcher.message(Command(commands=['statistics']))
async def statistics_handler(message: Message):
    response = chat.send_message(statatistics_prompt)
    await message.answer(response.text)


@dispatcher.message(Command(commands=['machine_learning']))
async def machine_learning_handler(message: Message):
    response = chat.send_message(machine_learning_prompt)
    await message.answer(response.text)


@dispatcher.message(Command(commands=['deep_learning']))
async def deep_learning_handler(message: Message):
    response = chat.send_message(deep_learning_prompt)
    await message.answer(response.text)


@dispatcher.message(Command(commands=['nlp']))
async def nlp_handler(message: Message):
    response = chat.send_message(nlp_prompt)
    await message.answer(response.text)


@dispatcher.message(Command(commands=['computer_vision']))
async def computer_vision_handler(message: Message):
    response = chat.send_message(computer_vision_prompt)
    await message.answer(response.text)


@dispatcher.message(Command(commands=['generative_ai']))
async def generative_ai_handler(message: Message):
    response = chat.send_message(generative_ai_prompt)
    await message.answer(response.text)
'''


@dispatcher.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    response = chat.send_message(message)
    await message.answer(response.text)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    # And the run events dispatching
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


