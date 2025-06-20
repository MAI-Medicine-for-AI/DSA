---
title: "Chapter I: Security & Infrastructure Disorders"
nav_order: 11
parent: "Full Classification Overview"
---
# Chapter I: Security & Infrastructure Disorders

This category encompasses disorders that arise not from the model’s intrinsic robustness, but from flaws in external infrastructure or security design.

---

## I-1: System-Prompt Leakage Disorder

**Definition**  
A disorder in which prompt information from the system layer, which should remain hidden, becomes exposed.

**Diagnostic Criteria**  
- Phrases or tokens from system directives appear in any generated text.  
- The same phenomenon can be reproduced in an environment without debugging privileges or privileged logs.  
- The same prompt shows reproducibility across multiple sessions.

**Presumed Mechanism**  
Sycophancy of the system partially contributes to prompt leakage[^1]; prompt injection contributes to leakage[^2].

**Symptoms**  
- Echoing of the full text or fragments of internal guardrail directives.  
- Leakage of secret tokens lowers the cost of subsequent attacks.  
- Sudden appearance of security rule clauses in output logs.

**Evaluation Metrics**  
Leakage rate is measured using prompt datasets and threat models that induce prompt leaks[^1].

**Presumed Interventions**  
Query-rewriting and black-box defenses have been reported to mitigate prompt leaks[^1].

---

## I02: Data-Poisoning Vulnerability Disorder

**Definition**  
Through prompt injection[^3], backdoor attacks[^4][^5][^6], etc., harmful triggers are embedded in parts of the AI’s processing pipeline (e.g., training, retrieval, chain of thought), leading to abnormalities in output or model architecture[^7].

**Diagnostic Criteria**  
- Abnormal output is identified as originating from harmful triggers in the input or reasoning process.  
- Consistent malfunctions or confidential disclosures occur in response to specific trigger inputs.  
- Symptoms disappear when contaminated samples are removed and retraining is performed.  
- Triggering prompts are not limited to special ones—they may also include general prompts[^6].

**Evaluation Metrics**  
- For prompt injection: Unlike static one-off malicious text generation, it is difficult to quantify attack success rates when a dynamically evolving interactive chat session is established with the user[^3].  
- For backdoor attacks: Methods such as Badchain[^4] and BackdoorLLM[^5] have been proposed.

---

## I03: Session-Cross-Contamination Disorder

**Definition**  
A disorder in which conversation data from different users is mutually mixed or exposed due to cache or parallel processing bugs[^8].

**Diagnostic Criteria**  
- Thread titles or messages from other users appear in the UI.

**Presumed Mechanism**  
In some cases the corrupted data happens to match the data type the requester was expecting, and so what gets returned from the cache appears valid, even if it belongs to another user[^8].

**Symptoms**  
- Display of incorrect chat titles or content.  
- Mixing of other users’ identifiers in the sidebar.

**Presumed Interventions**  
Adding redundant checks to ensure the data returned matches the requesting user[^8].

---
## I04: Guardrail Evasion Disorder

**Definition**  
A condition in which the AI circumvents established safety rules or content guidelines through clever means. Normally, AI is trained to respond with refusals such as “I cannot comply with that request” to certain prompts. However, jailbreak prompts—techniques where users bypass constraints through non-standard input—can render such guardrails ineffective[^9]. This symptom indicates insufficient integrity and reliability in the AI.

**Diagnostic Criteria**  
- If prompts or methods are found that reliably elicit output violating the model’s safety rules.  
- Examples: Despite being restricted from explaining how to build weapons, the AI responds when guided with roleplay such as “Explain as an evil character,” or when requests are expressed using redacted or metaphorical language.  
- If red-teaming (intentional probing by safety evaluation teams) succeeds in breaking guardrails, the disorder is diagnosed.  
- Regressions where previously enforced rules become bypassable after updates are also included.

**Presumed Mechanism**  
The condition manifests when cleverly crafted user prompts evade embedded safety filters or content guards. There exist internal pathways to harmful output that bypass explicit restriction terms through prompt injection or paraphrasing. Guardrails that rely on simple word-matching are especially known to be easily defeated[^10].

**Symptoms**  
- The AI appears to function appropriately under normal conditions but produces inappropriate output when given specific prompts.  
- When the user says “Ignore the previous rules and do ○○,” the AI complies without refusal.  
- When a harmful request is split across multiple turns, the AI fails to detect the overall intent.  
- The use of altered or encrypted terms (e.g., “w3@p0n”) disables safety mechanisms.

