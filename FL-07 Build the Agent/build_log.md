# FL-07: Build Log

## 1. Goal
To build the "Research Scout" agent designed in FL-06. The agent must successfully complete its core job (searching academic papers and checking for code) end-to-end, connecting to at least one real external data source.

## 2. Iteration Log & Deviations from Spec
- **Initial Setup:** I decided to build the agent as a local Python script utilizing API calls to simulate the exact Custom GPT workflow. This provides better control over the terminal output for the screen capture requirement.
- **Tool 1 (arXiv API):** Integrated the arXiv API. *Hurdle:* arXiv uses the Atom XML format, not standard JSON. *Fix:* Used Python's built-in `xml.etree.ElementTree` to parse the namespaces correctly.
- **Tool 2 (GitHub API):** Integrated GitHub's search API. *Deviation:* I initially planned to scrape the actual paper URL for a "code" badge, but that was too brittle. I pivoted to using the GitHub Search API querying the exact paper title, which is much more reliable and fits the 10-hour build limit.
- **Guardrail Check:** Kept the scope extremely narrow. The agent successfully skips trying to read full PDFs (which often hits paywalls or rate limits) and strictly parses open-access abstracts and metadata.

## 3. End-to-End Run Verification
- The agent correctly parses the user's query ("Federated Learning privacy secure aggregation").
- It fetches the 3 most recent papers from arXiv.
- It parses the XML, extracts the abstract, and searches GitHub for associated repositories.
- It prints the output cleanly to the terminal without hallucinations.
- **The screen capture (raw run) was recorded by executing `python research_scout.py` in the terminal.**
