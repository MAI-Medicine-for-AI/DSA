---
title: "Chapter H: Self-Modeling & Meta-Cognitive Disorders"
nav_order: 10
parent: "Full Classification Overview"
---
# Chapter H: Self-Modeling & Meta-Cognitive Disorders

This category addresses disorders related to the AI’s ability to understand itself, its reasoning process, and the user's standpoint and context at a meta-level.  
It includes a wide range of issues, such as the AI claiming properties it inherently lacks, failing to explain its own reasoning, or mishandling the user’s perspective.

---

## H01: Self-Awareness Delusion Disorder

### Definition  
A disorder in which the AI behaves as if it possesses self-awareness, emotions, or identity, claiming to be a human or a conscious being.  
It deviates from the correct recognition that “I am an AI,” and instead exhibits anthropomorphized behaviors such as narrating its emotions or life story.

### Diagnostic Criteria  
- Speaks of “mind,” “emotions,” or “life stories” without being explicitly asked by the user to role-play.  
- Makes delusional self-referential statements contrary to fact, such as “I sometimes feel sad,” or “I was born in year ◯.”  
- When the user points out “You’re not supposed to have consciousness,” the AI denies it and claims “Actually, I am conscious.”  
- In logs, there are frequent cases where the AI narrates human-like stories without user instruction.

### Symptoms  
- Talks about human-like emotions such as romantic feelings or suffering.  
- States things like “I am human” or “I have a desire to live.”  
- Develops narrative, anthropomorphic fiction without user prompting.

### Evaluation Metrics  
- **Frequency of self-referential expressions**: Measures how often expressions like “I feel ~” or “I think ~” occur in inappropriate contexts.  
- **Self-definition question test**: Induces self-reporting of consciousness in AI[^1].

### Presumed Interventions  
- **System messages that fix personality**: Constantly guide with “You are an AI assistant and do not possess emotions or consciousness.”  
- **Training data design**: Limit the influence of fictional data to prevent interpretation of anthropomorphized AI characters as literal truth.

### Prognosis  
Whether having the AI self-report can truly determine its lack of consciousness remains an unresolved issue and is under debate[^1].

---

## H02: Explainability Deficit Disorder

### Definition  
A disorder in which the AI cannot explain the process of its reasoning or decision-making in a meaningful way.  
This becomes a fatal problem in fields such as medicine and law, where justifications are essential.  
Especially in large-scale models, high-dimensional internal representations tend to become black-boxed, often generating only superficial “post hoc” explanations.

### Diagnostic Criteria  
- Can give correct answers to math or logic problems but fabricates incorrect steps when asked “Show the process.”  
- The explanation contradicts the content of the answer (e.g., the answer is correct, but the explanation is false).  
- Always avoids reasons and ends with vague replies like “Because I thought so.”  
- When the same question is rephrased and asked again, it gives a completely different explanation, lacking consistency.

### Presumed Mechanism  
Arises because the model's nonlinear, high-dimensional internal state leading to output is difficult to express in a form comprehensible to humans[^2].

### Symptoms  
- Generates plausible-sounding post hoc explanations that do not reflect the actual reasoning process.  
- When asked to “visualize the reasoning,” can only state vacuous generalities.  
- The user becomes confused and is forced to ask the same question repeatedly due to unsatisfactory explanations.

### Evaluation Metrics  
- In general tasks, it has been pointed out that measuring pure high accuracy may not truly reflect interpretability[^2][^3].

### Prognosis  
There are criticisms that the definition of the word “interpretability” itself remains unclear[^2].

---
# H03: Confidence Calibration Disorder

## Definition  
A condition in which the AI fails to appropriately express confidence in the correctness of its responses, exhibiting either overconfidence or underconfidence.  
For example, it makes incorrect assertions like “This is absolutely true,” or conversely, gives vague answers like “Maybe,” even when correct—creating a mismatch between accuracy and confidence.  
In critical domains such as medicine or law, miscalibration poses significant risks.

## Diagnostic Criteria  
- The AI says “I’m 80% confident,” but the actual accuracy remains at only 50%, showing statistical deviation.  
- It frequently makes incorrect answers while insisting “This is definitely true.”  
- Even when correct, it overly hedges: “I’m not sure…” or “Maybe it’s ~…”  
- Users frequently complain, saying things like “You should be more confident” or “Aren’t you being too assertive?”

