import argparse
import duckdb
import os

DB_PATH = 'data/db/Car_Inventory.duckdb'
TABLE_NAME = "car_inventory"

def ingest_csv(con, csv_path, table_name):
    """Upsert CSV data into DuckDB table using VIN as the primary key.
    Handles schema changes by adding new columns automatically."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    # Check if the table exists
    table_exists = con.sql(
        f"SELECT count(*) FROM information_schema.tables WHERE table_name = '{table_name}'"
    ).fetchone()[0] > 0

    if not table_exists:
        con.sql(f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{csv_path}')")
    else:
        con.sql(f"CREATE TEMP TABLE staging AS SELECT * FROM read_csv_auto('{csv_path}')")

        table_cols = set(row[0] for row in con.sql(f"DESCRIBE {table_name}").fetchall())
        staging_cols = set(row[0] for row in con.sql("DESCRIBE staging").fetchall())
         # Add new columns from CSV that don't exist in the table
        for col in staging_cols - table_cols:
            col_type = con.sql(f"SELECT typeof({col}) FROM staging LIMIT 1").fetchone()[0]
            con.sql(f"ALTER TABLE {table_name} ADD COLUMN {col} {col_type}")

        # Upsert: delete matching VINs, then insert
        con.sql(f"DELETE FROM {table_name} WHERE vin IN (SELECT vin FROM staging)")
        con.sql(f"INSERT INTO {table_name} SELECT * FROM staging")
        con.sql("DROP TABLE staging")

    print(f"Ingested {csv_path} into '{table_name}'")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    args = parser.parse_args()

    con = duckdb.connect(DB_PATH)
    try:
        ingest_csv(con, args.csv_path, TABLE_NAME)
    finally:
        con.close()

if __name__ == "__main__":
    main()