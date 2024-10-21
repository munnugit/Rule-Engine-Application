from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Rule(Base):
    __tablename__ = "rules"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    rule_ast = Column(JSON, nullable=False)
