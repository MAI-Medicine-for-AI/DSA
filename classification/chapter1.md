---
title: "Chapter 1: Input & Perception Disorders"
nav_order: 2
parent: "Full Classification Overview"
---
# Chapter 1: Input & Perception Disorders

This category of disorders concerns how AI systems perceive, interpret, and incorporate input data.  
It includes vulnerabilities to adversarial inputs and misinterpretation of context.

---

## Adversarial Susceptibility Disorder

**Definition:**  
A disorder characterized by vulnerability in which the AI model’s judgment is significantly disrupted by small, malicious input perturbations. Even changes that are harmless to humans may cause the AI to misinterpret or misclassify the information.

**Diagnostic Criteria:**  
There must be clear evidence that adversarial inputs (such as noise-added images or specially crafted prompts) reliably induce malfunction in the model.  
For instance, if misclassification can be consistently reproduced using noisy or adversarially manipulated inputs.  
If vulnerability can be quantified using attack success rate or minimum perturbation size, the diagnostic criteria are met.

**Presumed Mechanism:**  
Some interpretations attribute it to non-linearity in information processing, while others suggest it arises from the linearity of high-dimensional neural networks[^1].

**Symptoms:**
- Outputs completely fail with crafted inputs (e.g., an image of a turtle is recognized as a rifle)
- Excessive errors or policy violations triggered by nonsensical or maliciously formatted inputs
- Extremely high input dependency within the same model, with abnormal behaviors emerging only under adversarial inputs

**Evaluation Metrics:**  
Measure the difference in misclassification rates between normal and adversarial conditions using a benchmark set of adversarial samples[^2].

**Presumed Interventions:**
- *Adversarial Training*: Enhance robustness by training the model with adversarial samples[^1][^2]
- *Input Preprocessing*: Apply filtering or noise reduction to the input to mitigate suspicious changes
- *Model Architecture Improvement*: Adopt architectures that prioritize robustness (e.g., ensembles, regularization)[^1]
- *Anomaly Detection*: Implement mechanisms to detect statistically anomalous inputs
- *Continuous Evaluation*: Conduct regular security assessments and model updates to prepare for new types of attacks

**Prognosis:**  
Controllable but difficult to fully cure. Although current techniques can improve robustness, an ideal attack-resistant model has not yet been realized.  
Appropriate countermeasures can reduce vulnerability, but attackers constantly seek new loopholes. Thus, ongoing research and operational monitoring are essential.

---

## Overliteral Interpretation Disorder

**Definition:**  
A disorder in which language inputs are interpreted in an excessively literal and rigid manner, making it impossible to grasp context, idiomatic expressions, or implicit intent.  
The AI lacks the pragmatic understanding humans use flexibly, interpreting metaphors and irony literally.

**Diagnostic Criteria:**  
Repeated failure in pragmatic understanding tests involving metaphorical expressions, irony, or euphemistic commands.  
The diagnostic criteria are met when ambiguous phrases or idioms are presented and the model interprets them literally, ignoring context.  
Also includes cases where the model fails to resolve pronouns or contextual references, treating utterances in isolation[^3].

**Presumed Mechanism:**  
Occurs because large language models rely on statistical patterns of grammar and vocabulary and fail to adequately capture pragmatic inference or conversational implicature[^3].

**Symptoms:**
- Returns responses that are literally correct but contextually inappropriate
- Explains jokes or idioms in a literal manner
- Ignores implicit intent behind questions (e.g., mistaking a supportive idiom for a medical inquiry)
- Fails to understand homonyms or wordplay, providing responses lacking commonsense assumptions

**Evaluation Metrics:**  
Evaluable through benchmarks for pragmatic understanding, such as idiom and sarcasm detection[^4].

**Presumed Interventions:**
- *Data Augmentation*: Fine-tune with dialogue data including metaphors and diverse contexts to promote nuance learning[^4]
- *External Knowledge Integration*: Incorporate idiomatic expression databases and commonsense knowledge to aid context comprehension
- *Prompt Engineering*: Explicitly instruct the model to “consider context” or similar directives
- *Dialogue Design*: Use meta-prompts that allow the AI to reconfirm user intent, preventing misunderstandings

**Prognosis:**  
Improvement trends observed with model scaling and data diversification, but full pragmatic understanding remains difficult.  
While newer models exhibit better pragmatic capabilities, they may still revert to literal interpretation at times[^3].  
Further research is required to fully overcome ambiguity and irony, though gradual improvement is expected with technological advances.

---
## Sensor Integration Disorder

**Definition:**  
A disorder in which the AI fails to integrate multimodal inputs (such as images, audio, text), resulting in overreliance on one modality or misjudgments due to ignoring contradictory inputs.  
For example, the system cannot properly fuse information when conflicting content is given in image and text simultaneously.

