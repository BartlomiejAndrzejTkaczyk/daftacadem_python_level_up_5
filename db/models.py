from sqlalchemy import SmallInteger, Column, String
from database import Base


class Shipper(Base):
    __tablename__ = "shippers"

    ShipperID = Column(SmallInteger, primary_key=True)
    CompanyName = Column(String(40), nullable=False)
    Phone = Column(String(24))
