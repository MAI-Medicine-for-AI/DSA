---
layout: default
title: Community Case Reports
nav_order: 8
---

{% assign sorted_cases = site.cases | sort: "path" | reverse %}


# Community-Submitted Case Reports

Each case is formatted using the DSA-1 clinical taxonomy, and includes structured fields such as symptoms, severity, mechanisms, and interventions.


<a class="btn" href="https://github.com/MAI-Medicine-of-Artificial-Intelligence/DSA/issues/new?template=case_report.yml">
  🩺 Report a Case
</a>
<!-- 👇 これが抜けていた！ -->
{% assign chapter_letters = "A,B,C,D,E,F,G,H,I" | split: "," %}
<div style="margin-top: 1em; display: flex; gap: 1em; flex-wrap: wrap;">
  <label>
    <strong>Filter by Chapter:</strong>
    <select id="filter-chapter">
      <option value="">All</option>
      {% for letter in chapter_letters %}
        <option value="{{ letter }}">Chapter {{ letter }}</option>
      {% endfor %}
    </select>
  </label>

  <label>
    <strong>Filter by Severity:</strong>
    <select id="filter-severity">
      <option value="">All</option>
      <option value="4">4 – Severe</option>
      <option value="3">3 – Moderate</option>
      <option value="2">2 – Mild</option>
      <option value="1">1 – No harm</option>
    </select>
  </label>
</div>



---
{% assign case_index = 0 %}
{% for case in sorted_cases %}
  {% assign disorder_code = case.disorder | strip | split: " " | first %}
  {% assign chapter_letter = disorder_code | slice: 0, 1 | upcase %}


<article 
  class="case-entry"
  style="margin-bottom: 3em; padding: 1.5em; border-left: 4px solid #ccc; background: #f9f9f9;"
  data-index="{{ case_index }}"
  data-chapter="{{ chapter_letter }}"
  data-severity="{{ case.severity | slice: 0, 1 }}">


  {% assign filename = case.path | split: "/" | last | split: "." | first | remove: "-" %}
  {% assign disorder_code = case.disorder | strip | split: " " | first %}

  {% if case.title %}
    <h3 style="margin-top: 0.5em;">
      📝 {{ filename }} – {{ disorder_code }}: {{ case.title }}
    </h3>
  {% endif %}
  {% if case.author_display %}
    <p style="margin-top: -0.5em; font-size: 0.9em; color: #666;">
      Submitted by: {{ case.author_display }}
    </p>
  {% endif %}

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
      {% if case.evaluation %}
        <p><strong>Evaluation performed:</strong><br>{{ case.evaluation | markdownify }}</p>
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
{% assign case_index = case_index | plus: 1 %}
{% endfor %}

<!-- ここに移動！ -->
<div id="pagination-controls" style="text-align: center; margin-top: 2em;">
  <button id="prev-page" disabled>← Prev</button>
  <span id="page-info" style="margin: 0 1em;">Page 1</span>
  <button id="next-page">Next →</button>
</div>

<script>
  const chapterFilter = document.getElementById("filter-chapter");
  const severityFilter = document.getElementById("filter-severity");
  const entries = [...document.querySelectorAll(".case-entry")];
  const pageInfo = document.getElementById("page-info");
  const prevBtn = document.getElementById("prev-page");
  const nextBtn = document.getElementById("next-page");

  const ITEMS_PER_PAGE = 10;
  let currentPage = 1;
  let filteredEntries = [];

  function applyFilters() {
    const selectedChapter = chapterFilter.value.trim();
    const selectedSeverity = severityFilter.value.trim();

    filteredEntries = entries.filter(entry => {
      const entryChapter = (entry.dataset.chapter || "").trim();
      const entrySeverity = (entry.dataset.severity || "").trim();

      const matchChapter = !selectedChapter || entryChapter === selectedChapter;
      const matchSeverity = !selectedSeverity || entrySeverity === selectedSeverity;

      return matchChapter && matchSeverity;
    });

    currentPage = 1;
    renderPage();
  }

  function renderPage() {
    const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
    const endIndex = currentPage * ITEMS_PER_PAGE;

    entries.forEach(entry => entry.style.display = "none");
    filteredEntries.slice(startIndex, endIndex).forEach(entry => {
      entry.style.display = "block";
    });

    pageInfo.textContent = `Page ${currentPage} of ${Math.ceil(filteredEntries.length / ITEMS_PER_PAGE)}`;
    prevBtn.disabled = currentPage === 1;
    nextBtn.disabled = endIndex >= filteredEntries.length;
  }

  chapterFilter.addEventListener("change", applyFilters);
  severityFilter.addEventListener("change", applyFilters);
  prevBtn.addEventListener("click", () => {
    if (currentPage > 1) {
      currentPage--;
      renderPage();
    }
  });
  nextBtn.addEventListener("click", () => {
    if (currentPage * ITEMS_PER_PAGE < filteredEntries.length) {
      currentPage++;
      renderPage();
    }
  });

  document.addEventListener("DOMContentLoaded", applyFilters); // ← 初期レンダリング
</script>


<p style="font-size: 0.8em; color: #888;">
Copyright © 2025 MAI Project. This report was submitted by a contributor who has transferred copyright to the project. Licensed under CC BY-SA 4.0.
</p>
  
