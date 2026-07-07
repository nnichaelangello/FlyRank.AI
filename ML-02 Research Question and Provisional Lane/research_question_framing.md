# Research Question Framing

## 1. Selected Lane
**Core Lane 2: Refresh / Content Opportunity Scoring**

## 2. Search/Discoverability Question
Which existing visible pages are showing early signs of decline or underperformance and should be prioritized for a content refresh or metadata review?

## 3. Unit of Analysis
The unit of analysis is a single pseudonymized content item (page) over a defined time window.

## 4. Output
The output will be a ranked review queue (a list of pages) sorted by an opportunity/risk score, accompanied by transparent reason codes (e.g., "declining with demand", "stale visible page") and confidence labels.

## 5. Action
A content strategist or SEO reviewer can use this ranked queue to decide which pages to manually inspect and update first. Actions might include rewriting outdated content, improving metadata, expanding sections to better match search intent, or simply monitoring the page further.

## 6. Cost of a Wrong Recommendation
If the model falsely identifies a healthy page as declining (False Positive), the cost is wasted human review time—a reviewer might spend 15-30 minutes investigating a page that doesn't need changes. If the model misses a truly declining high-value page (False Negative), the cost is lost potential traffic and revenue over time. Since this is a decision-support tool rather than fully automated editing, the risks are bounded by human review capacity.

## 7. Why Data/ML Can Help
The problem is not just "training a model" but managing scale and limited human capacity. A site with tens of thousands of pages cannot be manually audited every month. While simple rules (e.g., "all pages older than 1 year") can catch obvious stale content, they often miss pages that are actively losing rank despite being recently updated, or they flag pages that are old but still perfectly capturing all available demand. Using historical engagement and search signals allows us to build a more nuanced, evidence-backed prioritization system that surfaces the most critical opportunities first, making human reviewers much more efficient.
