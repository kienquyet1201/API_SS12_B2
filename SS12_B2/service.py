from sqlalchemy.orm import Session
from models import OrderModel

def get_order_by_id(db: Session, order_id: int):
    return db.query(OrderModel).filter(OrderModel.id == order_id).first()