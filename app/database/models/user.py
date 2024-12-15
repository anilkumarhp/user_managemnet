# Third Party
from db import Base
from sqlalchemy import Boolean, Column, Enum, Integer, String
from sqlalchemy.orm import relationship
from utility.roles import UserRole


class User(Base):
    """Model for user table."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    adhar_no = Column(String, nullable=False, unique=True)
    registered_no = Column(String, nullable=True)
    display_name = Column(String, nullable=True)
    phone_no = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    # Relationship with Address
    address = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )
