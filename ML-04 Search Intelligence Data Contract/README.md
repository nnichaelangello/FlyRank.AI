# ML-04 Search Intelligence Data Contract

## Overview
This task establishes a robust Data Contract for predicting Content Refresh Opportunities (Core Lane 2). The goal is to define the exact analytical grain, time window, and target label while strictly avoiding "data leakage" (the trap of using future information to predict past states).

## What We Did
1. **Defined the Data Contract**: Specified the grain as `report_date` × `client_hash_id` × `content_hash_id` using the `fact_content_daily_performance` table for the mid-panel month of March 2026.
2. **Verified with Data**: Used DuckDB to connect to the Hugging Face data warehouse and ran queries to prove the grain is unique, display the exact date span, and verify the total row counts.
3. **Designed Safe Features**: Built a 5-feature data frame (`impressions_90d`, `clicks_90d`, `avg_position`, `sessions_90d`, and `engagement_time`) ensuring every feature is "knowable at the decision moment" and aggregated from historical windows.
4. **Demonstrated the Leakage Trap**: Created a deliberate data leak experiment in Python to show how using future metrics artificially inflates model accuracy, and documented the process of removing it to restore honesty.

## Results
- The notebook (`w03_data_contract.ipynb`) successfully executed all DuckDB verification queries.
- A clean, 5-row preview of the feature frame was successfully generated.
- The data contract is verified, honest, and ready for use in subsequent modeling phases.
