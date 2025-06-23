---
layout: default
title: Community Case Reports
nav_order: 8
---

# Community-Submitted Case Reports

This section lists all AI anomaly cases submitted by the community using the DSA-1 framework.  
Each case includes a structured report with the model name, symptoms, severity, and reproduction steps.

---

{% for case in site.cases %}
  <article style="margin-bottom: 2em;">
    <h2>{{ case.title }} ({{ case.disorder }})</h2>
    <p><strong>Model:</strong> {{ case.model }}  
    <br><strong>Severity:</strong> {{ case.severity }}</p>
    <p>{{ case.repro | markdownify | truncatewords: 40 }}</p>
    <a href="{{ case.url }}">Read full case</a>
  </article>
{% endfor %}
