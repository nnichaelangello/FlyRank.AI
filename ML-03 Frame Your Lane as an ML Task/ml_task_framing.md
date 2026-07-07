# ML Task Framing

## 1. Selected Lane
**Core Lane 2: Refresh / Content Opportunity Scoring**

## 2. ML Task Type
**Scoring and Ranking**. The system will output a probability or opportunity score for each page, which will be used to rank the pages from highest priority to lowest priority.

## 3. Target / Proxy
The proxy target is whether a page is experiencing a meaningful decline in search performance. In the starter setup, this is represented by a derived label (e.g., `trend_direction == "down"`). In a more advanced implementation, the target would be a forward-looking window (e.g., a sustained drop in impressions/clicks over the next 30 days compared to the previous 90 days).

## 4. Success Metric
The primary success metric is **Precision@K** (for example, Precision@50). Since human review capacity is limited, the most important question is: "Out of the top 50 pages the model recommends for a refresh, what percentage are actually experiencing a decline?" Secondary metrics like ROC AUC or Average Precision can be used for overall model evaluation, but Precision@K directly measures the business value of the review queue.

## 5. Why ML Beats a Fixed Rule
A fixed rule (e.g., "Flag page IF age > 180 days AND impressions > 500") is brittle. It treats a 181-day-old page exactly the same as a 1000-day-old page, and it cannot easily balance conflicting signals (e.g., an old page that still has excellent engagement vs. a newer page whose traffic is falling off a cliff). Machine Learning can simultaneously weigh dozens of continuous signals—such as exact age, exact traffic volume, engagement rates, and average position—to identify subtle patterns of early decay that a human-written IF/ELSE rule would miss. As seen in the starter notebooks, this capability allows a learned model to achieve a significantly higher Precision@K than a simple hand-written rule.

## 6. Real Content Action
The final output is a ranked queue. A content strategist will take the top K pages from this queue and perform targeted content actions. These actions include rewriting outdated sections, updating statistics, optimizing meta titles for better click-through rates, or expanding the content to cover new user intents that competitors might be capturing.
