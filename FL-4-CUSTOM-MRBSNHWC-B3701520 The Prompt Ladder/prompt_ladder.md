# FL-4: The Prompt Ladder

**Target Task:** Drafting the "Literature Review" section for a Scopus-indexed academic paper (from FL-01 Audit).

## Baseline Prompt (Version 0)
**Prompt:** "Tolong buatkan literature review tentang Federated Learning untuk paper saya."
**Simulated Output Excerpt:** "Federated Learning (FL) adalah konsep machine learning desentralisasi yang diperkenalkan oleh Google pada tahun 2017. FL memungkinkan model untuk dilatih... [3 paragraf penjelasan dasar FL yang sangat umum]."
**Notes:** 
- *What changed:* (Baseline)
- *What improved:* Nothing, this is the baseline.
- *What still failed:* It explains basic concepts like I'm a high school student. It has no citations, no specific focus, and is entirely unusable for a Q2 Scopus journal.
- *What I'll try next:* Add a specific role and audience.

## Iteration 1: Adding Role & Audience
**Prompt:** "Act as a postdoctoral computer science researcher writing for a Q2 Scopus journal. Write a literature review about Federated Learning."
**Simulated Output Excerpt:** "Recent advancements in decentralized machine learning have propelled Federated Learning (FL) to the forefront of privacy-preserving computation (McMahan et al., 2017). The paradigm shifts the training locus..."
**Notes:** 
- *What changed:* Added Role (postdoctoral researcher) and Audience (Q2 Scopus journal).
- *What improved:* The tone shifted immediately. It sounds academic, uses higher-level vocabulary ("paradigm", "locus"), and stopped explaining what FL is to a beginner.
- *What still failed:* It's hallucinating generic citations and talking about FL generally. It doesn't know my specific research focus (Non-IID data in Medical Imaging).
- *What I'll try next:* Add specific context and research goals.

## Iteration 2: Adding Context & Goal
**Prompt:** "Act as a postdoctoral computer science researcher writing for a Q2 Scopus journal. Write a literature review about Federated Learning. Focus specifically on the challenge of Dirichlet Non-IID data distributions in medical imaging classification."
**Simulated Output Excerpt:** "The efficacy of Federated Learning in healthcare is heavily bottlenecked by statistical heterogeneity, particularly Non-Independent and Identically Distributed (Non-IID) data. In medical imaging, data across distinct clinical institutions often follows a Dirichlet distribution..."
**Notes:** 
- *What changed:* Added Context (Non-IID data, medical imaging).
- *What improved:* The content is now highly relevant to my actual research. It's discussing the exact bottleneck (statistical heterogeneity).
- *What still failed:* It's making up broad claims without synthesizing specific papers. It lacks real academic structure (grouping by methodology).
- *What I'll try next:* Add constraints (no hallucinated citations, specific input data).

## Iteration 3: Adding Constraints & Input Data
**Prompt:** "Act as a postdoctoral computer science researcher writing for a Q2 Scopus journal. Write a literature review about Federated Learning focusing on Dirichlet Non-IID data in medical imaging. Constraint: DO NOT hallucinate citations. Only synthesize the following three findings I provide: 
1. Zhao et al. (2018) proved accuracy drops by 11% on highly skewed Non-IID CIFAR-10. 
2. Li et al. (2020) proposed FedProx to handle statistical heterogeneity by adding a proximal term. 
3. My previous paper (Riyadi, 2025) showed FedProx struggles with Dirichlet alpha < 0.1 in MRI datasets."
**Simulated Output Excerpt:** "The degradation of model performance under statistical heterogeneity remains a critical challenge. Initial studies by Zhao et al. (2018) demonstrated an 11% accuracy reduction in highly skewed Non-IID settings. To mitigate this, Li et al. (2020) introduced FedProx, which constrains local updates via a proximal term. However, recent evaluations (Riyadi, 2025) indicate that FedProx's efficacy diminishes significantly in medical imaging domains—specifically MRI datasets—when the Dirichlet distribution is highly skewed (alpha < 0.1)."
**Notes:** 
- *What changed:* Provided actual data points and a strict constraint against hallucination.
- *What improved:* The output is now a factual, logically flowing synthesis of my exact notes. It perfectly connected the three papers into a single narrative thread.
- *What still failed:* It's just one paragraph. I need it formatted into specific subsections for the paper draft.
- *What I'll try next:* Add output formatting requirements.

## Iteration 4: Adding Output Format (The "Made it Worse" moment)
**Prompt:** "[...all previous text...] Output format: Write this as a 5-page JSON object where each key is a paragraph and the values are arrays of sentences."
**Simulated Output Excerpt:** `{ "paragraph_1": ["The degradation...", "Initial studies..."], "paragraph_2": [...] }`
**Notes:** 
- *What changed:* Forced the output into a JSON format.
- *What improved:* It followed the formatting constraint perfectly.
- *What still failed:* **This made it worse.** By forcing JSON, I lost the natural academic flow and transition words between paragraphs. I also can't easily paste this into Microsoft Word or LaTeX. It was a useless technical constraint that degraded the writing quality.
- *What I'll try next:* Remove JSON, use Markdown step-decomposition instead.

## Iteration 5 (Final): Step Decomposition & Markdown
**Prompt:** "Act as a postdoctoral computer science researcher writing for a Q2 Scopus journal. Your task is to write a literature review on Federated Learning (Dirichlet Non-IID in Medical Imaging). 
Do this in two steps:
Step 1: Group the following 3 findings into two distinct themes: 'The Impact of Non-IID Data' and 'Algorithmic Mitigations'.
Step 2: Write two separate Markdown paragraphs under those headers, synthesizing the findings. 
Constraint: No hallucinated citations. Use ONLY these findings: 
1. Zhao et al. (2018): 11% accuracy drop on Non-IID. 
2. Li et al. (2020): FedProx adds proximal term. 
3. Riyadi (2025): FedProx fails on MRI with Dirichlet alpha < 0.1."
**Simulated Output Excerpt:** 
"### The Impact of Non-IID Data
The degradation of model performance under statistical heterogeneity is a well-documented challenge in decentralized training. Specifically, Zhao et al. (2018) demonstrated...
### Algorithmic Mitigations
To address these distributional skews, regularization techniques have been widely adopted. Li et al. (2020) proposed FedProx... However, Riyadi (2025) established that..."
**Notes:** 
- *What changed:* Used step decomposition (Step 1 group, Step 2 write) and Markdown headers.
- *What improved:* The output is perfectly structured, highly academic, mathematically accurate, and ready to be pasted directly into a LaTeX document.

---

## Final Reusable Prompt Template
```text
Act as a postdoctoral computer science researcher writing for a [INSERT JOURNAL TIER/NAME]. 
Your task is to write a literature review on [INSERT TOPIC].

Do this in two steps:
Step 1: Group the provided findings logically into themes.
Step 2: Write separate Markdown paragraphs under thematic headers, synthesizing the findings.

Constraints: 
- DO NOT hallucinate citations. 
- Maintain a highly objective, academic tone.
- Synthesize ONLY the following findings:
[INSERT BULLET POINTS OF YOUR PAPER NOTES/FINDINGS HERE]
```
