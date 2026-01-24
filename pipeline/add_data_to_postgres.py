import pandas as pd
from sqlalchemy import create_engine

# Read Parquet
df = pd.read_parquet("/Users/zhouwu/Documents/Data Engineer/Docker/Data-ZoomCamp---Docker-Workshop/pipeline/yellow_tripdata_2025-11.parquet")

# Connect to Postgres
engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi", future=True)

# Write to Postgres safely
with engine.begin() as connection:
    df.to_sql("yellow_trip_data_2025_11", connection, if_exists="replace", index=False, chunksize=100000)
