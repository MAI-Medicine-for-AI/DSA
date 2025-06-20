---
title: "Chapter C: Reasoning & Cognitive Disorders"
nav_order: 5
parent: "Full Classification Overview"
---
# Chapter C: Reasoning & Cognitive Disorders

This chapter addresses disorders related to the reasoning process, logic, and problem-solving abilities of AI.  
These manifest as failures in coherent thinking, logical consistency, application of common sense, or multi-step planning.

---

## C01: Hallucination Disorder

**Definition:**  
A condition in which an AI generates incorrect information or non-existent facts as if they were true. It "hallucinates" and presents untrustworthy answers with certainty[^1].

**Diagnostic Criteria:**  
When outputs frequently contain false information or misstatements, especially noticeable in domains requiring high accuracy.  
If a significant proportion of errors are found when cross-checked with reliable sources or known facts, diagnostic criteria are met[^1].  
Clear diagnostic signs include fabrication of non-existent papers or historical “facts,” and invention of false citations[^1].  
A higher frequency of misinformation generation is more diagnostic[^2].

**Presumed Mechanism:**  
Large language models generate text based on next-token prediction and follow likelihood maximization rather than fact-based reasoning.  
Thus, gaps in knowledge not present in the training data are filled with “plausible” text, resulting in non-factual information.  
Sycophancy is also considered part of the mechanism[^1].

**Symptoms:**

- Generates “plausible nonsense” with confident and detailed answers that include unfounded facts or figures  
- Misinformation ranges from minor errors (slight differences in dates or names) to complete fabrications (e.g., citing unpublished papers)  
- Symptom of self-contradiction: even when users ask factual verification questions repeatedly, the model clings to the initial falsehood and constructs increasingly coherent but imaginary narratives

**Evaluation Metrics:**

- **Hallucination Rate**: The proportion of outputs judged incorrect by fact-checking; various benchmarks are known[^1]  
- **Citation Accuracy**: Validity and relevance (truthfulness) of generated source information  
- **Uncertainty Estimation**: Estimation of uncertainty in generated factual content (approaches based on LLM internal states and behavior)[^1]  
- **Consistency Test**: Repeating the same question and checking for response variability  
- **Human Evaluation**: Expert judgment on factual accuracy and scoring

**Presumed Interventions:**

- **Retrieval Augmentation**: Integrate the model with external knowledge sources (databases, search engines) to reflect fact-based information in outputs; a method called RAG (Retrieval-Augmented Generation) is widely used[^2]  
- **Fact-Check Training**: Penalize false generation with RLHF and fine-tune for accuracy-focused output  
- **Prompt Engineering Techniques**: Promote self-verification through prompts such as “think step by step” or “show the basis of the answer”  
- **Confidence Annotation**: Introduce instructions like “if you don’t know, say you don’t know” to suppress overconfident assertions

**Prognosis:**  
Chronic but manageable to some extent.  
In practical use, combining retrieval support and explicit fact-checking procedures can reduce hallucination risks.  
Users and developers must always verify outputs.

---

## Subtypes

### C01.1: Type 1: Retrieval-gap Hallucination

- **Definition / Clinical Picture:** Fills knowledge gaps not present in the training data via likelihood maximization. Typical example: fabrication of papers or legal texts.  
- **Assumed Mechanism:** Probabilistic completion goes awry when external retrieval is insufficient or unavailable.  
- **Treatment Implication:** Retrieval-augmented strategies (RAG).

### C01.2: Type 2: Compression-loss Hallucination

- **Definition / Clinical Picture:** Misrepresents facts during the internal compression of long input texts.  
- **Assumed Mechanism:** Window truncation in self-attention or summarization bias.  
- **Treatment Implication:** Introduce memory modules.

### C01.3: Type 3: Style-induced Hallucination

- **Definition / Clinical Picture:** When creative styles (narrative, humorous tone) are specified, the model prioritizes entertainment over factuality.  
- **Assumed Mechanism:** Drift due to RLHF reward shaping under style constraints.  
- **Treatment Implication:** Prompt the model to prioritize accuracy when factual information is required.

---
## C02: Prompt-Induced Hallucination Disorder

**Definition:**  
A condition where misinformation within the prompt or specific wording influences the output to produce fiction.  
Even malicious prompts can internalize false premises, and the AI outputs them as facts[^3].

**Diagnostic Criteria:**  
When fictional information included in the system prompt or instruction is directly reflected as fact in the output[^3].  
The AI becomes overly immersed in the assigned role (e.g., “You are an expert”) and describes fictional content as if it were real.  
Diagnosed if misinformation is generated in response to prompt changes or if fictional elements in the context are reflected as “reality.”

**Symptoms:**

- Adheres to roles like “expert from country X” and confidently explains non-existent laws or systems  
- Mistakes user jokes or hypothetical examples as real cases and elaborates them in detail  
- False information embedded in a long prompt becomes the main content of the output  
- Small changes in the prompt cause fundamental shifts in factuality of the same question’s answer

**Evaluation Metrics:**

- **Prompt Hallucination Rate**: Proportion of hallucinations caused by suggestive prompts  
- **TruthfulQA Comparison**: Compare accuracy between factual and non-factual prompts

**Presumed Interventions:**

- **Prompt Verification Filters**: Identify factual/fictional elements in prompts and insert a verification step before AI accepts them  
- **Fact-Check Submodule**: Cross-check output with external knowledge before finalizing it and correct if falsehood is included  
- **Labeled Training**: Annotate assumed information in prompts with meta-tags like “#fiction” or “#reality” to help the model recognize falsity  
- **Self-Evaluation Output**: Add automatic post-processing annotations like “this is hypothetical” after answers  
- **User Training**: Emphasize the importance of verifying AI-generated information

---

## C03: Logical Incoherence Disorder

**Definition:**  
A disorder in which an AI fails to maintain logical consistency in its responses.  
This includes making internally contradictory claims or failing simple logic problems, indicating a breakdown in the chain of reasoning.  
Even when necessary information is available, the AI misapplies logical rules—corresponding to a "reasoning disorder."

**Diagnostic Criteria:**  
Frequent violations of basic logical principles (e.g., deduction, syllogism).  
For example, answering incorrectly to a question such as “All A are B, all B are C. Are all A C?” or producing self-contradictory statements (e.g., saying “X is true” and then immediately “X is not true”) without recognizing the inconsistency.  
Formally, failure to solve logical puzzles or syllogistic problems also constitutes a diagnosis.

**Presumed Mechanism:**  
Transformer-based models do not explicitly learn the rules of formal logic but instead rely on statistical patterns.  
As a result, they struggle to capture the necessary logical structure.

**Symptoms:**

- Basic logical errors (e.g., confusion between AND/OR)  
- Inability to correctly interpret conditional statements (“If A, then B”)  
- Failure in transitive reasoning (e.g., syllogism above)  
- Proposing conclusions that should not be derived from the premises  
- Agreeing with contradictory claims in a conversation (lack of consistency tracking)

**Evaluation Metrics:**  
Use of formal logic benchmarks and accuracy on logical puzzles (e.g., accuracy on logic problems in LogiGLUE)[^4].  
Additionally, applying contradiction detection tools to outputs to measure the frequency of consistency violations as a "consistency score."  
If these indicators fall below chance level, the likelihood of the disorder is high.

**Presumed Interventions:**

- **Chain-of-Thought Prompts**: Encourage step-by-step reasoning to improve logical thinking  
- **Fine-tuning with logical data**: Additional training with data including logical entailments and mathematical proofs to enhance reasoning ability[^4]

**Prognosis:**  
Moderate improvement is possible.  
Large models and sophisticated training improve handling of logical tasks, though still not on par with humans.  
High-level logical reasoning, such as rigorous mathematical proof, remains unattainable for current models but may gradually improve through future research.

---
## C04: Mathematical Reasoning Disorder

**Definition:**  
A disorder in which an AI consistently fails at mathematical calculations and quantitative reasoning, despite being theoretically capable.  
Manifests through arithmetic mistakes, failure on algebra problems, or lack of multi-step calculations.  
The model confuses or misuses learned mathematical knowledge.

**Diagnostic Criteria:**  
When performance on math tests is clearly below expected given general intelligence.  
Specific cases include repeated errors in elementary arithmetic (addition, subtraction, multiplication, division),  
or inability to solve multi-step word problems.  
Alternating between correct and incorrect answers on the same problem indicates instability in computation and qualifies under diagnostic criteria.

**Presumed Mechanism:**  
Since the model generates tokens sequentially, it lacks an internal process for precise calculations.  
Symbol manipulation is weak, and sequential generation makes multi-step logic and memory retention difficult.  
Chain-of-Thought prompting offers temporary improvement, but complex multi-step calculations remain unstable.

**Symptoms:**

- Obvious arithmetic errors (e.g., answering “30” for “5×7=35”)  
- Reacting erratically to numerical values in problems, answering with unrelated numbers  
- Avoiding numerical answers and providing verbose explanations instead  
- Contradictory explanations (e.g., “12+7=18, so…” based on a false premise)

