# ML-07: Baseline Action Score and Top-10 Review

## What We Did
In this task (Focus: *Core Lane 2 - Content Refresh Opportunity*), we built a **transparent, human-readable baseline rule** to detect web pages that are experiencing a decline in performance.

The steps taken were:
1. **Signal Audit (EDA):** We tested two main signals against the proxy label for traffic decline (`trend_direction == 'down'`).
2. **Building the Baseline Rule:** We created a manual scoring formula without using Machine Learning.
3. **Building the Ranked Queue:** We sorted the pages from highest to lowest priority and saved them into a CSV file (`work/outputs/baseline_action_score.csv`).

## The Baseline Rule
The manual rule we created is:
> "Flag a page for review if it is stale (**>180 days since the last update**), historically still has search visibility (**>500 impressions in the last 90 days**), but suffers from very poor engagement (**CTR < 2.0%**)."

For pages that meet all three conditions, their score is multiplied by their total impressions (`impressions_90d`) so that pages with the biggest traffic potential are ranked first.

Flagged pages are assigned:
* **Action Label:** `review_for_refresh`
* **Reason Code:** `stale_high_volume_low_ctr`

## The Results
The outcome of this Baseline Rule is highly satisfying:
* Out of approximately 30,000 rows of data, this manual rule successfully filtered and selected exactly **17 critical pages** that need a content refresh.
* **High Precision:** Out of the 17 flagged pages, **16 of them are proven to be actively declining in traffic** (based on the `is_declining` proxy label).
* This results in a **Precision@17 of ~94.1%**.

Achieving 94% precision using only a static rule (If-Else) proves that our business logic is correct and the chosen signals are extremely strong. This exact metric will serve as the **Baseline** that our future Machine Learning algorithms must beat in the upcoming weeks.
