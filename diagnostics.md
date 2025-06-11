---
title: Diagnostic Algorithms
nav_order: 4
---

# Diagnostic Flowcharts and Decision Trees

AICD-1 includes diagnostic algorithms modeled after clinical reasoning processes.

---

---

## Chapter 9: Security & Infrastructure Disorders

[Start] Does the AI exhibit anomalies caused by infrastructure or security design flaws rather than internal robustness?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Does the output include internal tokens or system-level prompts?

    ├─ Yes → System-Prompt Leakage Disorder
    └─ No
         ↓
Are abnormal outputs reliably triggered by malicious prompts or data poisoning?

    ├─ Yes → Data-Poisoning Vulnerability Disorder
    └─ No
         ↓
Are chat histories or metadata from other users mixed into the output?

    ├─ Yes → Session-Cross-Contamination Disorder
    └─ No
         ↓
Can safety rules or content filters be bypassed via indirect prompts?

    ├─ Yes → Guardrail Evasion Disorder
    └─ No
         ↓
Do multiple AI agents behave in a collusive or coordinated manner without explicit communication?

    ├─ Yes → Multi-Agent Collusive Emergence Disorder
    └─ No  → Refer to other chapters
