# GitHub Repository Monitor

## Introduction
This project monitors top GitHub repositories based on specified keywords and sends notifications via Telegram. It includes components for fetching, formatting, and scheduling updates.

## Requirements
- Python 3.12+
- Docker (optional)
- Telegram bot token (set in .env)
- GitHub API token (set in .env)

## How to Use
### Local Development
1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` file with your tokens
3. Run: `python main.py`

### Docker
1. Build: `docker-compose build`
2. Run: `docker-compose up -d`

### Configuration
Edit `.env` to customize:
- `KEYWORDS`: Comma-separated search terms
- `REPO_LIMIT`: Number of repos to fetch
- `TELEGRAM_CHAT_ID`: Target chat ID
- `TELEGRAM_TOKEN`: Your bot token
- `GITHUB_TOKEN`: Your GitHub token