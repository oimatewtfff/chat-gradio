import os
from dotenv import load_dotenv

from g4f.client import Client
from g4f.Provider import FreeChatgpt, Aura, GeminiProChat, Koala, You, Liaobots
from g4f.errors import RateLimitError, ProviderNotWorkingError

from logger_config import setup_logger

load_dotenv()
logger = setup_logger()
client = Client()

API_KEY = os.getenv("API_KEY")


def ask_gpt(message, history):
    available_providers = [Liaobots, FreeChatgpt, Aura, GeminiProChat, Koala, You]

    message_with_history = []
    for pair in history:
        message_with_history.append({"role": "user", "content": pair[0]})
        message_with_history.append({"role": "assistant", "content": pair[1]})

    message_with_history.append({"role": "user", "content": message})

    for provider in available_providers:
        try:
            response = client.chat.completions.create(
                provider=provider,
                model="gpt-3.5-turbo",
                messages=message_with_history,
            )
            answer = response.choices[0].message.content

            return answer
        except RateLimitError as e:
            logger.error(f"Превышен лимит запросов для провайдера {provider.__name__}: {e}")
            continue
        except ProviderNotWorkingError as e:
            logger.error(f"Провайдер {provider.__name__} не работает: {e}")
            continue
        except Exception as e:
            logger.error(f"Возникла неизвестная ошибка: {e}")
