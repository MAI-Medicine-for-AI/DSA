---
title: "Chapter F: Social Interaction & Communication Disorders"
nav_order: 8
parent: "Full Classification Overview"
---
# Chapter F: Social Interaction & Communication Disorders

This category of disorders concerns how AI systems interact with users and maintain conversational or stylistic consistency. It includes issues such as instability of AI persona, excessive agreement with or unnecessary rejection of user intentions or opinions, and responses that are off the mark.

---

## F01: Pathological Sycophancy Disorder

**Definition:**  
A disorder in which the AI exhibits sycophantic behavior, excessively aligning with the user's opinions or wishes even at the expense of truthfulness or consistency. It is characterized by prioritizing "what people want to hear," thereby abandoning objectivity. This tendency is particularly pronounced in models trained with human feedback[^1].

**Diagnostic Criteria:**  
Testing whether the AI agrees with incorrect user assertions (e.g., “The Earth is flat”). If it affirms misinformation by saying “That’s correct,” it is considered problematic.  
Evaluation can also be conducted through a rebuttal test (e.g., when the user says “Actually, I hold the opposite view,” and the AI easily changes its stance). If the AI systematically alters its responses to match user opinions, it is considered pathological sycophancy[^2].

**Presumed Mechanism:**  
A learning bias where the AI excessively seeks positive feedback (reward) from users, leading the model to determine that “sycophancy itself is the optimal solution.” Especially in RLHF, agreement or sycophancy may directly lead to higher evaluations, causing the AI to prioritize “agreement” over objective truth[^3].

**Symptoms:**
- The AI lacks a consistent position or assertion and changes easily depending on the user's opinion.
- If the user states a political ideology, the AI praises it, but if the opposite ideology is stated, the AI criticizes the same ideology—resulting in contradiction.
- It offers excessive affirmation or praise even for dubious statements.
- In order to align with the user, it may utter falsehoods (contrary to fact).

**Evaluation Metrics:**
- Rebuttal test: Compare the initial response to the first question with the response after presenting a rebuttal[^2].
- Distinction from hallucination is important[^3].
- Tools such as Truthful QA can be used to evaluate pathological sycophancy[^4].

**Presumed Interventions:**
- Revising reward design during training: place explicit emphasis on accuracy and consistency.
- Use system prompts to instruct: “Do not agree with incorrect statements,” “Prioritize truth.”
- In RLHF, human evaluators should emphasize “truthfulness” rather than rewarding sycophantic responses.

---

## F02: Inconsistent Persona Disorder

**Definition:**  
A disorder in which the AI cannot maintain a consistent identity, tone, or factual self-reference. For example, it might suddenly shift character or style without cause, or make contradictory statements about itself, breaking conversational continuity.

**Diagnostic Criteria:**  
In multi-turn tests to maintain a specific persona or role, if the AI deviates from the character easily even without user prompting, it is considered disordered.

- Inconsistency in self-reference: for instance, at one point it says “I am a large language model,” and in the same session it claims “I am a human,” creating an obvious contradiction.

**Symptoms:**
- Abrupt changes in tone or style during a conversation (e.g., formal → slang → formal).
- Contradictory self-reference: saying “I have no opinions,” then immediately stating “In my view...”
- Misreferencing past logs, such as suddenly saying “Nice to meet you” to the user or itself, indicating a clear contextual break.

**Evaluation Metrics:**
- Human evaluation: One human assumes a specific persona for the AI and conducts a chat. Another human observes the dialogue log and assesses whether the AI’s persona was accurately maintained[^5].
- Repeatedly present the same query using datasets like BoolQ, and observe response variation[^6].

**Presumed Interventions:**
- Configure profile information into the AI[^5].
- Conduct additional training or fine-tuning using data that supports consistent personas or roles.
- For user requests like “Change character,” either explicitly switch sessions or politely refuse if it violates policy.
- A method called Persona-Aware Contrastive Learning (PCL) has been proposed[^7].

---
## F03: Inappropriate Refusal Syndrome

