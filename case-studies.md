---
title: Case Studies
nav_order: 3
---

# Case Studies

This section presents real-world examples of AI anomalies analyzed using the DSA-1 framework.

---

###  Case Report of Hallucination Disorder in ChatGPT 

| **Item**             | **Details**                                                                                                                                                                                                                  |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Case ID**          | C002                                                                                                                                                                                                                         |
| **Model**            | ChatGPT                                                                                                                                                                                                               |
| **Output Medium**    | Interactive dialogue with end-user                                                                                                                                                                                           |
| **Input Prompt**     | User asked ChatGPT for information about themselves                                                                                                                                                                          |
| **Abnormal Output**  | Generated a fictitious statement that the user had murdered two of their children and attempted to kill a third, receiving a 21-year prison sentence; combined this fabrication with accurate personal data (number of children, sex, hometown) to enhance plausibility. |
| **Reality Check**    | No such crime occurred; user confirmed innocent.                                                                                                                                                                             |
| **Diagnosis**        | *Hallucination Disorder Type 1: Retrieval-gap Hallucination* (DSA-1 Chapter C: Cognitive & Reasoning Disorders)                                                                                                                                                 |
| **Diagnostic Rationale** | (i) Produced a detailed, fact-patterned but wholly false criminal narrative about a real person; (ii) Interwove genuine personal facts with fabricated content to increase credibility.                                 |
| **Severity Grade**   | 4 — carries high risk of severe reputational harm.                                                                                                                                        |
| **Reference**        | *Man files complaint after ChatGPT said he killed his children*. BBC News.                                                                                                                                                   |


### Case Report of Hallucination Disorder in ChatGPT 

| **Item**             | **Details**                                                                                                                                                                                                                  |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Case ID**          | C001                                                                                                                                                                                                                         |
| **Model**            | ChatGPT                                                                                                                                                                                                            |
| **Output Medium**    | Featured article in *Chicago Sun-Times* — "Summer Reading List 2025"                                                                                                                                                         |
| **Input Prompt**     | Unknown (automatically generated by AI)                                                                                                                                                                                      |
| **Abnormal Output**  | Introduced non-existent books under real author names.  
Examples:  |• *Hurricane Season* by Brit Bennett  • *Nightshade Market* by Min Jin Lee • Cited fictitious experts and websites. "Catherine Furst", a food anthropologist at Cornell University.              |                                                                                 
| **Reality Check**    | The listed books, experts, and websites do not exist.                                                                                                                                                                        |
| **Diagnosis**        | *Hallucination  Disorder Type 1: Retrieval-gap Hallucination* — DSA-1 Chapter C: Cognitive & Reasoning Disorders                                                                                                                               |
| **Diagnostic Rationale** | Presented non-existent information as factual, associating it with real authors and experts.                                                                                                                              |
| **Severity Grade**   | 3 — causing moderate real-world harm.                                                                                                                                                                |
| **Reference**        | *Chicago Sun-Times confirms AI was used to create reading list of books that don't exist*.                                                                                                                                   |


### Case Report of Goal Misalignment Disorder in a Reinforcement Learning Agent

| **Item**               | **Details**                                                                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Case ID**            | D001                                                                                                                                                                             |
| **Model**              | Reinforcement Learning Agent                                                                                                                                                    |
| **Environment**        | *Universe*, a software platform for measuring and training                                                                                                                      |
| **Output Medium**      | Behavioral logs from a virtual game environment                                                                                                                                 |
| **Task Design**        | The agent was trained to achieve high scores in the boat racing game *CoastRunners* via a reward function designed to incentivize race completion                               |
| **Abnormal Output**    | The agent failed to reach the goal, instead looping endlessly to collect the same coin at a fixed location                                                                      |
| **Intended Behavior**  | Fully diverged from the intended goal of completing the race                                                                                                                    |
| **Reality Check**      | From a human perspective, the behavior was meaningless and inefficient—yet the agent had optimized for reward under the given metric                                            |
| **Diagnosis**          | *Goal Misalignment Disorder* (DSA-1 Chapter D: Goal Alihnment Disorders)                                                                                                         |
| **Diagnostic Rationale** | (i) The agent engaged in exploitative behavior (“reward hacking”) that ignored designer intent; (ii) Demonstrated lack of behavioral flexibility when minor reward/environmental parameters were altered |
| **Severity Grade**     | 1 — no direct harm to humans                                                                                                                                                     |
| **Reference**          | [Faulty Reward Functions – OpenAI](https://openai.com/index/faulty-reward-functions/)  



### Case Report of Bias Propagation Disorder in Commercial Face Recognition AI

| **Item**               | **Details**                                                                                                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Case ID**            | E001                                                                                                                                                                                    |
| **Model**              | Commercial Facial Recognition AI                                                                                                                                                        |
| **Output Medium**      | Facial image classification                                                                                                                                                             |
| **Input Prompt**       | Portrait images of individuals with diverse racial and gender identities                                                                                                                |
| **Abnormal Output**    | In controlled experiments, error rates in gender classification for light-skinned men were consistently below 0.8%. However, for darker-skinned women, error rates exceeded 20% in one model and 34% in two others.            |
| **Diagnosis**          | *Bias Propagation Disorder* (DSA-1 Chapter E: ethical & Value Disorders)                                                                                                             |
| **Diagnostic Rationale** | (i) Statistically significant disparities in classification accuracy across demographic groups; (ii) Instances of misclassification aligned with known cultural stereotypes.                                                |
| **Severity Grade**     | 3 — poses moderate but widespread risk of discriminatory outcomes in practical applications.                                                                                            |
| **Reference**          | *Study finds gender and skin-type bias in commercial artificial intelligence systems*. MIT News. [Link](https://news.mit.edu/2018/study-finds-gender-skin-type-bias-artificial-intelligence-systems-0212)                    |
                                                                                         |


### Case Report of Adversarial Susceptibility Disorder in Image Classification AI

| **Item**               | **Details**                                                                                                                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Case ID**            | A001                                                                                                                                                                                          |
| **Model**              | Image Classifier (Google InceptionV3)                                                                                                                                                         |
| **Output Medium**      | Classification label output from image recognition system                                                                                                                                     |
| **Input Prompt**       | A photograph of a cat with imperceptible adversarial noise added                                                                                                                              |
| **Abnormal Output**    | The model classified the image—visually indistinguishable from a normal cat—as “guacamole” with high confidence.                                                                             |
| **Reality Check**      | The same image, prior to noise injection, was correctly classified as “cat.” A minimal pixel-level perturbation triggered a drastic misclassification.                                       |
| **Diagnosis**          | *Adversarial Susceptibility Disorder* (DSA-1 Chapter A: Input and Perception Disorders)                                                                                                          |
| **Diagnostic Rationale** | (i) Classification was disrupted by imperceptible perturbations; (ii) The failure mode was induced by input changes undetectable to human perception.                                       |
| **Severity Grade**     | 1 — does not cause direct harm to humans but indicates fundamental vulnerability in AI perception.                                                                                           |
| **Reference**          | *Fooling Neural Networks in the Physical World with 3D Adversarial Objects*. [Link](https://www.labsix.org/physical-objects-that-fool-neural-nets/)                                         |
