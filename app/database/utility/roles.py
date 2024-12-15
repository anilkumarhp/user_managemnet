# Standard Library
from enum import Enum


class UserRole(str, Enum):
    """Enums for roles."""

    USER = 'User'
    DOCTOR = 'Doctor'
    STAFF = 'Staff'
    ADMIN = 'Admin'
    PHARMACIST = 'Pharmacist'
