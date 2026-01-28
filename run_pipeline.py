from llm.orchestrator import ETLOrchestrator

RAW_SCHEMA = """
raw_events(
 user_id text,
 event_time timestamp,
 event_type text,
 session_id text,
 revenue numeric,
 user_agent text
)
"""

BUSINESS_RULES = """
Create sessions after 30 minutes inactivity.
Exclude bots.
Revenue only from purchase events.
"""

def main():
    orchestrator = ETLOrchestrator()
    sql_file = orchestrator.generate_sql(RAW_SCHEMA, BUSINESS_RULES)
    print("Generated SQL at:", sql_file)

    sql_logic = sql_file.read_text()
    orchestrator.generate_tests(sql_logic)
    print("Generated tests.")

if __name__ == "__main__":
    main()
