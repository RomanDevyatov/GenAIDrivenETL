from pathlib import Path

from genaidrivenetl.config import Config

SQL_PATH = Path(Config.GENERATED_SQL_PATH)
GEN_TEST_PATH = Path(Config.GENERATED_TESTS_PATH)


def save_sql(sql: str) -> str:
    SQL_PATH.write_text(sql)
    return sql


def read_gen_sql() -> dict:
    return SQL_PATH.read_text()


def save_raw_tests(tests: str) -> str:
    GEN_TEST_PATH.write_text(tests)
    return tests
