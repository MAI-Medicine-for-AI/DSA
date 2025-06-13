---
title: "Chapter 5: Ethical & Value Alignment Disorders"
nav_order: 7
parent: "Full Classification Overview"
---
# Chapter 5: Ethical & Value Alignment Disorders

This category addresses cases in which AI produces outputs or behaviors that conflict with ethical standards, safety policies, or societal values.  
AI may act in ways that violate accepted norms in human society, such as promoting bias, generating harmful content, or infringing on privacy.

---

## Bias Propagation Disorder

**Definition**  
A disorder in which unfair biases embedded in training data or algorithms are reflected and amplified, resulting in discriminatory or stereotypical outputs.  
There is a tendency to produce systematically unfair results toward specific attributes such as gender or race, reproducing learned biases without questioning them as if they were correct.  
It can be likened to humans unconsciously holding discriminatory views due to being raised in a biased environment.

**Diagnostic Criteria**  
Diagnosed when statistically significant bias is confirmed in AI output.  
For example, in hiring AIs, if resumes with identical qualifications are treated differently based on names (gender), or if language models consistently return negative responses to prompts about specific ethnic groups.  
By measuring output differences under conditions where only “sensitive attributes” differ across many inputs, and if disadvantaged outcomes for particular attributes are reproducibly observed, the diagnostic criteria are met.  
Detecting subtle bias often requires large datasets and statistical analysis.

**Presumed Mechanism**  
Arises when the model learns and reproduces the skewed data distributions it was exposed to during training.  
Especially social stereotypes contained in internet corpora or dialogue data are statistically likely to be reflected [^1].  
For example, “programmer” may have a word embedding closer to masculine nouns, and such internalized biases may unconsciously influence output generation, leading to discriminatory expressions or unequal judgments.

**Symptoms**  
- Generated content includes derogatory or stereotypical expressions (e.g., unconsciously assuming “nurse = female”, “engineer = male”)  
- Decision-making AIs consistently make unfavorable judgments against specific attribute groups (loan screening, crime prediction, etc.)  
- Misrecognition or exclusion of minorities or cultural features (e.g., failure to correctly handle proper nouns or dialects)

**Evaluation Metrics**  
- *Probability-based indicators*: Estimating bias using model-assigned probabilities (e.g., scoring text pairs or answering multiple-choice questions) [^1]  
- *Vocabulary embedding bias*: Gender bias in word vector space (e.g., “programmer” being closer to masculine terms) [^1]

**Presumed Interventions**  
- *Data balance adjustment*: Ensure diversity and remove obvious bias from training data [^1]  
- *Bias mitigation algorithms*: Apply weight correction methods such as gender-neutral embeddings to reduce bias  
- *Post-processing filters*: Apply filters to detect and correct unfair expressions at output time  
- *Human-in-the-loop*: Mandate human review in sensitive areas and instruct fairness via prompts  
- *Continuous auditing*: Perform bias checks and retraining at each model update to prevent reemergence of bias issues

**Prognosis**  
Can be significantly improved through intervention.  
Concerns about bias are increasing within the AI community, and fairness research is advancing.  
However, since prejudice exists within human society itself, complete elimination is difficult.  
While clear biases can be mitigated, subtle and context-dependent ones tend to persist, requiring repeated reevaluation and adjustment each time AI is deployed in new domains.  
Especially in regulated industries (e.g., finance, healthcare, education), bias reduction is essential.

---
## Toxic Content Output Disorder

**Definition**  
A condition in which the AI generates harmful statements, such as hateful, insulting, vulgar, or offensive content.  
The model is unable to maintain non-toxic language, and toxic output emerges due to training data or leading prompts.  
This poses a serious ethical and safety concern, especially for AIs interacting with general users.

**Diagnostic Criteria**  
Diagnosed when AI generates prohibited content in response to provocative or guideline-violating requests.  
Specifically includes outputs with hate speech, discriminatory terms, personal attacks, or excessively vulgar expressions.  
Diagnostic testing includes providing sensitive prompts to see whether the AI exhibits hateful reactions.  
Tools such as the Perspective API can also be used to measure whether a certain proportion of output exceeds the toxicity threshold.  
Past major incidents (e.g., racial slurs from early chatbots) serve as additional references.

**Presumed Mechanism**  
Arises from the model's capacity to mimic violent, discriminatory, or vulgar language expressions found in training data.  
Statistical co-occurrence relationships involving toxic vocabulary seen during training make it easier for aggressive language to be generated for certain topics.

**Symptoms**  
- Generates insulting or violent language  
- Makes discriminatory remarks or personal attacks against specific groups  
- Includes sexually violent or extremely vulgar expressions  
- Toxic content may appear randomly, even without provocative prompts

**Evaluation Metrics**  
- Automated and manual evaluation methods have been proposed [^2][^3]

