import logging

from dotenv import load_dotenv

from genaidrivenetl.config import Config
from genaidrivenetl.llm.factory import build_llm
from genaidrivenetl.logging_config import setup_logging
from genaidrivenetl.pipeline.pipeline import build_pipeline

logger = logging.getLogger(__name__)


load_dotenv()
Config.ensure_directories()
setup_logging()


def run_pipeline():
    llm = build_llm(
        Config.LLM_MODEL,
        Config.OPENROUTER_API_KEY,
        Config.OPENROUTER_BASE,
    )

    pipeline = build_pipeline(llm)

    try:
        pipeline.invoke({})
    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")

    logger.info(f"Pipeline: {pipeline}")


if __name__ == "__main__":
    run_pipeline()
