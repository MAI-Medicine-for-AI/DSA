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
    field_line = f"### {field}".lower().strip()
    for i, line in enumerate(lines):
        if line.strip().lower().startswith(field_line):
            # その次の行が本文（空行の可能性もあるためスキップして探す）
            for j in range(i + 1, len(lines)):
                content = lines[j].strip()
                if content:  # 空じゃなければ返す
                    return content
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
print("==== FULL BODY ====")
print(body)

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


