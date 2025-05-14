import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


def send_telegram_message(text):
    logger.info("Sending Telegram message")
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        logger.error("Telegram credentials not set")
        raise Exception("Telegram credentials not set")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    headers = {
        "accept": "application/json",
        "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        "content-type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        logger.error(f"Failed to send Telegram message: {response.text}")
        raise Exception(f"Failed to send Telegram message: {response.text}")
    logger.info(f"Telegram message sent with status: {response.status_code}")
    return response
