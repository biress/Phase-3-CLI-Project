import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import Base, Customer, Table
from app.database import engine, SessionLocal

Base.metadata.create_all(engine)
session = SessionLocal()

# Add sample tables
tables = [Table(table_number=i, capacity=4) for i in range(1, 6)]
session.add_all(tables)
session.commit()