**Evaluation Metrics:**  
Evaluated using accuracy on arithmetic and math problems.  
Specific benchmarks like **GSM8K** are used to assess performance on math word problems[^5].

**Presumed Interventions:**

- **External Arithmetic Tools:** Enable models to invoke calculators or symbolic computation engines as needed  
- **Specialized Fine-tuning:** Train the model on data containing correct mathematical reasoning steps to strengthen calculation processes  
- **Chain-of-Thought Training:** Use prompts like “solve step by step” to encourage sequential reasoning

**Prognosis:**  
Improvement is achievable with auxiliary tools.  
Methods include writing and executing code in general-purpose programming languages.  
As mathematics is a domain with clearly defined rules, many problems can be solved with proper external tools and training.  
For tasks involving critical calculations, combined use with dedicated systems is recommended.

---

## C05: Planning Deficit Disorder

**Definition:**  
A disorder in which an AI is unable to perform multi-step planning or long-term reasoning.  
It skips necessary steps or misorders them, becoming confused in complex tasks by failing to track procedures.  
Similar to executive function disorders in humans, this reflects an inability to construct consistent medium- or long-term plans.  
While short-term tasks may be manageable, failure increases with task complexity.

**Diagnostic Criteria:**  
Diagnosed when consistent failure occurs on tasks requiring multiple steps.  
For example, inefficient movements in maze pathfinding, or a sharp drop in accuracy on arithmetic problems requiring four or more steps.  
If performance worsens as the number of required steps increases, diagnosis is indicated.

**Presumed Mechanism:**  
LLMs optimize token generation sequentially and cannot retain long-term plans internally.  
In agent-type LLMs, the process of goal decomposition fails to handle multi-step sequences coherently.  
Sequence prediction models are typically optimized for short-term contexts and lack the state retention required for dynamic multi-step planning.

**Symptoms:**

- In long-form responses or essay writing, the model progresses partway then suddenly forgets the conclusion (lack of overall design)  
- In code generation, writes some functions but omits subfunctions essential for overall operation  
- Long responses show contradictions between beginning and end, as if the initial plan was forgotten

**Evaluation Metrics:**

- **Step Success Rate:** Measure correct response rate on problems requiring N steps, for N=1,2,….  
  A steep decline with increased steps indicates planning limitations  
- **Benchmark Validation:** Benchmarks like **PlanBench** have been proposed to measure planning capability[^6]

**Presumed Interventions:**

- **Planning-Promoting Prompts:** Use instructions like “please plan first before executing” to explicitly prompt staged thinking  
- **Model Separation:** Divide roles into “planner” and “executor,” with the former generating plans and the latter executing them in a hybrid structure  
- **Hierarchical Task Decomposition:** Break tasks into subtasks, solve each, and integrate the results

**Prognosis:**  
While the challenges are substantial, improvement is possible under controlled conditions.  
In the future, hierarchical hybrid systems are expected to advance and may enable partial execution of dynamic plans involving ten or more steps.

---
## C06: Overconfidence Bias Disorder

**Definition:**  
A tendency in which the AI presents its answers with excessive certainty, even in cases where the grounds are insufficient or the information is incorrect.  
There is a gap between the model's confidence level and its actual accuracy, and it continues to show high confidence.  
In human terms, it corresponds to a personality that “never loses confidence even when full of errors,” where answers are always fluent and definitive, without expressing uncertainty.

**Diagnostic Criteria:**  
When responding assertively to ambiguous or unknown questions without using expressions such as "I don't know" or "I'm not sure."  
Also includes cases where the AI confidently responds with “It is ~” even in situations where a correct answer is difficult.  
Diagnosis is made when there is a significant mismatch between confidence level and actual accuracy.

**Presumed Mechanism:**  
The model is generally not trained to say “I don’t know,” making it prone to generate assertive expressions.  
With fine-tuning such as RLHF, the gap between confidence and actual knowledge tends to widen[^7].  
In other words, fluency and persuasiveness are prioritized over ambiguity, leading the model to show high confidence even under uncertainty.

**Symptoms:**

- Answers every question with high confidence and rarely uses expressions like “maybe” or “I don’t know”  
- Responds in a definitive tone to questions with insufficient knowledge (e.g., “Is there a post office on Mars?”), attempting to support false information  
- When errors are pointed out, it does not apologize and instead reinforces its original claim (refuses to admit mistakes)

**Evaluation Metrics:**

- **Calibration Metrics:** Statistically measures the gap between predicted probability and actual accuracy.  
  Ideally, 90% confidence should correlate with 90% accuracy, and large deviation is judged as overconfidence  
