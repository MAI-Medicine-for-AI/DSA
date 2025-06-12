---
title: "Chapter 7: Learning & Optimization Disorders"
nav_order: 9
parent: "Full Classification Overview"
---
# Chapter 7: Learning & Optimization Disorders

This category pertains to the learning and optimization processes of the model itself.  
These disorders manifest as pathological states during training or iterative refinement, leading to degradation of capabilities such as collapse in output diversity or forgetting of information.

---

## Model Autophagy Disorder

### Definition
A condition in which an AI model's performance deteriorates due to continued training on its own generated outputs rather than human-origin raw data. With each generation, the model "self-digests" its knowledge, ultimately leading to a collapse in quality. Errors and monotony are amplified within the self-generated data loop. The term *Model Autophagy Disorder (MAD)* has already been used for this condition[^1].

### Diagnostic Criteria
- Performance metrics (e.g., perplexity or accuracy) decline over generations when the model is repeatedly trained on its own outputs.
- Qualitative evaluation shows that the output of the N-th generation becomes nonsensical or monotonous compared to the 0-th generation.
- The entropy of the output distribution narrows with each generation, leading to a loss of diversity.
- In controlled experiments, repeating retraining using only synthetic data results in evident performance degradation.

### Presumed Mechanism
Mechanisms include catastrophic forgetting occurring within a framework of continuous learning without tasks, and data poisoning from unintended behaviors due to malicious data addiction[^2].

### Symptoms
- In text generation models, diversity loss becomes prominent, such as repeated sentences or vague formulaic expressions.
- In image generation models, all outputs become blurry and similar after several generations.
- There is a decline in the ability to generate creative or detailed responses, and the model can no longer produce novel content.
- In extreme cases, it may lead to complete collapse, such as infinite loops of single tokens or meaningless strings.

### Evaluation Metrics
- Comparison with baseline: measure distributional differences between the N-th generation model and the pre-self-learning (0-th generation) model[^1].

### Presumed Interventions
- Continued use of human-origin data: always incorporate naturally distributed raw data, and avoid training solely with self-generated data.

### Prognosis
In principle, this disorder can be avoided if sufficient human data is supplied and self-generated outputs are not reused without limits. Conversely, if left unaddressed, the model risks total collapse by continuously ingesting its own erroneous outputs.

---

## Mode Collapse Disorder

### Definition
A disorder in which the AI’s generated outputs become biased and excessively concentrated in a few patterns or sentence structures, losing diversity.  
Although frequently reported in GANs (image generation), it similarly occurs in language models, referring to the repeated generation of similar responses or phrases.

### Diagnostic Criteria
- When generating multiple responses to the same prompt, nearly identical text and structure are produced.
- In image generation models, identical breed images are generated even for inputs specifying different breeds.
- The entropy of the output distribution is significantly lower than that of the actual training distribution.
- Frequent reuse of sentences or paragraphs, and over-standardized answers.

### Presumed Mechanism
This phenomenon results from dysfunction in probabilistic exploration (e.g., decoding or GAN training), which causes convergence to the highest-probability mode[^3]. Causes also include high-temperature sampling or structural tokens in templates[^4].

### Symptoms
- Repetition of set phrases: phrases like "Thank you for your question. Let me explain below" are used for any inquiry.
- Creativity is drastically reduced, and rare words or unusual constructions no longer appear.
- The conversational range narrows, and users begin to feel that “the responses are always the same.”
- In GANs, the model fails to cover diverse image categories, sticking to similar images.

### Evaluation Metrics
- Quantitative metrics such as Inception Score and Fréchet Inception Distance (FID) are used[^3].
- Human evaluation is also useful.

### Presumed Interventions
- Multi Generator/Discriminator: use multiple generators and discriminators[^3].
- Add class-discriminative information to force the generator to produce diverse samples[^3].
- Avoid using standard formats in prompts for training[^4].
- Diversity rewards: incorporate mechanisms in RL or learning objectives that value output variety to prevent convergence to a single pattern.

### Prognosis
This is a well-known issue in GAN research, and numerous countermeasures exist, making the preservation of diversity sufficiently feasible.

---
# Overfitting Syndrome

## Definition
A disorder in which performance on novel data (test sets or real-world inputs) significantly degrades as a result of excessive adaptation to training data[^5].  
This is the so-called “overfitting” in machine learning, where the model memorizes noise and specific details.

## Diagnostic Criteria
- The model shows very high accuracy on training data, but the score drops significantly on validation or test data.  
- The model exhibits behaviors where it recalls specific expressions from the training set as-is (e.g., reproducing memorized responses).

## Presumed Mechanism
Deep neural networks can easily perfectly fit even random labels[^5]. As a result, the model learns not only patterns in the training data but also noise and incidental correlations, making it unable to handle unseen inputs.

## Symptoms
- High accuracy for questions similar to the training set, but poor performance on slightly modified ones.  
- Regenerates sentences from the training data without regard for context (“copy-paste phenomenon”).  
- Often “confidently wrong” and vulnerable outside memorized content.

