import logging

from dotenv import load_dotenv
from llm.orchestrator import ETLOrchestrator

from genaidrivenetl.config import (
    AGGREGATES,
    FIXTURE_NAME,
    RAW_SCHEMA,
    REQUIRED_CHECKS,
    RULES,
    RULES_TEST,
    USER_METRICS_STAGING_VIEW_NAME,
)
from genaidrivenetl.logging_config import setup_logging

logger = logging.getLogger(__name__)


load_dotenv()
setup_logging()


def main():
    orchestrator = ETLOrchestrator()
    generated_sql_file_path = orchestrator.generate_sql(
        RAW_SCHEMA, USER_METRICS_STAGING_VIEW_NAME, RULES, AGGREGATES
    )

    sql_logic = generated_sql_file_path.read_text()
    orchestrator.generate_tests(
        sql_logic,
        USER_METRICS_STAGING_VIEW_NAME,
        FIXTURE_NAME,
        REQUIRED_CHECKS,
        RULES_TEST,
    )


if __name__ == "__main__":
    main()
