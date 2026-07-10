# FL-02: Prompting Fundamentals (Cross-Model Comparison)

*Note: The detailed iteration log (Baseline to Version 5) is documented in the FL-4 Prompt Ladder task. This document presents the final prompt and the cross-model evaluation.*

## Final Reusable Prompt Template
```text
Act as a postdoctoral computer science researcher writing for a Q2 Scopus journal. 
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

## Cross-Model Comparison (Claude vs. ChatGPT)

When running the final optimized prompt above on the exact same set of findings, the models exhibited distinctly different stylistic choices:

1. **Tone and Academic Rigor:**
   - **Claude (3.5 Sonnet):** Claude's output felt noticeably more "human-academic." It used nuanced transition phrases (e.g., "While regularization provides a baseline, recent evaluations suggest...") and felt less robotic. It strictly adhered to the "no hallucination" rule.
   - **ChatGPT (GPT-4o):** ChatGPT was highly structured but felt slightly more mechanical. It tended to overuse certain academic transition clichés (e.g., "Furthermore," "Moreover"). However, it was exceptionally good at formatting the Markdown headers exactly as requested.

2. **Structure and Constraint Adherence:**
   - Both models perfectly executed the Step 1 (grouping) and Step 2 (writing) decomposition.
   - **Failure Point (ChatGPT):** ChatGPT occasionally tried to add a concluding summary paragraph that wasn't strictly asked for, slightly violating the "Synthesize ONLY the following findings" constraint by adding external generic fluff at the end.
   - **Failure Point (Claude):** Claude occasionally merged two thematic headers into one if it felt the findings were too similar, which technically violated the rigid structure but made for a better-flowing paper.

**Conclusion:** For drafting academic literature reviews where strict adherence to provided notes is required (to avoid plagiarism/hallucination), **Claude** is the slightly better model due to its superior natural academic tone and strict adherence to negative constraints (not adding fluff).
