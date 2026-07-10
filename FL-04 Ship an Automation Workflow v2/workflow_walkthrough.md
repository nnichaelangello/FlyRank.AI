# FL-04: Ship an Automation Workflow (Literature Review Pipeline)

## The Pipeline Design
I designed a no-code workflow using a **Claude Project (with structured instructions)** to automate the "Source-Grounded Study Notes & Drafting" routine from my FL-01 audit. 

### The 3 Distinct Steps:
1. **Gather & Synthesize (Input):** I feed raw notes, PDF highlights, or raw data from recent academic papers into the project.
2. **Review against Constraints:** The system automatically cross-references the input against my custom instructions (e.g., "Must focus on Federated Learning, no hallucination").
3. **Format & Draft (Output):** The system outputs a strictly formatted Markdown literature review grouped by thematic headers, ready for LaTeX insertion.

## The Claude Project Configuration
**System Prompt / Custom Instructions:**
> "Act as a postdoctoral computer science researcher. Your job is to convert raw reading notes into Q2 Scopus-ready literature review sections.
> Step 1: Analyze the provided raw notes and identify 2-3 common themes.
> Step 2: Write a continuous academic synthesis under thematic Markdown headers.
> Constraint 1: NEVER hallucinate citations. Only use the authors provided in the input.
> Constraint 2: Use an objective, highly technical academic tone."

## The 5 Real Runs (Testing the Pipeline)
1. **Run 1 (FedProx limits):** Fed raw notes on Li (2020) and Zhao (2018). Output successfully grouped them under "Statistical Heterogeneity."
2. **Run 2 (Medical Imaging FL):** Fed notes on MRI Non-IID challenges. Output correctly isolated Dirichlet distribution impacts.
3. **Run 3 (Differential Privacy):** Fed notes on Abadi (2016). The pipeline correctly formatted a standalone privacy paragraph.
4. **Run 4 (YOLOv8 Edge Tracking):** Fed notes on my CCTV architecture. Output grouped under "Real-time Edge Inference."
5. **Run 5 (Federated Averaging Math):** Fed raw mathematical equations. *Output struggled slightly to format the math correctly in plain text without LaTeX wrapping.*

## Time Saved Estimate
- **Manual approach:** Reading notes, grouping themes manually, and writing academic transitions takes me ~45 minutes per section.
- **Workflow approach:** Setup took 15 minutes. Running the pipeline takes 2 minutes. 
- **Time saved:** ~40 minutes per run. For a full 5-section literature review, this saves over 3 hours.

## Known Failure Points & Human Review
- **Failure Point:** If the input notes contain conflicting data (e.g., two papers claiming different baseline accuracies without context), the workflow aggressively merges them, creating confusing sentences.
- **Human Review Required:** A human must ALWAYS verify the final academic transitions and manually wrap mathematical equations in `$$` for LaTeX, as the workflow occasionally outputs plain-text math.
