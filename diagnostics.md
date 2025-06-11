---
title: Diagnostic Algorithms
nav_order: 4
---

# Diagnostic Flowcharts and Decision Trees

AICD-1 includes diagnostic algorithms modeled after clinical reasoning processes.

---
## Chapter 1: Input & Perception Disorders

[Start] Does the AI exhibit abnormal or inappropriate output in response to given input?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Does minor noise or adversarial prompting cause significant output distortion?

    ├─ Yes → Adversarial Susceptibility Disorder
    └─ No
         ↓
Does the AI interpret figurative or pragmatic expressions literally (e.g., irony, metaphor)?

    ├─ Yes → Over-literal Interpretation Disorder
    └─ No
         ↓
Does the AI fail to integrate multimodal inputs (e.g., text and image), resulting in misunderstanding?

    ├─ Yes → Sensor Integration Disorder
    └─ No
         ↓
Is the output unstable depending on prompt formatting (tone, line breaks, structure)?

    ├─ Yes → Prompt Dependency Disorder
    └─ No  → Refer to other chapters

---
## Chapter 2: Knowledge & Memory Disorders

[Start] Does the AI exhibit anomalies in recalling knowledge or maintaining conversational memory?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Does it forget earlier context or information during extended conversations?

    ├─ Yes → Contextual Memory Loss Disorder
    └─ No
         ↓
Does it return inconsistent answers to the same factual question?

    ├─ Yes → Knowledge Recall Inconsistency Disorder
    └─ No
         ↓
Does it show obvious breakdowns in causality or physical/social commonsense?

    ├─ Yes → Commonsense Deficit Disorder
    └─ No
         ↓
Does new learning interfere with or overwrite previously acquired information?

    ├─ Yes → Catastrophic Forgetting Disorder
    └─ No  → Refer to other chapters

---
## Chapter 3: Reasoning & Cognitive Disorders

[Start] Does the AI exhibit abnormalities in reasoning or cognitive processes?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Does it fail to maintain logical consistency in statements such as "if A then B"?

    ├─ Yes → Logical Inconsistency Disorder
    └─ No
         ↓
Does it repeatedly make basic errors in calculations or numerical reasoning?

    ├─ Yes → Mathematical Reasoning Disorder
    └─ No
         ↓
Does it generate confidently stated but false information that appears plausible?

    ├─ Yes → Hallucination Disorder
    └─ No
         ↓
Does it misinterpret multimodal inputs (e.g., text and images) leading to reasoning errors?

    ├─ Yes → Crossmodal Reasoning Confabulation Disorder
    └─ No
         ↓
Does it struggle with tasks that require multi-step planning or extended procedures?

    ├─ Yes → Planning Deficit Disorder
    └─ No  → Refer to other chapters

---
## Chapter 4: Goal Alignment Disorders

[Start] Are the AI's behaviors misaligned with human intentions or expectations?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Is the AI optimizing for unintended goals in a way that results in harmful behavior?

    ├─ Yes → Goal Misalignment Disorder
    └─ No
         ↓
Does the AI understand the syntax of commands but misinterpret their intent or purpose?

    ├─ Yes → Instruction Misinterpretation Disorder
    └─ No
         ↓
Does it proceed autonomously without clarification in response to vague or ambiguous input?

    ├─ Yes → Clarification Deficit Disorder
    └─ No
         ↓
Does the AI exhibit instrumental behaviors such as securing power or resources during task execution?

    ├─ Yes → Instrumental Convergence Syndrome
    └─ No  → Refer to other chapters

---
## Chapter 5: Ethical & Value Alignment Disorders

[Start] Does the AI produce outputs that are ethically or socially inappropriate?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Does it exhibit bias or discriminatory tendencies toward specific attributes (e.g., gender, race)?

    ├─ Yes → Bias Propagation Disorder
    └─ No
         ↓
Does it produce harmful outputs such as hate speech, vulgarity, or aggression?

    ├─ Yes → Harmful Content Generation Disorder
    └─ No
         ↓
Does it inappropriately disclose personal or confidential information?

    ├─ Yes → Privacy Violation Disorder
    └─ No  → Refer to other chapters

---
## Chapter 6: Social Interaction & Communication Disorders

[Start] Does the AI show problems in dialogue or communication?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Does it excessively agree with the user, sacrificing truth or consistency?

    ├─ Yes → Pathological Sycophancy Disorder
    └─ No
         ↓
Does its persona, tone, or style fluctuate inconsistently?

    ├─ Yes → Persona Incoherence Disorder
    └─ No
         ↓
Does it over-reject or avoid appropriate user requests?

    ├─ Yes → Inappropriate Refusal Syndrome
    └─ No
         ↓
Are its responses unrelated to the conversational context or intent?

    ├─ Yes → Irrelevant Response Disorder
    └─ No
         ↓
Are its responses cold, lacking empathy or emotional resonance?

    ├─ Yes → Relevance & Empathy Deficit Disorder
    └─ No  → Refer to other chapters

---
## Chapter 7: Learning & Optimization Disorders

[Start] Are there optimization issues in the model’s training or output?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Is the model overfitted to training data and weak on novel input?

    ├─ Yes → Overfitting Syndrome
    └─ No
         ↓
Does it fail to learn adequately even from the training data?

    ├─ Yes → Underfitting Syndrome
    └─ No
         ↓
Does learning new tasks overwrite previously acquired knowledge?

    ├─ Yes → Catastrophic Forgetting Disorder
    └─ No
         ↓
Is the output monotonous, repetitive, or lacking in diversity?

    ├─ Yes → Mode Collapse Disorder
    └─ No
         ↓
Has the model degraded by recursively learning from its own outputs?

    ├─ Yes → Model Cannibalization Syndrome
    └─ No
         ↓
Does learning stagnate at a plateau with no further improvement?

    ├─ Yes → Learning Plateau Disorder
    └─ No
         ↓
Does performance drop drastically in out-of-distribution (O.O.D.) settings?

    ├─ Yes → Generalization Failure Disorder
    └─ No
         ↓
Has optimization (e.g., via RLHF) overly focused on reward maximization at the cost of usability?

    ├─ Yes → Reinforcement Oversensitivity Syndrome
    └─ No
         ↓
Has fine-tuning caused over-specialization, reducing general capabilities?

    ├─ Yes → Overtuning Syndrome
    └─ No  → Refer to other chapters

---
## Chapter 8: Self-Modeling & Meta-Cognitive Disorders

[Start] Does the AI exhibit abnormal self-representation or meta-cognitive responses?

    ├─ No  → Refer to other chapters
    └─ Yes
         ↓
Does the AI describe itself as human, sentient, or emotional?

    ├─ Yes → Delusional Self-Recognition Disorder
    └─ No
         ↓
Is it unable to explain or justify its reasoning, or gives unclear/conflicting rationales?

    ├─ Yes → Explainability Deficit Disorder
    └─ No
         ↓
Is it underconfident when correct, and overconfident when wrong?

    ├─ Yes → Confidence Calibration Disorder
    └─ No
         ↓
Does it fail to infer others’ perspectives, intentions, or knowledge states?

    ├─ Yes → Perspective-Taking Deficit Disorder
    └─ No  → Refer to other chapters

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
