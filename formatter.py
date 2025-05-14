from datetime import datetime

def format_repos(repos):
    lines = ["🔥 **Top GitHub Repositories Today** 🔥\n", f"⏳ Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
    for i, repo in enumerate(repos, 1):
        lines.append(f"{i}. [{repo.full_name}]({repo.html_url}) ★ {repo.stargazers_count}\n_{repo.description}_\n")
    return "\n".join(lines)
