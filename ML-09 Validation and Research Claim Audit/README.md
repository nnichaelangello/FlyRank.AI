# ML-09: Validation and Research Claim Audit

## Purpose
The primary objective of this project is to apply rigorous scientific standards to the Random Forest model we built during the Week-5 Capstone (`ML-08`). In the real world, a model is only as useful as the honesty of its claims. This notebook (`w06_validation_audit.ipynb`) serves as an audit to ensure our model does not suffer from data leakage, methodology flaws, or exaggerated marketing claims.

## What We Did
1. **Methodology Critique**: We examined hypothetical findings from the FlyRank research paper, questioning where their labels came from (manual vs. historical clicks) and whether their validation design truly prevents structural data leakage.
2. **The "Honest Split" Implementation**: We retrained our own Random Forest model using two different data-splitting techniques:
   - *Naive Split (`train_test_split`)*: Randomly splitting rows.
   - *Honest Split (`GroupShuffleSplit`)*: Grouping the data by `client_id` so the model is tested on completely unseen clients.
3. **Leakage Audit**: We ran a correlation matrix between all features and the target variable (`is_declining`) to ensure the model isn't "cheating" by using a feature that acts as a proxy for the target.
4. **Claim Calibration**: We rewrote our boldest marketing claims into safe, scientifically sound language (using terms like *observed*, *measured*, *directional*, and *decision-support*).

## Findings & Results

### 1. The Danger of Naive Splits (Structural Leakage)
When we ran the experiment, we found a significant gap in performance:
- **BEFORE (Naive Split Accuracy):** `66.58%`
- **AFTER (Honest Split Accuracy):** `57.65%`

**Conclusion:** The naive split artificially inflated our model's performance by almost 9%. Because content from the same client shares structural similarities, randomly splitting rows caused the model to memorize client-specific artifacts (a form of structural data leakage). The *Honest Split* of 57.65% reflects the true generalization capability of the model when deployed to entirely new clients.

### 2. Leakage Audit Results
Our absolute correlation check yielded the following top features:
- `word_count`: 0.118863
- `has_word_count`: 0.090431
- `days_since_last_update`: 0.081383

**Conclusion:** We found zero evidence of trivial target leakage. None of the features showed a suspiciously near-perfect correlation (e.g., > 0.9) with the `is_declining` target. The model is learning from genuine, weak signals rather than a leaked label proxy.

### 3. Final Claim Calibration
Instead of claiming that our model *"accurately predicts exactly which content will decline,"* we have adjusted our scientific stance. The audited claim is now:
> *"Our model provides directional decision-support by measuring content decay indicators. It observes historical trends to help prioritize which articles might benefit from a refresh."*