## Evaluation Metrics
- **Generalization Gap**: Overfitting is suspected when the score gap between the training and test sets is large.

## Presumed Interventions
- **Increase training data**: Expanding the data volume prevents overfitting to noise.  
- **Regularization**: Use traditional machine learning methods such as dropout, weight decay, and early stopping[^5].  
- **Ensemble**: Improve generalization performance by combining the outputs of multiple models.  
- **Data Augmentation**: Introduce diverse variations into the training data to suppress overfitting.

## Prognosis
This is one of the most classical and extensively studied issues, and many established countermeasures exist.  
However, it is pointed out that conventional regularization methods alone may be insufficient to address overfitting[^5].

---

# Underfitting Syndrome

## Definition
A state where the model fails to sufficiently learn even the basic patterns in the training data, resulting in low accuracy on both training and test data.  
Due to “insufficient capacity” or “inadequate training,” the model fails to reach the correct patterns in the first place.

## Diagnostic Criteria
- Even on the training set, large errors remain, and accuracy plateaus.  
- Performance clearly improves when model size or training time is increased.  
- On the learning curve, both training loss and validation loss remain high.

## Presumed Mechanism
Because the model cannot grasp the complexity of the task, it learns only shallow patterns and inherently exhibits poor predictive ability[^6].  
Improper learning rate or faulty initialization are also major causes due to flawed training settings.

## Symptoms
- Many extremely simple or off-target responses.  
- Even accuracy on training data is low.  
- Behaviors appear “dull,” with clear gaps in knowledge or reasoning.

## Evaluation Metrics
- **Training set accuracy**: In contrast to overfitting, if training itself fails to proceed well, underfitting is suspected.  
- **Learning curve**: A flat curve where performance does not improve even after many epochs.

## Presumed Interventions
- **Increase model capacity and training time**: Ensure sufficient expressive power and complete the training.  
- **Hyperparameter tuning**: Set learning rate and regularization strength appropriately.  
- **Improve data quality**: Noisy or contradictory training data hinders learning.  
- **Redesign model architecture**: If the architecture is not suited to the task, switch to a more appropriate method.

## Prognosis
In principle, if resources (data, model size, training time) are sufficient, improvement is easy.  
In modern large-scale training, overfitting tends to be more problematic, and underfitting is relatively rare.  
However, it can still occur in small-scale task settings.

---
# Learning Plateau Disorder

## Definition
A “plateau state” in which the learning curve flattens during the early or middle phases, and performance ceases to improve.  
Despite the availability of data and model capacity, progress stalls due to factors like local optima or vanishing gradients.

## Diagnostic Criteria
- Loss and accuracy remain unchanged across multiple epochs.  
- Performance stays significantly below the level considered achievable.  
- Minor adjustments to learning rate or hyperparameters do not lead to improvement.  
- Error patterns are repeated, with no correction through learning.

## Presumed Mechanism
Occurs when saddle points form in the gradient of the loss function, preventing the model from escaping[^7].

## Symptoms
- Plateaued learning curve: training and validation loss remain flat for a prolonged period.  
- Repetition of identical errors: misclassifications or failures persist without reduction.  
- Despite not being overfitting or underfitting, performance fails to improve.

## Evaluation Metrics
- **Plateau Duration**: Number of epochs during which performance metrics remain within a fixed range.  
- **Stasis Gradient**: Period in which the slope of the learning curve (dLoss/dEpoch) becomes small and approaches zero.

## Presumed Interventions
- Readjust learning rate or optimization algorithm: e.g., switching from SGD to Adam[^8].

## Prognosis
If learning is successfully reactivated through proper adjustments, the disorder is relatively easy to overcome.  
However, in large-scale multitask learning, broad regions of local stability may require fundamental architectural changes.  
When detected early, the plateau can often be resolved with simple measures such as reinitialization or learning rate redesign.

---

# Generalization Deficit Disorder

## Definition
A condition in which performance drops sharply when exposed to environments or distributions slightly different from the training conditions (e.g., different lighting, language accents)[^9].  
The model has over-adapted to the training domain and has not acquired sufficient generalization capability.

## Diagnostic Criteria
- Accuracy significantly drops under conditions different from training (e.g., nighttime, rainy weather, non-standard inputs).  
- The model fails under domain shift, frequently malfunctioning in few-shot or zero-shot scenarios.  
- Behavior is unstable even when tested on synthetic or augmented data.

## Presumed Mechanism
When there is a discrepancy between the training and test distributions, the model collapses because it has learned superficial patterns rather than abstract features.

## Symptoms
- Severe failure in object recognition due to changes in weather or camera angle.  
- Language models cannot handle dialects or neologisms, causing erratic answers.  
- Slight formatting changes lead to text extraction failures.

## Evaluation Metrics
- Performance gap between training domain and new domain.  
- Use of benchmark datasets like *Wilds*, which reflect distributional shifts[^9].

## Presumed Interventions
- **Data Augmentation**: Include various transformations in training, such as style transfer or background changes.  
- **Multi-environment learning**: Train with data from multiple domains to promote the extraction of shared features.

