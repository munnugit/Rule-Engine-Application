import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost:5432/rule_engine")
