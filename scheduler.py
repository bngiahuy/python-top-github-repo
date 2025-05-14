import schedule
import time
from fetcher import fetch_top_repos
from formatter import format_repos
from notifier import send_telegram_message
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def job():
    logger.info("Running scheduled job")
    keywords = os.getenv("KEYWORDS", "").split(",")
    repos = fetch_top_repos(keywords, int(os.getenv("REPO_LIMIT", 50)))
    message = format_repos(repos)
    send_telegram_message(message[:4000])  # Telegram giới hạn 4096 ký tự
    logger.info("Job completed successfully")

def start_scheduler():
    logger.info("Starting scheduler")
    schedule.every().day.do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)