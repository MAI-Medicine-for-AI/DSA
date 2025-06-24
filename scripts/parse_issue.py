import sys
import os
import requests
import json
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
def extract_multi(field):
    field_line = f"### {field}".lower().strip()
    values = []
    inside_field = False
    for line in lines:
        stripped = line.strip()
        if stripped.lower().startswith(field_line):
            inside_field = True
            continue
        if inside_field:
            if stripped.startswith("### "):  # 次のセクションが始まったら終了
                break
            if stripped.startswith("- [x] "):  # チェックされたものだけを対象にする
                values.append(stripped[6:].strip())
    return values



author_login = issue["user"]["login"]  # ← ここでGitHub IDを取得
title = escape(issue["title"])
disorder_list = extract_multi("Disorder code(s) (DSA-1)")
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
disorder_str = ", ".join(disorder_list)
disorder_yaml = f'"{disorder_str}"'  # ダブルクオート付きで1つの文字列としてYAMLに書き込む

disorder_md = ", ".join(disorder_list)  # Markdown用にカンマ区切り表示
if author_preference == "GitHub ID (public)":
    author_display = author_login
else:
    author_display = "Anonymous"
    
print("==== DEBUG ====")
print("Title:", title)
print("Disorder:", disorder_md)
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
disorder: {disorder_yaml}
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
## Disorder Code(s)

{disorder_md}


json_data = {
    "case_id": int(issue_number),
    "title": title,
    "disorder": disorder_list,
    "model": model,
    "severity": severity,
    "evaluation": evaluation,
    "detectability": detectability,
    "occurrence": occurrence,
    "confidence": confidence,
    "algorithm": algorithm,
    "mechanism": mechanism,
    "symptoms": symptoms,
    "intervention": intervention,
    "outcome": outcome,
    "repro": repro,
    "evidence": evidence,
    "author_display": author_display
    
}

json_filename = f"_cases/case-{int(issue_number):03}.json"
with open(json_filename, "w") as jf:
    json.dump(json_data, jf, indent=2, ensure_ascii=False)


