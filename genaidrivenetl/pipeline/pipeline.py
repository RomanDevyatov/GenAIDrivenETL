from langchain_core.runnables import RunnableLambda

from genaidrivenetl.config import Config
from genaidrivenetl.infrastructure.file_storage import (
    save_raw_tests,
    save_sql,
)
from genaidrivenetl.pipeline.chains import build_chain
from genaidrivenetl.pipeline.inputs import (
    prepare_gen_sql_inputs,
    prepare_gen_test_inputs,
)


def build_pipeline(llm):
    gen_sql_chain = build_chain(llm, Config.SQL_PROMPT_PATH)
    gen_test_chain = build_chain(llm, Config.TEST_PROMPT_PATH)

    return (
        RunnableLambda(prepare_gen_sql_inputs)
        | gen_sql_chain
        | RunnableLambda(save_sql)
        | RunnableLambda(prepare_gen_test_inputs)
        | gen_test_chain
        | RunnableLambda(save_raw_tests)
    )
