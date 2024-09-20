from sqlalchemy.orm import Session, joinedload

from src.models.product import Product


class ProductController:

    def show_product(self, id: int, db: Session) -> dict:
        product = db.query(Product).options(joinedload(Product.inventory)).filter(Product.id == id).first()
        return product

    def products(self, db: Session):
        products = db.query(Product).options(joinedload(Product.inventory)).all()
        return products
