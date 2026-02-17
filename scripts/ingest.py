import duckdb

con = duckdb.connect('data/db/my_db.duckdb')
con.sql("CREATE TABLE car_inventory AS SELECT * FROM read_csv_auto('data/raw/cars_data_1.csv')")
con.close()