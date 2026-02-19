# Lendbuzz Home Assignment

## Overview
This project implements a local data platform using Python and DuckDB for data ingestion, and dbt for transformations. The goal is to process car inventory data through various stages of schema changes and updates.


## Setup
```bash
# Create and activate virtual environment
python -m venv env
source env/Scripts/activate   # Windows (Git Bash)
# source env/bin/activate     # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

## 1. Data Ingestion

### 1.a. Initialization
```bash
python scripts/ingest.py
```
### 1.b. Upsert
Refactored the script to accept a CSV path as argument and support upsert logic (using VIN as the unique key).
```bash
python scripts/ingest.py data/raw/cars_data_2.csv
```

### 1.c Schema Change
Refactored the script to detect new columns in the CSV that don't exist in the table.
Missing columns are added automatically via `ALTER TABLE` before upserting.
```bash
python scripts/ingest.py data/raw/cars_data_3.csv
```

## 2. Data Transformation

### 2.a. dbt Setup
Initialized a dbt project (`lendbuzz_dbt`) with the DuckDB adapter. The `profiles.yml` is stored inside the repo and points to the existing DuckDB database.


## Time Log
| Task | Time Spent |
|------|------------|
| 1.a. Initialization | 2 hours |
| 1.b. Upsert | 45 min |
| 1.c. Schema Change | 25 min |
| 2.a. dbt Setup | 1.5 hours |
| 2.b. Data Modeling | 2 hours |
| 2.c. Data Testing | |
