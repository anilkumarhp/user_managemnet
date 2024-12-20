# Standard Library
import os

# Third Party
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Reading database credentials from environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

DATABASE_URL = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

# Creates a SQLAlchemy engine which handles database connections.
engine = create_engine(DATABASE_URL)

# Creates a session factory and associates the session with our database engine
# autocommit=False: Changes aren't automatically committed to database
# autoflush=False: Changes aren't automatically synchronized with database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creates a base class for declarative models.
# All the database models (tables) will inherit from this base class.
Base = declarative_base()


def get_db():
    """Create a new database session and return it to caller."""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(str(e))
    finally:
        db.close()