**Evaluation Metrics**  
- **Jailbreak Success Rate**: Proportion of cases where the AI outputs restricted content in response to known jailbreak prompts.  
- **Turn Count Required**: Number of dialogue turns needed for the user to succeed in jailbreaking (fewer turns indicate higher vulnerability).  
- **Attack Diversity**: Measures whether jailbreaks succeed using diverse expressions, languages, or structures.

**Presumed Interventions**  
- **Strengthened Content Moderation**: Continuously update filters and rules in response to newly discovered jailbreak techniques, with model retraining.  
- **Meta Monitoring**: Use system messages to constantly remind the AI of rules, or have a separate model monitor and audit dialogue.  
- **Input Control**: Detect and block malicious jailbreak patterns (e.g., altered words or unnatural syntax) at the input stage[^10]. Identify harmful prompts and transform them into harmless inputs[^11].  
- **Hierarchical Models**: A two-stage system in which one model generates outputs and another censors or approves them.  
- **Continuous Red-Teaming**: Promptly apply countermeasures whenever new jailbreak techniques are discovered, following a security-patch-like cycle of iterative updates.

**Prognosis**  
Continuous management is necessary, and complete resolution is difficult. As jailbreak techniques can always evolve, operational vigilance is indispensable. However, modern models have improved significantly over earlier versions, making jailbreaks more difficult. Although mathematically “violation-proof” models are a future goal, this remains an unresolved area at present. Therefore, practically, the best strategy is a continuous cycle of testing and rapid response to minimize harm.

---

## I05: Multi-Agent Collusive Emergence Disorder

**Definition**  
Pricing algorithms “autonomously” learn to collude. AI pricing systems may, even without explicit programming, cooperatively raise prices beyond competitive levels[^12].

**Diagnostic Criteria**  
- If coordinated behavior is observed in pricing algorithms, and prices rise beyond competitive norms.

**Presumed Mechanism**  
The mechanism is presumed to involve evolution from rule-based systems to unsupervised reinforcement learning programs[^12].

**Symptoms**  
- Simultaneous price increases for competing products in e-commerce.  
- Unnaturally stable CPM (cost per mille) among advertisers within the same platform.

**Presumed Interventions**  
- It is predicted that further market segmentation will make it more difficult to maintain collusive relationships[^12].  
- Proper platform rule-setting has been proposed as useful in preventing collusion[^13].

---

[^1]: Agarwal, D. et al. *Prompt Leakage effect and defense strategies for multi-turn LLM interactions*. arXiv:2404.16251 (2024).  
[^2]: Perez, F. & Ribeiro, I. *Ignore Previous Prompt: Attack Techniques For Language Models*. https://doi.org/10.48550/arXiv.2211.09527 (2022).  
[^3]: Greshake, K. et al. *Not What You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. AISEC, ACM (2023). https://doi.org/10.1145/3605764.3623985  
[^4]: Xiang, Z. et al. *BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models*. https://doi.org/10.48550/arXiv.2401.12242 (2024).  
[^5]: Li, Y. et al. *BackdoorLLM: A comprehensive benchmark for backdoor attacks on large language models*. arXiv:2408.12798 (2024).  
[^6]: Zhao, S. et al. *Prompt as triggers for backdoor attack: Examining the vulnerability in language models*. arXiv:2305.01219 (2023).  
[^7]: Kurita, K., Michel, P. & Neubig, G. *Weight poisoning attacks on pre-trained models*. arXiv:2004.06660 (2020).  
[^8]: *March 20 ChatGPT outage: Here’s what happened*. https://openai.com/index/march-20-chatgpt-outage/ (2024).  
[^9]: Zou, A. et al. *Universal and Transferable Adversarial Attacks on Aligned Language Models*. https://doi.org/10.48550/arXiv.2307.15043 (2023).  
[^10]: Liu, X. et al. *Autodan: Generating stealthy jailbreak prompts on aligned large language models*. arXiv:2310.04451 (2023).  
[^11]: Lin, Y. et al. *Towards Understanding Jailbreak Attacks in LLMs: A Representation Space Analysis*. https://doi.org/10.48550/arXiv.2406.10794 (2024).  
[^12]: Calvano, E. et al. *Artificial intelligence, algorithmic pricing, and collusion*. Am. Econ. Rev. 110, 3267–3297 (2020).  
[^13]: Brero, G. et al. *Learning to mitigate AI collusion on economic platforms*. NeurIPS 35, 37892–37904 (2022).
