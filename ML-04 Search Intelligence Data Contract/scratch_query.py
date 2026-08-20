import duckdb
con = duckdb.connect()
con.execute("CREATE SECRET (TYPE huggingface, TOKEN 'hf_YOUR_API_KEY_HERE')")
print(con.sql("SELECT * FROM read_parquet('hf://datasets/FlyRank/internship-warehouse/fact_content_daily_performance/month=2026-03/*.parquet') LIMIT 1"))
