# ML-08 Capstone Modeling Lane

## Overview
This task represents the culmination of the modeling phase for Lane 2 (Content Refresh Opportunity). Moving beyond the simple rule-based baseline established in Week 4, we built an "honest" Machine Learning model to better predict which content pages are at risk of declining traffic, allowing the business to prioritize refreshes effectively.

## Our Approach
1. **Model Choice**: We utilized a **Random Forest Classifier**. This choice perfectly matches the "Which first?" ranking problem by outputting reliable probabilities. It naturally handles non-linear interactions (e.g., how CTR relates to Impressions) and provides excellent interpretability through permutation importance without being overly complex.
2. **Honest Validation**: To strictly prevent data leakage, we implemented a `GroupShuffleSplit` on `client_id` (80% Train, 20% Test). This ensures the model learns generalizable signals rather than memorizing client-specific structural artifacts.
3. **Apples-to-Apples Comparison**: We evaluated both our new Random Forest model and the exact ML-07 Baseline Rule on the *same test split* using the *same metric* (**Precision@50**).

## Results
The model successfully competed against the baseline. By utilizing permutation importance on the test set, we were able to isolate the most critical drivers of content decline and verify that no "suspiciously perfect" future features leaked into our training data. Furthermore, an error analysis on the top False Positives helped us identify edge cases (such as structurally static pages) that trick the model, paving the way for future feature engineering.

## Deliverables
- `w05_model.ipynb`: The executed notebook containing the rationale, split design, training code, baseline comparison table, and error interpretation.
