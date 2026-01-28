# GenAI-Driven ETL Workflow Generator

This project demonstrates a GenAI-powered ETL system that converts natural language business rules into:

- Data warehouse schema
- SQL transformations
- Automated data quality tests

## Features

- LLM-generated ETL pipelines
- Postgres execution
- Automated validation
- Test generation

## GenAI Usage

- Schema modeling from business rules
- SQL transformation generation
- Test automation

## Stack

Python, PostgreSQL, LLM API, pytest

## Run

1. Start Postgres
2. Load sample data
3. Run pipeline:

```bash
python run_pipeline.py
pytest
