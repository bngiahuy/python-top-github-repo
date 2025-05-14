from dotenv import load_dotenv
from scheduler import start_scheduler
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting application")
    load_dotenv()
    start_scheduler()
