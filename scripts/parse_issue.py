import sys
import os
import requests

def escape(s):
    return s.replace('"', '\\"').replace("\n", " ").strip()

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
            for j in range(i + 1, len(lines)):
                content = lines[j].strip()
                if content:
                    return content
    return ""

title = escape(issue["title"])
disorder = escape(extract("Disorder code (DSA-1)"))
model = escape(extract("Model / Version"))
severity = escape(extract("Severity (DSA-1)"))
repro = extract("Failure description & reproduction steps")  # このままMarkdown本文用に
evidence = extract("Evidence (e.g., URLs, logs)")
symptoms = extract("Symptom(s) observed")
intervention = extract("Intervention or treatment")
outcome = extract("Outcome / Follow-up")
mechanism = extract("Presumed underlying mechanism")
detectability = extract("Detectability of failure")
occurrence = extract("Estimated frequency / prevalence")
confidence = extract("Diagnostic confidence")
algorithm = extract("Diagnostic pathway (if applicable)")
print("==== DEBUG ====")
print("Title:", title)
print("Disorder:", disorder)
print("Model:", model)
print("Severity:", severity)
print("Repro:", repro)
print("Evidence:", evidence)
print("==== FULL BODY ====")
print(body)

filename = f"_cases/case-{int(issue_number):03}.md"
with open(filename, "w") as f:
    f.write(f"""---
title: "{title}"
disorder: "{disorder}"
model: "{model}"
severity: "{severity}"
detectability: "{detectability}"
occurrence: "{occurrence}"
confidence: "{confidence}"
algorithm: "{algorithm}"
mechanism: "{escape(mechanism)}"
symptoms: "{escape(symptoms)}"
intervention: "{escape(intervention)}"
outcome: "{escape(outcome)}"
repro: "{escape(repro)}"
evidence: "{escape(evidence)}"
---

## Symptoms

{symptoms}

## Presumed Mechanism

{mechanism}

## Reproduction Steps

{repro}

## Evidence

{evidence}

## Intervention

{intervention}

## Outcome / Follow-up

{outcome}

## Diagnostic Details

- **Severity:** {severity}
- **Detectability:** {detectability}
- **Estimated Prevalence:** {occurrence}
- **Diagnostic Confidence:** {confidence}
- **Diagnostic Pathway:** {algorithm}
""")

