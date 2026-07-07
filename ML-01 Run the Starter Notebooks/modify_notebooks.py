import json
import sys

def modify_notebook(path, target_string, new_source):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            if target_string in source:
                cell['source'] = new_source
                break

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
        f.write('\n')

modify_notebook(
    'flyrank-ml-internship-starter/notebooks/01_first_look_and_discovery.ipynb',
    '# Your discovery here',
    [
        "# Your discovery here\n",
        "df_pos = df[df[\"impressions_90d\"] > 0]\n",
        "corr_pos = df_pos[\"search_volume\"].corr(df_pos[\"impressions_90d\"])\n",
        "print(f\"Correlation between search_volume and impressions_90d (impressions > 0): {corr_pos:.3f}\")\n",
        "print(\"Directionally, it might be slightly higher but likely still very weak, showing search volume isn't the whole story.\")\n"
    ]
)

modify_notebook(
    'flyrank-ml-internship-starter/notebooks/02_your_first_readable_model.ipynb',
    '# Your experiment here',
    [
        "# Your experiment here\n",
        "tree_d3 = DecisionTreeClassifier(max_depth=3, class_weight=\"balanced\", random_state=42)\n",
        "tree_d3.fit(X, y)\n",
        "tree_d3_score = tree_d3.predict_proba(X)[:, 1]\n",
        "print(\"Depth 3 Tree:\")\n",
        "print(export_text(tree_d3, feature_names=features))\n",
        "tr_d3 = precision_at_k(tree_d3_score, y, 50)\n",
        "print(f\"Precision@50 with max_depth=3: {tr_d3:.3f}\")\n"
    ]
)
