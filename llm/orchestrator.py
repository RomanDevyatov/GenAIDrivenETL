from pathlib import Path
from llm.client import LLMClient

PROMPTS_DIR = Path("prompts")
OUTPUT_DIR = Path("pipelines/generated")

class ETLOrchestrator:
    def __init__(self):
        self.llm = LLMClient()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def load_prompt(self, name):
        return (PROMPTS_DIR / name).read_text()

    def generate_sql(self, raw_schema, rules):
        prompt = self.load_prompt("transformation_generation.txt").format(
            raw_schema=raw_schema,
            business_rules=rules
        )

        sql = self.llm.generate(prompt)

        path = OUTPUT_DIR / "etl.sql"
        path.write_text(sql)
        return path

    def generate_tests(self, sql_logic):
        prompt = self.load_prompt("test_generation.txt").format(
            sql_logic=sql_logic
        )

        tests = self.llm.generate(prompt)

        Path("tests/generated_tests.py").write_text(tests)
