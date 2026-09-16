"""
Bulk-creates all bug issues on your GitHub repo.

Setup:
1. pip install requests
2. Create a GitHub Personal Access Token (classic) with "repo" scope:
   https://github.com/settings/tokens
3. Run:  python create_issues.py <owner> <repo> <your_token>
   e.g.: python create_issues.py dhruv campuscart ghp_xxxxxxxxxxxx

This reads issues.json (generated alongside this script) and creates
one GitHub Issue per bug, with labels.
"""
import sys
import json
import time
import requests

def main():
    if len(sys.argv) != 4:
        print("Usage: python create_issues.py <owner> <repo> <token>")
        sys.exit(1)

    owner, repo, token = sys.argv[1], sys.argv[2], sys.argv[3]

    with open("issues.json") as f:
        issues = json.load(f)

    label_defs = {
        "frontend": "1f77b4",
        "backend": "d62728",
        "good-first-issue": "2ea44f",
        "intermediate": "fbca04",
    }
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    for name, color in label_defs.items():
        requests.post(
            f"https://api.github.com/repos/{owner}/{repo}/labels",
            headers=headers,
            json={"name": name, "color": color},
        )

    created = 0
    for issue in issues:
        resp = requests.post(
            f"https://api.github.com/repos/{owner}/{repo}/issues",
            headers=headers,
            json={"title": issue["title"], "body": issue["body"], "labels": issue["labels"]},
        )
        if resp.status_code == 201:
            created += 1
            print(f"Created: {issue['title']}")
        else:
            print(f"FAILED ({resp.status_code}): {issue['title']} -> {resp.text}")
        time.sleep(1)

    print(f"\nDone. Created {created}/{len(issues)} issues.")

if __name__ == "__main__":
    main()
