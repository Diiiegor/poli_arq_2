from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.controllers.inventory_controller import InventoryController
from src.controllers.product_controller import ProductController
from src.core.database import get_db
from src.requests.enter_product import EnterProduct

router = APIRouter(prefix="/api")
product_controller = ProductController()
inventory_controller = InventoryController()


@router.get("/product/{id}")
def show_product(id: int, db: Session = Depends(get_db)):
    return product_controller.show_product(id, db)


@router.get("/products")
def products(db: Session = Depends(get_db)):
    return product_controller.products(db)


@router.post("/enter-product")
def enter_product(payload: EnterProduct, db: Session = Depends(get_db)):
    return inventory_controller.enter_product(payload, db)
