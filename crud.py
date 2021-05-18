from sqlalchemy import update
from sqlalchemy.orm import Session
import models


def get_suppliers(db: Session):
    return db.query(models.Shipper).order_by(models.Shipper.ShipperID).all()
