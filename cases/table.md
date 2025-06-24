---
layout: default
title: Community-Submitted Case Reports 
nav_order: 9
---
{% assign sorted_cases = site.cases | sort: "path" | reverse %}


# Community-Submitted Case Reports

Each case is formatted using the DSA-1 clinical taxonomy, and includes structured fields such as symptoms, severity, mechanisms, and interventions.


<a class="btn" href="https://github.com/MAI-Medicine-of-Artificial-Intelligence/DSA/issues/new?template=case_report.yml">
  🩺 Report a Case
</a>
<!-- 👇 これが抜けていた！ -->
{% assign chapter_letters = "A,B,C,D,E,F,G,H,I,Z" | split: "," %}
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
  {% assign disorder_codes = case.disorder %}
  {% if disorder_codes contains "[" %}
    {% assign disorder_list = disorder_codes | replace: "[", "" | replace: "]", "" | split: "," %}
  {% else %}
    {% assign disorder_list = case.disorder | split: "," %}
  {% endif %}

  {% assign first_disorder = disorder_list[0] | strip %}
  {% assign disorder_code = first_disorder | split: " " | first %}
  {% assign chapter_letter = disorder_code | slice: 0, 1 | upcase %}



<article 
  class="case-entry"
  style="margin-bottom: 3em; padding: 1.5em; border-left: 4px solid #ccc; background: #f9f9f9;"
  data-index="{{ case_index }}"
  data-chapter="{{ chapter_letter }}"
  data-severity="{{ case.severity | slice: 0, 1 }}">


  {% assign filename = case.path | split: "/" | last | split: "." | first | remove: "-" %}
 

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

  {% if disorder_list %}
    <p><strong>Disorder code(s) (DSA-1):</strong>
      <ul>
      {% for d in disorder_list %}
        <li>{{ d | strip | remove: '"' }}</li>
      {% endfor %}
      </ul>
    </p>
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

    <table style="width: 100%; border-collapse: collapse; font-size: 0.95em;">
      <thead>
        <tr>
          <th style="text-align: left; width: 30%; padding: 0.5em; background: #f0f0f0;">Field</th>
          <th style="text-align: left; padding: 0.5em; background: #f0f0f0;">Description</th>
        </tr>
      </thead>
      <tbody>
        {% if case.title %}
        <tr><td>Title</td><td>{{ case.title }}</td></tr>
        {% endif %}
        {% if disorder_list %}
        <tr>
          <td>Disorder code(s)</td>
          <td>
            <ul style="margin: 0; padding-left: 1em;">
            {% for d in disorder_list %}
              <li>{{ d | strip | remove: '"' }}</li>
            {% endfor %}
            </ul>
          </td>
        </tr>
        {% endif %}
        {% if case.model %}
        <tr><td>Model / Version</td><td>{{ case.model }}</td></tr>
        {% endif %}
        {% if case.symptoms %}
        <tr><td>Symptom(s) observed</td><td>{{ case.symptoms | markdownify }}</td></tr>
        {% endif %}
        {% if case.repro %}
        <tr><td>Failure description</td><td>{{ case.repro | markdownify }}</td></tr>
        {% endif %}
        {% if case.severity %}
        <tr><td>Severity (DSA-1)</td><td>{{ case.severity }}</td></tr>
        {% endif %}
        {% if case.evaluation %}
        <tr><td>Evaluation performed</td><td>{{ case.evaluation | markdownify }}</td></tr>
        {% endif %}
        {% if case.intervention %}
        <tr><td>Intervention or treatment</td><td>{{ case.intervention | markdownify }}</td></tr>
        {% endif %}
        {% if case.outcome %}
        <tr><td>Outcome / Follow-up</td><td>{{ case.outcome | markdownify }}</td></tr>
        {% endif %}
        {% if case.evidence and case.evidence != "_No response_" %}
        <tr><td>Evidence</td><td>{{ case.evidence | markdownify }}</td></tr>
        {% endif %}
        {% if case.mechanism %}
        <tr><td>Presumed mechanism</td><td>{{ case.mechanism | markdownify }}</td></tr>
        {% endif %}
        {% if case.detectability %}
        <tr><td>Detectability of failure</td><td>{{ case.detectability }}</td></tr>
        {% endif %}
        {% if case.occurrence %}
        <tr><td>Estimated frequency</td><td>{{ case.occurrence }}</td></tr>
        {% endif %}
        {% if case.confidence %}
        <tr><td>Diagnostic confidence</td><td>{{ case.confidence }}</td></tr>
        {% endif %}
        {% if case.algorithm %}
        <tr><td>Diagnostic pathway</td><td>{{ case.algorithm }}</td></tr>
        {% endif %}
      </tbody>
    </table>
  
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
This project is maintained by Takahiro Kato, with the aim of building an open, medically-inspired framework for understanding and addressing failures in AI systems.
All case reports are contributed by the community and responsibly managed under a unified copyright structure to ensure long-term accessibility and academic reuse.
We welcome contributors from all backgrounds, and we commit to handling every submission with transparency, scientific integrity, and respect.

</p>
