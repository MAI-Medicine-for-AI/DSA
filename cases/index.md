---
layout: default
title: Community Case Reports
nav_order: 8
---

# Community-Submitted Case Reports

This section lists all AI anomaly cases submitted by the community using the DSA-1 framework.  
Each case includes a structured report with the model name, symptoms, mechanism, severity, and reproduction steps.

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
      <p><strong>Disorder:</strong> {{ case.disorder }}</p>
    {% endif %}
    {% if case.model %}
      <p><strong>Model:</strong> {{ case.model }}</p>
    {% endif %}
    {% if case.severity %}
      <p><strong>Severity:</strong> {{ case.severity }}</p>
    {% endif %}
    {% if case.detectability %}
      <p><strong>Detectability:</strong> {{ case.detectability }}</p>
    {% endif %}
    {% if case.confidence %}
      <p><strong>Diagnostic Confidence:</strong> {{ case.confidence }}</p>
    {% endif %}
    {% if case.occurrence %}
      <p><strong>Estimated Prevalence:</strong> {{ case.occurrence }}</p>
    {% endif %}
    {% if case.symptoms %}
      <p><strong>Symptoms:</strong><br>{{ case.symptoms | markdownify }}</p>
    {% endif %}
    {% if case.mechanism %}
      <p><strong>Presumed Mechanism:</strong><br>{{ case.mechanism | markdownify }}</p>
    {% endif %}
    {% if case.repro %}
      <p><strong>Reproduction Steps:</strong><br>{{ case.repro | markdownify }}</p>
    {% endif %}
    {% if case.intervention %}
      <p><strong>Intervention:</strong><br>{{ case.intervention | markdownify }}</p>
    {% endif %}
    {% if case.outcome %}
      <p><strong>Outcome / Follow-up:</strong><br>{{ case.outcome | markdownify }}</p>
    {% endif %}
    {% if case.evidence and case.evidence != "_No response_" %}
      <p><strong>Evidence:</strong><br>{{ case.evidence | markdownify }}</p>
    {% endif %}
  </article>
{% endfor %}


