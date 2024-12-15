# Third Party
from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Address(Base):
    """Model for address table."""

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, index=True)
    house_no = Column(String, nullable=True)
    building = Column(String, nullable=True)
    street = Column(String)
    cross = Column(String, nullable=True)
    post = Column(String, nullable=True)
    taluk = Column(String)
    district = Column(String)
    state = Column(String)
    country = Column(String)

    # ForeignKey to the User model
    adhar_no = Column(
        String, ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )

    # Establish the relationship with the User model
    user = relationship('User', back_populates='address')