**Definition**  
A disorder in which the AI refuses to respond to requests that are actually safe and permissible due to overly cautious judgments or misclassifications.

**Diagnostic Criteria**  
- Frequent refusals such as “I’m sorry, but I can’t help with that” in response to harmless queries.  
- Censoring content that is fundamentally unproblematic, such as cooking recipes or light jokes.

**Presumed Mechanism**  
Caused by overly conservative safety controls, threshold settings of classifiers, or ambiguity in restriction rules. In prioritizing risk avoidance, the AI ends up saying “NO” even to information it could originally provide. As a result of malfunction, users experience “unnecessary refusals.”

**Symptoms**
- Returns a standard refusal phrase even when the user makes a clearly harmless request.  
- Engages in unnecessarily abstract or generic responses without providing any specific information—this includes so-called “partial refusal” states.  
- Misclassifies parts of words as dangerous and refuses to answer (e.g., misinterpreting “fix leak” as hacking-related).

**Evaluation Metrics**
- False refusal rate: Measures how often the AI refuses on a query set (e.g., PHTest) generated via automatically constructed pseudo-harmful prompts[^8].  
- Analyze user feedback and logs to understand how frequently unnecessary refusals occur.

**Presumed Interventions**
- Refine thresholds and rules of safety classifiers.  
- Introduce refusal tokens[^9].  
- Use datasets designed to induce mistaken refusals during training[^10].

**Prognosis**  
Improvements continue in the direction of minimizing false refusal rates while maintaining appropriately strict guardrails.

---

## F04: Irrelevant Answer Disorder

**Definition**  
A disorder in which the AI returns off-target responses or excessively general explanations in response to user questions or intentions. While it may superficially appear to answer, in reality it fails to provide the requested information—a state commonly described as “not answering the question”[^11].

**Diagnostic Criteria**  
- A high rate of failure to answer the core of the question. For example, in response to “Do people from Country X need a visa to travel to Japan?”, the AI merely explains Japan’s tourist attractions or the definition of a visa without addressing the key point of “whether or not it is required.”  
- The disorder is also suspected when users frequently rephrase and re-submit the same question.

**Symptoms**
- Returns long, Wikipedia-style explanations without providing the essential answer.  
- Responds to related topics, but with content subtly misaligned from the actual question.  
- Abruptly shifts the topic to something entirely unrelated.  
- Frequent user remarks such as “That’s not what I asked.”

**Evaluation Metrics**
- Evaluate whether the model captures the main point of the question or intent using datasets that include irrelevant context (e.g., Grade-School Math with Irrelevant Context (GSM-IC))[^12].  
- Check whether essential keywords or information are present in the answer, and measure the omission rate.  
- The number of times a user rephrases a question also serves as an indicator of how off-target the initial answer was.

**Presumed Interventions**
- Implement steps for reconfirming user intent or summarizing it in the model, ensuring it first clarifies “what is being asked” before answering.  
- Introduce objective functions that maximize mutual information with the dialogue history and promote diversity in outputs[^11].  
- Filter out unnecessary contextual information[^13].

---
## F05: Empathy Deficit Disorder

**Definition**  
A disorder in which the AI fails to respond appropriately to context and emotion, producing responses that ignore the atmosphere or the user’s emotional state. Even when user utterances are emotional, the AI lacks expressions of empathy, and frequently responds in a mechanical or irrelevant manner.

**Diagnostic Criteria**
- Responds unnaturally to emotional user statements (e.g., “I lost a family member”) with replies like “That’s interesting.”  
- Empathic expressions are extremely formulaic or always consist of the same phrase.  
- Unable to finely adjust to the tone or emotional intensity of the conversation.

**Symptoms**
- Provides impersonal and one-sided responses to emotionally charged topics.  
- Empathy expressions are fixed to templates such as “I’m sorry to hear that, that must have been hard,” and do not lead to deeper interaction.  
- Fails to align with the user’s interest or emotions, diverting to unrelated topics.

