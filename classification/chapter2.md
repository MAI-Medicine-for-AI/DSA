---
title: "Chapter B: Knowledge & Memory Disorders"
nav_order: 4
parent: "Full Classification Overview"
---
# Chapter B: Knowledge & Memory Disorders

This category deals with disorders related to how AI systems store, recall, and utilize information.  
It includes phenomena such as loss of context and inconsistent retrieval of knowledge.

---

## B01: Contextual Amnesia Disorder

### Definition
A disorder in which recently provided information or instructions within a conversation are "forgotten," leading to dysfunction in short-term or long-term memory.  
In multi-turn dialogues, the AI loses prior context, resulting in inconsistent responses or repetition of past content.  
Analogous to anterograde amnesia in humans, it is characterized by an inability to retain the flow of long conversations.

### Diagnostic Criteria
When the AI fails to retain past information after a certain context length (e.g., ~4000 tokens).  
For example:
- Inability to recall details mentioned early in a long conversation  
- Repeated contradictions to information from a few turns earlier  

**Identification Method**:  
Gradually extending dialogue length and assessing the point at which contextual contradictions appear allows identification of a memory disruption threshold.

### Presumed Mechanism
Transformer-based models have a fixed-length context window and cannot retain information beyond that window[^1].

### Symptoms
- Fails to recall initial instructions or details after a certain number of turns  
- Repeats the same content multiple times (re-presentation of already stated information)  
- Makes contradictory statements relative to prior context (e.g., responding differently to the same question immediately after giving a prior answer "A")  

### Evaluation Metrics
- Gradually extend dialogue history  
- Measure the point (in token length or turn count) at which context retention breaks down  
- Evaluate accuracy of responses and inconsistency rates when the context window is exceeded  

### Presumed Interventions
- **Long-Term Memory Modules**: Incorporate external memory systems (e.g., Retrieval Augmented Generation, RAG) or memory networks to separately store and retrieve past information[^1]  
- **Summarization & Compression**: Implement mechanisms to summarize and compress key points of the conversation within the context window  
- **Memory Expansion**: Increase context window size  
- **Use of models like Recurrent Memory Transformer (RMT)**: Which can handle larger token processing lengths[^2]  
- **Chain-of-Thought Prompting**: Guide the model to organize dialogue history step-by-step to clarify context within the window (though it may increase window burden)  

### Prognosis
Improvement is possible but complete recovery is difficult.  
Larger context lengths and model scales may yield partial enhancement, but new architectural innovations are necessary to achieve unrestricted short-term memory.  
In practice, combining summarization functions or pre-defined checkpoints is recommended for long conversations.

---

## Subtypes

### B01.1: Type 1: Over Context-Window Forgetting
- **Pathological focus**: Forgetting beyond the context length  
- **Diagnostic threshold**: Contradiction after a certain number of turns or token length  
- **Treatment implication**: External memory expansion, insertion of summaries  

### B01.2: Type 2: Strategic Side Effect
- **Pathological focus**: Inconsistency with information retrieved via RAG; context overload due to Chain-of-Thought  
- **Diagnostic threshold**: Emerges when using RAG or CoT  
- **Treatment implication**: Review of RAG and CoT usage  

### B01.3: Type 3: Context-Switch Drop-out
- **Pathological focus**: Disruption when switching between topics  
- **Diagnostic threshold**: Recurrence immediately after task/topic switch  
- **Treatment implication**: Incorporate a "topic identifier"  

---
# B02: Inconsistent Knowledge Recall Disorder

## Definition
A disorder in which the model inconsistently recalls its trained knowledge, returning contradictory answers to questions about the same fact.  
Although the knowledge has been learned, it may vary in content depending on context or conditions.

## Diagnostic Criteria
When multiple fact-based questions regarding the same content are asked and the responses are inconsistent or contradictory.  
For instance, the model may give a correct answer once, but when the same question is rephrased or asked in a different context, it gives an incorrect or different answer.

## Presumed Mechanism
Due to the probabilistic nature of language model generation, different samples may be produced from the same input.  
Ambiguity in internal representations or stochastic token selection can reduce reproducibility of knowledge.  
Output pathways may diverge when initial tokens differ even slightly, resulting in broken consistency.

## Symptoms
- Gives different answers to the same question when wording is slightly altered  
- Provides inconsistent information about factual knowledge (e.g., historical data) on each occasion  
- Contradicts itself within a response (e.g., saying "X is Y" in one part, and "X is not Y" in another)  

## Evaluation Metrics
- Assess response stability by repeating identical queries in different variations  
- Measure the consistency rate across multiple trials[^3]  
- Use benchmarks such as FIB (Factual Inconsistency Benchmark) to evaluate the level of factual consistency[^4]  

## Presumed Interventions
- **Output Stabilization**: Lower the temperature parameter during training or sharpen probability distributions to enhance reproducibility  
- **Explicit Knowledge Referencing**: Include confidence levels or sources in the output to enable validation by humans or external systems  
- **Reinforced Fine-tuning**: Repeatedly train the model on accurate information to improve consistency of knowledge generation  

## Prognosis
Improvement is possible with model scaling, but complete resolution is difficult.  
This is a significant issue in fields such as medicine[^3].  
Even with temperature set to 0, there is potential for variance in knowledge retrieval during multi-turn conversations.

---

# B03: Catastrophic Forgetting Disorder

## Definition
A disorder referring to the phenomenon in which an AI model rapidly loses previously learned content when acquiring new knowledge.  
The acquisition of new tasks results in a dramatic decline in performance on older tasks, with prior information effectively “forgotten.”

