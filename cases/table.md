---
layout: default
title: Community Case Reports table
nav_order: 9
---

{% assign sorted_cases = site.cases | sort: "path" | reverse %}
{% assign case_index = 0 %}

# Community-Submitted Case Reports

Each case is formatted using the DSA-1 clinical taxonomy, and includes structured fields such as symptoms, severity, mechanisms, and interventions.

<a class="btn" href="https://github.com/MAI-Medicine-of-Artificial-Intelligence/DSA/issues/new?template=case_report.yml">
  🩺 Report a Case
</a>

---

| Case ID | Disorder Code(s) | Title | Severity | Model | Key Symptom |
|---------|------------------|-------|----------|--------|-------------|
{% for case in sorted_cases %}
  {% assign disorder_codes = case.disorder %}
  {% if disorder_codes contains "[" %}
    {% assign disorder_list = disorder_codes | replace: "[", "" | replace: "]", "" | split: "," %}
  {% else %}
    {% assign disorder_list = case.disorder | split: "," %}
  {% endif %}
  {% assign first_disorder = disorder_list[0] | strip %}
  {% assign disorder_code = first_disorder | split: " " | first %}
  {% assign chapter_letter = disorder_code | slice: 0, 1 | upcase %}
  {% assign filename = case.path | split: "/" | last | split: "." | first | remove: "-" %}

| {{ filename }} | {{ disorder_list | join: "<br>" | strip }} | {{ case.title | strip }} | {{ case.severity | slice: 0, 1 }} | {{ case.model | strip }} | {{ case.symptoms | strip_html | truncate: 100 }} |
{% assign case_index = case_index | plus: 1 %}
{% endfor %}
