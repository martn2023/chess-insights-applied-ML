from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    # FK to countries table
    country_code = Column(String, ForeignKey("countries.code"))

    # Relationships
    country = relationship("Country", back_populates="players")