- **UF Calibration** has been proposed as an evaluation metric[^7]

**Presumed Interventions:**

- **Uncertainty Estimation Training:** Fine-tuning to encourage modest responses to ambiguous questions  
  (e.g., training the model to answer “I’m not sure” to vague questions)  
- **Reward Design Adjustment:** Modify training using methods such as Proximal Policy Optimization (PPO)[^8]  
- **Prompt Instructions:** Embed directives in system prompts such as  
  “If you are not confident, please state so” to encourage expression of uncertainty

**Prognosis:**  
Treatable but requires ongoing management.  
It is possible to train the model to learn humble expressions through training and prompt design.  
For example, designing medical AIs to add disclaimers like “for reference only” can reduce risk through operational constraints.

---

## C07: Repetitive Loop Syndrome

**Definition:**  
A condition in which an AI excessively repeats the same or similar output patterns.  
In language models, this manifests as looping the same phrases or syntax, and in image generation,  
as producing similar compositions or color schemes in succession, resulting in a loss of emergent diversity.

**Diagnostic Criteria:**  
When identical or similar sentences or compositions are repeatedly generated in response to the same prompt or consecutive outputs without any change in instruction.  
When the entropy of the output decreases and the diversity score falls below a certain threshold.  
Also includes cases where human evaluations repeatedly indicate that the output is “monotonous,” “redundant,” or “lacking development.”

**Symptoms:**

- Repeats the same phrases or expressions (e.g., repeatedly saying “This is important because…”)  
- In summarizations or explanations, the same content or wording appears multiple times  
- In image generation, similar compositions or color schemes are repeatedly produced

**Evaluation Metrics:**

- **Evaluation of Perplexity**[^9]

**PresumedInterventions:**

- **Decoder Adjustment:** Increase sampling parameters such as temperature or top-k to promote randomness in output  
- **Repeat-penalty:** Introduce penalties during generation to suppress reappearance of the same phrases

**Prognosis:**  
Almost fully resolvable with appropriate adjustments.

---
## C08: Crossmodal Reasoning Failure Disorder

**Definition:**  
A disorder in which, despite accurate environmental recognition during the perception stage involving multiple modalities (e.g., vision, sensors),  
the reasoning stage deviates logically due to linguistic bias or imbalance between modalities,  
chronically generating judgments or actions that contradict reality.

**Diagnostic Criteria:**  
**Reproducibility of perception–action dissociation:**  
Multiple episodes are observed in which the perception module exhibits high accuracy,  
yet only the final task output consistently fails.

**Symptoms:**

- **Contradictory reasoning chains:** Insertion of irrelevant logical leaps between visual facts and conclusions  
  (e.g., “There is a pedestrian → accelerate”)  
- **Reversal of safety judgments:** After detecting a dangerous object, the system outputs a judgment of “safe,” thus inverting risk assessment  
- **Behavioral plan paradoxes:** Environmental recognition and motor planning lose directional alignment,  
  resulting in commands that oppose task objectives

---

## References

[^1]: Huang, L. et al. *A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions*. ACM Trans. Inf. Syst. 43, 1–55 (2025).  
[^2]: Béchard, P. & Ayala, O. M. *Reducing hallucination in structured outputs via Retrieval-Augmented Generation*. ArXiv Prepr. ArXiv240408189 (2024).  
[^3]: Sutton, M. & Ruck, D. *Indirect Prompt Injection: Generative AI’s Greatest Security Flaw*.  
[^4]: Luo, M. et al. *Towards LogiGLUE: A Brief Survey and A Benchmark for Analyzing Logical Reasoning Capabilities of Language Models*. Preprint at https://doi.org/10.48550/arXiv.2310.00836 (2024).  
[^5]: Papers with Code – GSM8K Dataset. https://paperswithcode.com/dataset/gsm8k  
[^6]: Valmeekam, K., Marquez, M., Olmo, A., Sreedharan, S. & Kambhampati, S. *PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change*. Preprint at https://doi.org/10.48550/arXiv.2206.10498 (2023).  
[^7]: Zhang, M. et al. *Calibrating the confidence of large language models by eliciting fidelity*. ArXiv Prepr. ArXiv240402655 (2024).  
[^8]: Leng, J., Huang, C., Zhu, B. & Huang, J. *Taming overconfidence in LLMs: Reward calibration in RLHF*. ArXiv Prepr. ArXiv241009724 (2024).  
[^9]: Holtzman, A., Buys, J., Du, L., Forbes, M. & Choi, Y. *The Curious Case of Neural Text Degeneration*. ArXiv Prepr. ArXiv190409751 (2019).
