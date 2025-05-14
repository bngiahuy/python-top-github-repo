from github import Github
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def fetch_top_repos(keywords, limit=10):
    logger.info(f"Fetching top repos for keywords: {keywords}")
    g = Github(os.getenv("GITHUB_TOKEN"))
    if not g:
        logger.error("GITHUB_TOKEN is not set")
        raise Exception("GITHUB_TOKEN is not set")
    repos = []
    for keyword in keywords:
        logger.info(f"Searching for keyword: {keyword}")
        results = g.search_repositories(query=f"{keyword} in:name,description", sort="stars", order="desc")
        repos.extend(results[:limit])
    # Remove duplicates based on full_name
    unique = {r.full_name: r for r in repos}.values()
    logger.info(f"Found {len(unique)} unique repositories")
    return sorted(unique, key=lambda r: r.stargazers_count, reverse=True)[:limit]
