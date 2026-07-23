from dotenv import load_dotenv
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


# Load environment variables
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not found in .env")

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require"
    },
    pool_pre_ping=True
)


# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for SQLAlchemy models
Base = declarative_base()


# Test connection
def test_connection():

    try:
        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT NOW();")
            )

            print("✅ Database connected successfully")
            print("Server time:", result.fetchone()[0])


    except Exception as e:
        print("❌ Database connection failed.")
        print(e)



# Run the connection test when executed directly
if __name__ == "__main__":
    test_connection()