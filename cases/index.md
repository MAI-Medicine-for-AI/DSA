---
layout: default
title: Community Case Reports
nav_order: 8
---

# Community-Submitted Case Reports

This section lists all AI anomaly cases submitted by the community using the DSA-1 framework.  
Each case includes a structured report with the model name, symptoms, severity, and reproduction steps.

---

{% assign sorted_cases = site.cases | sort: "title" %}
{% for case in sorted_cases %}
  <article style="margin-bottom: 2em; padding: 1em; border-left: 4px solid #ccc; background: #f9f9f9;">
    <h2 style="margin-bottom: 0.2em;">{{ case.title }}</h2>
    {% if case.disorder %}
      <p><strong>Disorder:</strong> {{ case.disorder }}</p>
    {% endif %}
    {% if case.model %}
      <p><strong>Model:</strong> {{ case.model }}</p>
    {% endif %}
    {% if case.severity %}
      <p><strong>Severity:</strong> {{ case.severity }}</p>
    {% endif %}
    {% if case.repro %}
      <p><strong>Summary:</strong><br>{{ case.repro | markdownify }}</p>
    {% endif %}
    {% if case.evidence and case.evidence != "_No response_" %}
      <p><strong>Evidence:</strong><br>{{ case.evidence | markdownify }}</p>
    {% endif %}
    <p><a href="{{ case.url }}">→ View Full Case</a></p>
  </article>
{% endfor %}