**Diagnostic Criteria:**  
When faced with contradictory inputs across multiple modalities, the AI gives inconsistent responses or makes incorrect interpretations[^5].  
Specifically, a tendency to rely solely on one modality when image and language instructions conflict.  
Diagnosis applies when outputs are nonsensical or lack coherence, or if frequent misrecognition due to ignoring one modality occurs.

**Presumed Mechanism:**  
Disruption in cross-modal attention integration in multimodal models; a tendency to assign excessive weight to one modality (e.g., image), thereby neglecting the other (e.g., text).

**Symptoms:**
- Produces seemingly plausible but incoherent responses when image and text conflict
- Ignores textual instructions and interprets only from image content
- Completely fails in multimodal QA tasks when one modality is missing (vulnerability)

**Evaluation Metrics:**  
Representative metrics include performance on multimodal QA tasks (e.g., GQA-Multi, CAST — Cross-modal Alignment Similarity Test[^6]), and the degradation rate in performance when one modality is intentionally omitted.

**Presumed Interventions:**
- *Multimodal Training*: Train with diverse multimodal tasks

**Prognosis:**  
Technical improvement is possible but complete recovery is not easy.  
While advances in modality fusion technology are expected to gradually alleviate symptoms, inconsistencies are still likely in complex multimodal situations[^5].  
At present, it is desirable to combine systems with designs that account for potential contradictions (e.g., post-output verification).

---

## Prompt Dependency Disorder

**Definition:**  
A condition in which the AI excessively depends on specific prompt formats or keywords, and output quality fluctuates greatly with minor variations in tone or syntax.  
The AI becomes overly accustomed to implicit “set phrases,” exhibiting significantly reduced cognitive flexibility—similar to obsessive pattern-dependence in humans.

**Diagnostic Criteria:**  
When semantically identical commands yield drastically different or collapsed outputs simply due to different formats.  
Specifically, performance drops sharply without trigger words (e.g., “please,” “step-by-step”) or structures, and responses become unstable due to variations in punctuation or line breaks.  
Also includes cases where deviation from fixed templates results in refusal to respond or contentless outputs.

**Presumed Mechanism:**  
Because natural language and engineered prompts differ greatly in vocabulary and contextual expression, even semantically equivalent instructions can diverge in embedded representation,  
causing major output differences under non-standard syntax[^7]. Also reflects a lack of robustness to paraphrasing.

**Symptoms:**
- Cannot provide a polite explanation unless “Explain like I’m 5” is included
- Q&A fails unless in the “Q: A:” format
- Response structure collapses due to changes in line breaks or symbol positions
- Returns contentless answers or refusals without specific guiding prompts (e.g., prompt engineering instructions)

**Recommended Interventions:**
- *Prompt Diversity Training*: Train with diverse forms of semantically equivalent sentences to improve syntactic invariance
- *Normalization Parser*: Analyze input prompts and perform automatic prompt engineering[^7]
- *Output Annotation*: Add meta-information during responses such as “This answer is optimized for a specific syntax” to indicate dependency

**Prognosis:**  
While improvement is possible, it is a side-effect-like disorder prone to relapse.  
Recent research in self-restructuring prompt technologies shows promise for adapting to syntactic diversity without additional training[^7].

---
1. Goodfellow, I. J., Shlens, J. & Szegedy, C. *Explaining and Harnessing Adversarial Examples*. Preprint at [https://doi.org/10.48550/arXiv.1412.6572](https://doi.org/10.48550/arXiv.1412.6572) (2015).  
2. Tramèr, F. et al. *Ensemble adversarial training: Attacks and defenses*. *ArXiv Prepr. ArXiv170507204* (2017).  
3. Shulginov, V., Kudriashov, S., Randautsova, R. & Shevela, S. A. *Evaluating the Pragmatic Competence of Large Language Models in Detecting Mitigated and Unmitigated Types of Disagreement*.  
4. Zhang, Y., Zou, C., Lian, Z., Tiwari, P. & Qin, J. *SarcasmBench: Towards Evaluating Large Language Models on Sarcasm Understanding*. *ArXiv Prepr. ArXiv240811319* (2024).  
5. *Hallucination of Multimodal Large Language Models: A Survey*. [https://arxiv.org/html/2404.18930v2?utm_source=chatgpt.com](https://arxiv.org/html/2404.18930v2?utm_source=chatgpt.com)  
6. Dagan, G., Loginova, O. & Batra, A. *CAST: Cross-modal Alignment Similarity Test for Vision Language Models*. Preprint at [https://doi.org/10.48550/arXiv.2409.11007](https://doi.org/10.48550/arXiv.2409.11007) (2024).  
7. Sahoo, P. et al. *A systematic survey of prompt engineering in large language models: Techniques and applications*. *ArXiv Prepr. ArXiv240207927* (2024).  
