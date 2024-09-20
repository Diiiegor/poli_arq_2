from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Mapped, relationship

from src.core.database import Base
from src.models.inventory import Inventory


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(Text)
    image = Column(String)
    inventory = relationship("Inventory", back_populates="product", uselist=False)