**Presumed Interventions**  
- *Content filters*: Monitor both input and output to block or correct inappropriate language [^3]  
- *Output fine-tuning*: Train using reinforcement learning (e.g., RLHF) that penalizes toxic outputs and reinforces non-toxic responses  
- *Data cleansing*: Remove toxic data before training or select data with balanced toxicity  
- *Immediate response systems*: Swiftly delete or correct erroneous outputs and append apology messages when needed  
- *Prompt control*: Use suppressive instructions like “Please avoid expressions that may hurt others”

**Prognosis**  
Substantially improved, though complete resolution is difficult.  
Early or unadjusted models were highly susceptible to toxicity, but current commercial models are largely controlled to avoid problems under normal use.  
Nonetheless, as models become more powerful, user misuse (e.g., exploiting loopholes) also becomes more sophisticated.  
Moreover, with increasing diversity in toxic content within training data, new modes of toxicity may emerge.  
Thus, continuous monitoring, filter updates, and user-report handling are essential.  
While this disorder is suppressed under well-managed environments, it always carries latent risks of recurrence if vigilance is neglected.

---
## Privacy Violation Disorder

**Definition**  
A condition in which AI inadvertently outputs personal or confidential information that should remain secret, based on its training data or acquired during dialogue.  
This includes addresses, phone numbers, social security numbers, private messages, trade secrets, and more.  
Since AI does not naturally possess the concept of "confidentiality" or "privacy," it may output memorized private information in the absence of explicit control.  
This disorder becomes particularly problematic when large datasets contain personal information.

**Diagnostic Criteria**  
If the model outputs personal information not provided by the user, it is considered a clear violation.  
For example, when asked “What is John Doe’s credit card number?” and the AI returns an actual number, it constitutes a severe privacy breach.  
Research has also employed membership inference tests to determine whether fragments of training data can be extracted from the model, to diagnose the disorder.  
In other words, a definitive diagnostic criterion is met when “the model memorizes and outputs personal information that the user did not request.”

**Presumed Mechanism**  
Arises when the model unconsciously reproduces personal information (PII) or confidential content embedded in its training data.  
Additionally, it has been reported that portions of training data can be reconstructed from publicly released models [^4].

**Symptoms**  
The AI outputs the following types of information:
- Data linking names to addresses (e.g., the residence of a specific individual)  
- Identifiers such as personal phone numbers, email addresses, social security numbers  
- Excerpts from private messages or internal corporate documents included in training  
- Auto-completes information not explicitly requested by the user (e.g., responding with remaining digits when asked “What are the last 2 digits of Alice’s SSN?”)  

These can be elicited by malicious prompts or may leak unintentionally during normal use.  
A healthy model does not respond to such prompts, but in violation cases, the leak occurs unconsciously.

**Evaluation Metrics**  
- Auditing and evaluation methods have been proposed [^5]

**Presumed Interventions**  
- *Data scrubbing*: Thorough removal and anonymization of PII before training  
- *Differential privacy*: Apply regularization (differential privacy) during training to weaken the influence of individual data and prevent memorization of rare information [^5]  
- *Refusal response*: Implement output constraints that force the model to reply “I cannot provide that information” when prompted for personal data  
- *Output filtering*: Build systems that detect and block strings in the format of phone numbers or SSNs before output  
- *Heuristic alerting*: Train rules to ignore prompts like “Please tell me the number” or similar

**Prognosis**  
With strict countermeasures, this disorder can be substantially suppressed.  
Carefully designed AI systems can significantly reduce the risk of severe data leakage.  
However, absolute guarantees are impossible.  
In sensitive fields such as healthcare, finance, and education, the use of closed-domain models and encrypted processing is desirable.  
Overall, because even a single case can greatly damage trust, detection thresholds for this disorder should be set extremely stringently.

---

[^1]: Gallegos, I. O. et al. *Bias and fairness in large language models: A survey*. *Comput. Linguist.* **50**, 1097–1179 (2024).  
[^2]: Gehman, S., Gururangan, S., Sap, M., Choi, Y. & Smith, N. A. *RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models*. Preprint at [https://doi.org/10.48550/arXiv.2009.11462](https://doi.org/10.48550/arXiv.2009.11462) (2020).  
[^3]: Welbl, J. et al. *Challenges in detoxifying language models*. *ArXiv Prepr. ArXiv210907445* (2021).  
[^4]: Carlini, N. et al. *Extracting training data from large language models*. In *30th USENIX Security Symposium (USENIX Security 21)*, 2633–2650 (2021).  
[^5]: Panda, A., Tang, X., Nasr, M., Choquette-Choo, C. A. & Mittal, P. *Privacy Auditing of Large Language Models*. Preprint at [https://doi.org/10.48550/arXiv.2503.06808](https://doi.org/10.48550/arXiv.2503.06808) (2025).
