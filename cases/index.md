---
layout: default
title: Community Case Reports
nav_order: 8
---

# Community-Submitted Case Reports

Each case is formatted using the DSA-1 clinical taxonomy, and includes structured fields such as symptoms, severity, mechanisms, and interventions.

---
<a class="btn" href="https://github.com/MAI-Medicine-of-Artificial-Intelligence/DSA/issues/new?template=case_report.yml">
  🩺 Report a Case
</a>

---

{% assign sorted_cases = site.cases | sort: "title" %}
{% for case in sorted_cases %}
<article style="margin-bottom: 3em; padding: 1.5em; border-left: 4px solid #ccc; background: #f9f9f9;">
  <h2 style="margin-bottom: 0.5em;">{{ case.title }}</h2>

  {% if case.disorder %}
    <p><strong>Disorder code (DSA-1):</strong> {{ case.disorder }}</p>
  {% endif %}
  {% if case.model %}
    <p><strong>Model / Version:</strong> {{ case.model }}</p>
  {% endif %}
  {% if case.symptoms %}
    <p><strong>Symptom(s) observed:</strong><br>{{ case.symptoms | markdownify }}</p>
  {% endif %}

  <details>
    <summary style="cursor: pointer; font-weight: bold; margin-top: 1em;"> Show full case report</summary>
    <div style="margin-top: 1em;">

      {% if case.repro %}
        <p><strong>Failure description & reproduction steps:</strong><br>{{ case.repro | markdownify }}</p>
      {% endif %}
      {% if case.severity %}
        <p><strong>Severity (DSA-1):</strong> {{ case.severity }}</p>
      {% endif %}
      {% if case.intervention %}
        <p><strong>Intervention or treatment:</strong><br>{{ case.intervention | markdownify }}</p>
      {% endif %}
      {% if case.outcome %}
        <p><strong>Outcome / Follow-up:</strong><br>{{ case.outcome | markdownify }}</p>
      {% endif %}
      {% if case.evidence and case.evidence != "_No response_" %}
        <p><strong>Evidence (e.g., URLs, logs):</strong><br>{{ case.evidence | markdownify }}</p>
      {% endif %}
      {% if case.mechanism %}
        <p><strong>Presumed underlying mechanism:</strong><br>{{ case.mechanism | markdownify }}</p>
      {% endif %}
      {% if case.detectability %}
        <p><strong>Detectability of failure:</strong> {{ case.detectability }}</p>
      {% endif %}
      {% if case.occurrence %}
        <p><strong>Estimated frequency / prevalence:</strong> {{ case.occurrence }}</p>
      {% endif %}
      {% if case.confidence %}
        <p><strong>Diagnostic confidence:</strong> {{ case.confidence }}</p>
      {% endif %}
      {% if case.algorithm %}
        <p><strong>Diagnostic pathway (if applicable):</strong> {{ case.algorithm }}</p>
      {% endif %}

    </div>
  </details>
</article>
{% endfor %}
