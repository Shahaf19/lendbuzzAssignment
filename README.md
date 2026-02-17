# Lendbuzz Home Assignment

## Overview
This project implements a local data platform using Python and DuckDB for data ingestion, and dbt for transformations. The goal is to process car inventory data through various stages of schema changes and updates.


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
## Time Log
| Task | Time Spent |
|------|------------|
| 1.a. Initialization | 2 hours |
| 1.b. Upsert | 45 min |
| 1.c. Schema Change | |
| 2.a. dbt Setup | |
| 2.b. Data Modeling | |
| 2.c. Data Testing | |
