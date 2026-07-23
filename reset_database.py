from database import engine
from models import Base

print("Resetting database...")

Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

print("Database reset completed!")