from sqlalchemy import create_engine
from decouple import config

# Specify the driver in the connection string
engine = create_engine(
    f"postgresql+psycopg2://{config('DB_USER')}:{config('DB_PASSWORD')}@"
    f"{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_DB')}"
)

def connection():
    return engine