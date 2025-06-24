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
def extract_consent():
    clauses = [
        "I confirm that this report does not contain any personally identifiable information (PII), private data, or confidential content.",
        "I understand that this report will be publicly visible and published under the Creative Commons BY-SA 4.0 license.",
        "I understand that inappropriate or malicious submissions may be moderated or removed."
    ]
    for clause in clauses:
        matched = False
        for line in lines:
            if clause in line:
                if "[x]" in line.lower():
                    matched = True
                    break
        if not matched:
            return "not_confirmed"
    return "confirmed"

author_login = issue["user"]["login"]  # ← ここでGitHub IDを取得
title = escape(issue["title"])
disorder = escape(extract("Disorder code (DSA-1)"))
model = escape(extract("Model / Version"))
evaluation = escape(extract("Evaluation performed (optional)"))
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
author_preference = extract("Author name display preference")
consent = extract_consent()

if author_preference == "GitHub ID (public)":
    author_display = author_login
else:
    author_display = "Anonymous"
    
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
evaluation: "{evaluation}"
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
author_display: "{escape(author_display)}"
consent: "{consent}"
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

## Evaluation

{evaluation}

## author_display

This report was submitted as: **{author_display}**

## Diagnostic Details

- **Severity:** {severity}
- **Detectability:** {detectability}
- **Estimated Prevalence:** {occurrence}
- **Diagnostic Confidence:** {confidence}
- **Diagnostic Pathway:** {algorithm}
""")