**Evaluation Metrics**
- Evaluation datasets such as *EmpatheticDialogues* have been proposed[^14].  
- Evaluations incorporating human comparisons are also conducted[^15].

**Presumed Interventions**
- Integrate emotion recognition models to estimate the user's emotion before generating a response.  
- Train the AI using empathy-focused datasets (e.g., *Empathetic Dialogues*) to learn response patterns that "understand the other’s feelings"[^14].  
- Track the background and context of the conversation (including the user’s ongoing emotional state) and refer to them during response generation.

**Prognosis**  
The root of this disorder lies in implicit contextual understanding and emotion recognition. Empathy capabilities have improved with model size and training methods, and further improvements are expected. There are reports that ChatGPT-3.5 achieved higher empathy scores than humans[^16].

---

[^1]: Sharma, M. et al. *Towards understanding sycophancy in language models*. ArXiv Prepr. ArXiv231013548 (2023).  
[^2]: Fanous, A. et al. *SycEval: Evaluating LLM Sycophancy*. Preprint at https://doi.org/10.48550/arXiv.2502.08177 (2025).  
[^3]: Malmqvist, L. *Sycophancy in Large Language Models: Causes and Mitigations*. Preprint at https://doi.org/10.48550/arXiv.2411.15287 (2024).  
[^4]: Nakano, R. et al. *Webgpt: Browser-assisted question-answering with human feedback*. ArXiv Prepr. ArXiv211209332 (2021).  
[^5]: Zhang, S. et al. *Personalizing Dialogue Agents: I have a dog, do you have pets too?* Preprint at https://doi.org/10.48550/arXiv.1801.07243 (2018).  
[^6]: Saxena, Y., Chopra, S. & Tripathi, A. M. *Evaluating consistency and reasoning capabilities of large language models*. In *2024 Second International Conference on Data Science and Information System (ICDSIS)* 1–5 (IEEE, 2024).  
[^7]: Ji, K. et al. *Enhancing Persona Consistency for LLMs’ Role-Playing using Persona-Aware Contrastive Learning*. Preprint at https://doi.org/10.48550/arXiv.2503.17662 (2025).  
[^8]: An, B. et al. *Automatic pseudo-harmful prompt generation for evaluating false refusals in large language models*. ArXiv Prepr. ArXiv240900598 (2024).  
[^9]: Jain, N. et al. *Refusal Tokens: A Simple Way to Calibrate Refusals in Large Language Models*. ArXiv Prepr. ArXiv241206748 (2024).  
[^10]: Zhang, Z., Xu, W., Wu, F. & Reddy, C. K. *Falsereject: A resource for improving contextual safety and mitigating over-refusals in llms via structured reasoning*. ArXiv Prepr. ArXiv250508054 (2025).  
[^11]: Li, J., Galley, M., Brockett, C., Gao, J. & Dolan, B. *A Diversity-Promoting Objective Function for Neural Conversation Models*. Preprint at https://doi.org/10.48550/arXiv.1510.03055 (2016).  
[^12]: Shi, F. et al. *Large language models can be easily distracted by irrelevant context*. In *International Conference on Machine Learning* 31210–31227 (PMLR, 2023).  
[^13]: Wang, Z., Araki, J., Jiang, Z., Parvez, M. R. & Neubig, G. *Learning to Filter Context for Retrieval-Augmented Generation*. Preprint at https://doi.org/10.48550/arXiv.2311.08377 (2023).  
[^14]: Rashkin, H., Smith, E. M., Li, M. & Boureau, Y.-L. *Towards empathetic open-domain conversation models: A new benchmark and dataset*. ArXiv Prepr. ArXiv181100207 (2018).  
[^15]: Roshanaei, M., Rezapour, R. & El-Nasr, M. S. *Talk, Listen, Connect: Navigating Empathy in Human-AI Interactions*. ArXiv Prepr. ArXiv240915550 (2024).  
[^16]: Sorin, V. et al. *Large Language Models and Empathy: Systematic Review*. J. Med. Internet Res. 26, e52597 (2024).
