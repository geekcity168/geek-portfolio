# projects/utils.py
import requests

def get_github_project_stats(repo_url):
    try:
        repo_path = repo_url.rstrip('/').split('github.com/')[-1]
        api_url = f"https://api.github.com/repos/{repo_path}"
        headers = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {
                'stars': data['stargazers_count'],
                'forks': data['forks_count'],
                'issues': data['open_issues_count'],
            }
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
    return {'stars': 0, 'forks': 0, 'issues': 0}