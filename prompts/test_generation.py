You are a data quality engineer.

Given this ETL logic:
{sql_logic}

Generate pytest tests that validate:

- no null session_id
- session_end >= session_start
- revenue >= 0
- no duplicate sessions
