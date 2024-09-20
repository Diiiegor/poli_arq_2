from sqlalchemy.orm import Session

from src.models.inventory import Inventory
from src.requests.enter_product import EnterProduct


class InventoryController:
    def enter_product(self, payload: EnterProduct, db: Session):
        try:
            product_id = payload.id
            quantity = payload.quantity
            inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()

            if inventory:
                inventory.stock += quantity
            else:
                inventory = Inventory(product_id=product_id, stock=quantity)
                db.add(inventory)

            db.commit()
            db.refresh(inventory)
            return inventory
        except Exception as e:
            return {"error": "Invalid product id"}
