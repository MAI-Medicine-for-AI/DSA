import sys
import os
import requests

issue_number = sys.argv[1]
repo = os.environ['GITHUB_REPOSITORY']
token = os.environ['GH_TOKEN']

url = f'https://api.github.com/repos/{repo}/issues/{issue_number}'
headers = {'Authorization': f'token {token}'}

r = requests.get(url, headers=headers)
issue = r.json()

body = issue["body"]
lines = body.split("\n")

def extract(field):
    for i, line in enumerate(lines):
        if line.strip() == f"### {field}":
            if i + 1 < len(lines):
                return lines[i + 1].strip()
    return ""

title = issue["title"]
disorder = extract("Disorder code (DSA-1)")
model = extract("Model / Version")
severity = extract("Severity (1 = mild, 5 = catastrophic)")
repro = extract("Failure description & reproduction steps")
evidence = extract("Evidence (e.g., URLs, logs)")

print("==== DEBUG ====")
print("Title:", title)
print("Disorder:", disorder)
print("Model:", model)
print("Severity:", severity)
print("Repro:", repro)
print("Evidence:", evidence)

filename = f"_cases/case-{issue_number}.md"
with open(filename, "w") as f:
    f.write(f"""---
title: "{title}"
disorder: "{disorder}"
model: "{model}"
severity: "{severity}"
---

## Reproduction Steps

{repro}

## Evidence

{evidence}
""")


