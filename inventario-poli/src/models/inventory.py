from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Base


class Inventory(Base):
    __tablename__ = 'inventory'

    product_id = Column(Integer,ForeignKey('products.id'), primary_key=True, autoincrement=False)
    stock = Column(Integer)
    product = relationship("Product", back_populates="inventory")

