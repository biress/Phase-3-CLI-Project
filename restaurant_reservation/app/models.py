from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    reservations = relationship("Reservation", back_populates="customer")

class Table(Base):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True)
    table_number = Column(Integer)
    capacity = Column(Integer)
    reservations = relationship("Reservation", back_populates="table")

class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    table_id = Column(Integer, ForeignKey('tables.id'))
    reservation_time = Column(DateTime)
    guest_count = Column(Integer)

    customer = relationship("Customer", back_populates="reservations")
    table = relationship("Table", back_populates="reservations")