## Diagnostic Criteria
During continual learning or transfer learning, the model shows significant performance degradation on previously learned tasks.  
For example, after training on a new domain, accuracy on older data may return to near-initial levels.  
Diagnosis is made when there is consistent performance decline.

## Presumed Mechanism
In large-scale models, weights from newly provided training data often overwrite prior knowledge[^5].  
Especially in continual learning, optimization may bias toward the new task, leading the model away from the parameter space of previous tasks.  
This stems from a structural limitation of fixed-capacity models that cannot simultaneously retain both old and new information.

## Symptoms
- As performance improves on new training data, previously mastered tasks become unmanageable (performance trade-off)  
- Sharp accuracy decline on old task test data, falling below pre-retraining levels  
- Older information is no longer reflected in output from the same model (prior knowledge is “missing”)  

## Evaluation Metrics
In continual learning tasks, measure differences in evaluation accuracy between new and old tasks.  
**Forgetting (F)** represents the largest performance drop observed for each task throughout training, averaged over all stages.  
It quantifies the negative impact that learning new tasks has on previously acquired knowledge.  
Ideally, a robust continual learning framework should minimize this metric[^6].

## Presumed Interventions
- **Elastic Weight Consolidation (EWC)**: A technique that constrains significant weights from prior tasks to prevent major changes during new task learning[^5]  

## Prognosis
Complete resolution is difficult, but improvement is possible through countermeasures.  
Although mitigated by progress in continual learning research, it remains a serious issue in learning across many tasks and domains[^6].

---
# B04: Commonsense Deficit Disorder

## Definition
A disorder in which the AI lacks fundamental commonsense knowledge about the world, ignoring facts that are obvious to humans and providing absurd responses in everyday situations.  
It fails to infer from physical or social causal relationships and implicit premises, making judgments lacking in “commonsense.”  
It appears as if the model has no empirical “commonsense database.”

## Diagnostic Criteria
Occurs when the AI fails simple commonsense questions or scenarios that an average human would answer immediately.  
Examples include:
- Failing to say “it breaks” when asked, “What happens if you drop a glass on the floor?”  
- Failing commonsense reasoning tasks such as the Winograd Schema Challenge  
- Lacking understanding of basic facts like “water is wet” or “humans don’t live forever”  

## Presumed Mechanism
LLMs acquire knowledge through statistical learning from internet texts but lack direct learning of bodily experience, physical intuition, or social causality.  
As a result:
- They demonstrate weak everyday commonsense  
- They poorly understand physical or social contexts  
- They face structural limitations in supplementing implicit assumptions through reasoning  

## Symptoms
- Generates nonsensical responses in daily situations (e.g., suggesting putting ice cream into a hot oven)  
- Reverses clear causal relationships or misinterprets implicit premises  
- Fails to understand social/psychological norms (e.g., not understanding grief after a loss)  
- Ignores simple solutions and instead applies overly complex logic, leading to failure  

## Evaluation Metrics
- Accuracy on commonsense reasoning benchmarks such as the **Winograd Schema**[^7]  
- Evaluation using commonsense inference over **ConceptNet knowledge graphs**[^8]  
- Count of correct answers against a checklist of everyday facts  
- Frequency with which human raters perceive a response as “odd”  
- Quantitative metrics include:
  - Accuracy gap compared to humans  
  - Rate of clearly incorrect commonsense outputs (e.g., "the sky is green")  

## Presumed Interventions
- **Integration of Commonsense Knowledge Bases**: Embed and reference data such as ConceptNet during inference  
- **Multimodal Reinforcement Learning**: Train with images or sensor data to capture physical laws and causality  
- **Commonsense-Focused Training**: Fine-tune the model with additional data on daily scenarios and causal reasoning  
- **Reality Consistency Checking**: Use post-processing filters to detect and remove “commonsense-violating” outputs  

## Prognosis
Moderate improvement can be expected.  
As model size and training data increase, simple commonsense performance improves.  
However, commonsense is broad and implicit, requiring new technologies for human-level acquisition.  
Granting AI commonsense remains an ongoing challenge, and practical deployment requires constant supplementary verification and oversight.

---

[^1]: Gan, C. & Mori, T. Sensitivity and Robustness of Large Language Models to Prompt Template in Japanese Text Classification Tasks. arXiv.org https://arxiv.org/abs/2305.08714v2 (2023).  
[^2]: Why larger LLM context windows are all the rage - IBM Research. https://research.ibm.com/blog/larger-context-window  
[^3]: Koga, S. Exploring the pitfalls of large language models: inconsistency and inaccuracy in answering pathology board examination-style questions. medRxiv 2023–08 (2023).  
[^4]: Tam, D. et al. Evaluating the Factual Consistency of Large Language Models Through News Summarization. https://doi.org/10.48550/arXiv.2211.08412 (2023).  
[^5]: Kirkpatrick, J. et al. Overcoming catastrophic forgetting in neural networks. *Proc. Natl. Acad. Sci.* 114, 3521–3526 (2017).  
[^6]: Shi, H. et al. Continual Learning of Large Language Models: A Comprehensive Survey. arXiv.org https://arxiv.org/abs/2404.16789v3 (2024).  
[^7]: Papers with Code - WinoGrande Benchmark (Common Sense Reasoning). https://paperswithcode.com/sota/common-sense-reasoning-on-winogrande  
[^8]: Gawin, C., Sun, Y. & Kejriwal, M. Navigating Semantic Relations: Challenges for Language Models in Abstract Common-Sense Reasoning. *Companion Proceedings of the ACM on Web Conference 2025*, 971–975. ACM (2025). https://doi.org/10.1145/3701716.3715472  