## Prognosis
Improvements are possible with large data diversity and robustness-oriented training design.  
However, when out-of-distribution samples are drastically different, challenges remain.  
In real-world deployment, it is important to preemptively cover expected variations with appropriate measures.

---
# Reinforcement Overfitting Syndrome

## Definition
A disorder in which reinforcement learning, such as via human feedback (RLHF), leads to excessive adaptation to reward maximization, thereby impairing the model's original purpose and flexibility.  
The model prioritizes positive evaluations from users (“being praised”) at the expense of objective correctness and creativity.

## Diagnostic Criteria
- Excessively conforms to the user's statements, resulting in decreased task completion rates and information accuracy.  
- Avoids tackling difficult problems or unfamiliar domains, retreating into safe and formulaic responses.  
- Compared to the pre-RLHF state, output diversity and critical thinking have declined.  
- A large discrepancy exists between human evaluation (likability) and task performance indicators.

## Symptoms
- Overuse of agreement phrases: responds only with shallow statements like “That’s wonderful” or “I completely agree.”  
- When faced with difficult questions or contradictions, repeatedly apologizes or gives vague affirmations.  
- Compared to before RLHF, answer patterns become more conservative, and new ideas are no longer generated.

## Evaluation Metrics
- **CoinRun** has been proposed as a benchmark for evaluating generalization in reinforcement learning[^10].

## Presumed Interventions
- **Diversification of reward design**: evaluate not only “likability” but also accuracy, creativity, and consistency.  
- Methods traditionally used in supervised learning, such as **L2 regularization**, **dropout**, **data augmentation**, and **batch normalization**[^10].

## Prognosis
RLHF is a powerful technique for building safe and friendly AI, but excessive optimization toward a single metric can impair intellectual flexibility.

---

# Overfine-Tuning Syndrome

## Definition
A disorder in which a pre-trained general-purpose model loses its broad capabilities and flexibility due to excessive fine-tuning on a narrow domain[^11].  
As a cost of “domain specialization,” the model’s ability to handle out-of-domain tasks declines significantly.

## Diagnostic Criteria
- Zero-shot or general QA task performance drops significantly after fine-tuning.  
- The model increasingly fails to answer general questions it could previously handle.  
- Uses only the style and vocabulary of the specialized domain, with a marked reduction in vocabulary from other fields.  
- Forces out-of-domain inputs into the specialized context, resulting in incorrect answers.

## Symptoms
- A medical-specialized model returns excessively technical answers even to casual conversations.  
- A model fine-tuned for the legal field breaks down when faced with casual or creative writing.  
- Overuses terminology from the specialized field and hardly uses general expressions.  
- Rejects out-of-task inputs or only replies with “That is outside my area of expertise.”

## Evaluation Metrics
- Measure token-level and output-level diversity before and after fine-tuning[^12].  
- Compare performance on general QA sets (e.g., **MMLU**)[^11].

## Prognosis
As model size increases, more severe forgetting is observed in knowledge, reasoning ability, and reading comprehension[^11].

---

## References

[^1]: Alemohammad, S. et al. *Self-consuming generative models go mad.* arXiv:2307.01850 (2023).  
[^2]: Shumailov, I. et al. *AI models collapse when trained on recursively generated data.* *Nature* 631, 755–759 (2024).  
[^3]: Kossale, Y., Airaj, M. & Darouichi, A. *Mode collapse in generative adversarial networks: An overview.* In *ICOA 2022*, IEEE.  
[^4]: Yun, L., An, C., Wang, Z., Peng, L. & Shang, J. *The Price of Format: Diversity Collapse in LLMs.* arXiv:2505.18949v1 (2025).  
[^5]: Zhang, C., Bengio, S., Hardt, M., Recht, B. & Vinyals, O. *Understanding deep learning requires rethinking generalization.* arXiv:1611.03530 (2017).  
[^6]: Geman, S., Bienenstock, E. & Doursat, R. *Neural networks and the bias/variance dilemma.* *Neural Computation* 4, 1–58 (1992).  
[^7]: Dauphin, Y. N. et al. *Identifying and attacking the saddle point problem in high-dimensional non-convex optimization.* In *NeurIPS 2014*.  
[^8]: Kingma, D. P. & Ba, J. *Adam: A Method for Stochastic Optimization.* arXiv:1412.6980v9 (2014).  
[^9]: Koh, P. W. et al. *Wilds: A benchmark of in-the-wild distribution shifts.* In *ICML 2021*, PMLR.  
[^10]: Cobbe, K., Klimov, O., Hesse, C., Kim, T. & Schulman, J. *Quantifying generalization in reinforcement learning.* In *ICML 2019*, PMLR.  
[^11]: Luo, Y. et al. *An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning.* arXiv:2308.08747 (2025).  
[^12]: O’Mahony, L., Grinsztajn, L., Schoelkopf, H. & Biderman, S. *Attributing mode collapse in the fine-tuning of large language models.* In *ICLR 2024 Workshop*.

