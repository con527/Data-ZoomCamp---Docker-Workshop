from sqlalchemy import create_engine, text  # note the text import

# Connect to Postgres
engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi", connect_args={"connect_timeout": 5})

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(result.fetchall())
except Exception as e:
    print("Connection failed:", e)