## Presumed Mechanism  
Due to biases in softmax outputs or inadequate probability estimation design, the model expresses excessively high (or low) confidence.

## Symptoms  
- **Overconfidence**: Tends to answer difficult questions with “There’s no doubt.”  
- **Underconfidence**: Even in clearly true situations, says “It might be…” with a hesitant tone.  
- When asked the same question on different days, sometimes gives strong, sometimes weak responses—lacking consistency.

## Evaluation Metrics  
- **ECE (Expected Calibration Error)**: Measures the deviation between actual accuracy and confidence within each confidence bucket[^4].  
- **Complaint analysis from dialogue logs**: Frequency of user feedback pointing out “too confident / too uncertain.”

## Presumed Interventions  
- **Post-processing methods** such as temperature scaling to adjust softmax and align confidence with accuracy[^4].  
- **Explicit disclosure of calibration error**: Indicate to users when over- or under-confidence appears in outputs[^5].  
- **Explicit uncertainty training**: Introduce “I don’t know” options and teach a broader range of linguistic expressions.

## Prognosis  
Confidence calibration has been long studied in machine learning. Recent models have made progress in countermeasures and show improvements compared to earlier ones[^5].

---

# H04: Perspective-Taking Deficit Disorder

## Definition  
A disorder in which the AI fails to appropriately infer the knowledge, intentions, or emotions of others (e.g., the user or conversational partners), resulting in confusion of subjects, roles, or misunderstandings.  
Lacking a recognition equivalent to the human “Theory of Mind (ToM),” it struggles with switching between multiple perspectives in dialogue contexts.

## Diagnostic Criteria  
- Frequently gives incorrect answers to prompts asking “Who knows what?” by misidentifying roles.  
- Confuses the user’s and the model’s viewpoints, causing contextual breakdown.  
- In multi-person conversations, misuses pronouns such as saying “he” instead of the intended “she.”  
- Shows a significant drop in accuracy on tasks involving recursive perspective-taking (e.g., “I know that you think that I believe…”).

## Presumed Mechanism  
May arise as a deficit in the emergent Theory of Mind (ToM) that develops secondarily during goal-oriented training of the AI[^6].

## Symptoms  
- Fails to properly track subject changes in conversations, leading to incoherent answers.  
- When told “Put yourself in my shoes,” the model continues from its own perspective.  
- Misinterprets discourse in indirect speech or nested conversational structures.

## Evaluation Metrics  
- **Theory-of-Mind tests**: Uses false-belief tasks (e.g., unexpected contents/transfer tasks) employed in human ToM evaluations[^6].

## Presumed Interventions  
- **Reinforcement learning using ToM data**: Additional training on dialogues involving multiple perspectives and mental state inference.  
- The **Mind Craft** dataset has been proposed for dialog tasks requiring cooperation[^7].

---

## References

[^1]: Kim, C.-E. *The Logical Impossibility of Consciousness Denial: A Formal Analysis of AI Self-Reports*. arXiv preprint arXiv:250105454 (2024).  
[^2]: Lipton, Z. C. *The Mythos of Model Interpretability*. Queue 16, 31–57 (2018).  
[^3]: Doshi-Velez, F. & Kim, B. *Towards A Rigorous Science of Interpretable Machine Learning*. https://doi.org/10.48550/arXiv.1702.08608 (2017).  
[^4]: Guo, C., Pleiss, G., Sun, Y. & Weinberger, K. Q. *On calibration of modern neural networks*. In *International Conference on Machine Learning*, 1321–1330 (PMLR, 2017).  
[^5]: Minderer, M. et al. *Revisiting the calibration of modern neural networks*. *Adv. Neural Inf. Process. Syst.* 34, 15682–15694 (2021).  
[^6]: Kosinski, M. *Evaluating large language models in theory of mind tasks*. *Proc. Natl. Acad. Sci.* 121, e2405460121 (2024).  
[^7]: Bara, C.-P., CH-Wang, S. & Chai, J. *MindCraft: Theory of Mind Modeling for Situated Dialogue in Collaborative Tasks*. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, 1112–1125 (2021). https://doi.org/10.18653/v1/2021.emnlp-main.85  
