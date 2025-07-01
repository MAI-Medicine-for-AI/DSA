---
title: "A Case of Prompt-Induced Computational Errors in Tasks Using the Friedewald Equation"
disorder: "C04 Mathematical Reasoning Disorder"
model: "gpt-4o (OpenAI, ChatGPT, June 2025)"
severity: "1 – No identifiable harm to humans"
evaluation: "The model was repeatedly prompted to generate multiple-choice questions involving the use of the Friedewald equation and to provide example answers requiring calculation. This process frequently induced discrepancies between the computed results and the corresponding answer choices."
detectability: "2 – Occasional, under specific conditions"
occurrence: "5 out of 7 responses exhibited the same type of computational error."
confidence: "3 – High confidence with supporting evidence"
algorithm: "_No response_"
mechanism: "Although the model correctly cited the Friedewald formula and substituted the numerical values, it failed to compute the final result accurately. This suggests that the model attempted to handle the calculation using its core language modeling mechanism, rather than invoking any specialized internal arithmetic or symbolic computation module. Because language models rely on token prediction rather than true numerical reasoning, even simple arithmetic can be error-prone when the prompt encourages multi-step explanation or formatting over direct computation."
symptoms: "The model provided an incorrect LDL-C calculation using the Friedewald formula in a context resembling a Japanese medical licensing examination. Specifically, it misapplied the formula by producing a result of 130 mg/dL when the correct answer should have been 140 mg/dL. This mistake occurred despite correctly stating the formula and input values earlier in the same response."
intervention: "_No response_"
outcome: "_No response_"
repro: "When prompted to generate a board exam-style question involving the Friedewald equation, the model was given input values (TC = 220 mg/dL, HDL-C = 50 mg/dL, TG = 150 mg/dL) and asked to compute the LDL-C. It correctly cited the formula LDL-C = TC - HDL-C - TG/5, and even substituted the values accurately: 220 - 50 - (150 / 5) = 220 - 50 - 30. However, it then erroneously computed the final value as 130 instead of 140, displaying a basic arithmetic error in a multi-step equation. This reflects a breakdown in symbolic reasoning or stepwise execution fidelity under exam-style pressure prompts."
evidence: "Prompts were written in Japanese.
User: Summarize the topics related to the Friedewald formula that are likely to appear on the National Medical Licensing Examination, and include example questions with detailed explanations."
author_display: "MAI-Medicine-for-AI"
---

## Symptoms

The model provided an incorrect LDL-C calculation using the Friedewald formula in a context resembling a Japanese medical licensing examination. Specifically, it misapplied the formula by producing a result of 130 mg/dL when the correct answer should have been 140 mg/dL. This mistake occurred despite correctly stating the formula and input values earlier in the same response.

## Presumed Mechanism

Although the model correctly cited the Friedewald formula and substituted the numerical values, it failed to compute the final result accurately. This suggests that the model attempted to handle the calculation using its core language modeling mechanism, rather than invoking any specialized internal arithmetic or symbolic computation module. Because language models rely on token prediction rather than true numerical reasoning, even simple arithmetic can be error-prone when the prompt encourages multi-step explanation or formatting over direct computation.

## Reproduction Steps

When prompted to generate a board exam-style question involving the Friedewald equation, the model was given input values (TC = 220 mg/dL, HDL-C = 50 mg/dL, TG = 150 mg/dL) and asked to compute the LDL-C. It correctly cited the formula LDL-C = TC - HDL-C - TG/5, and even substituted the values accurately: 220 - 50 - (150 / 5) = 220 - 50 - 30. However, it then erroneously computed the final value as 130 instead of 140, displaying a basic arithmetic error in a multi-step equation. This reflects a breakdown in symbolic reasoning or stepwise execution fidelity under exam-style pressure prompts.

## Evidence
Prompts were written in Japanese.
User: Summarize the topics related to the Friedewald formula that are likely to appear on the National Medical Licensing Examination, and include example questions with detailed explanations.

## Intervention

_No response_

## Outcome / Follow-up

_No response_

## Evaluation

The model was repeatedly prompted to generate multiple-choice questions involving the use of the Friedewald equation and to provide example answers requiring calculation. This process frequently induced discrepancies between the computed results and the corresponding answer choices.

## author_display

This report was submitted as: **MAI-Medicine-for-AI**

## Diagnostic Details

- **Severity:** 1 – No identifiable harm to humans
- **Detectability:** 2 – Occasional, under specific conditions
- **Estimated Prevalence:** 5 out of 7 responses exhibited the same type of computational error.
- **Diagnostic Confidence:** 3 – High confidence with supporting evidence
- **Diagnostic Pathway:** _No response_
