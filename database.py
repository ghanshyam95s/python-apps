from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

url = "sqlite:///./data/app.db"
engine = create_engine(url)
session = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    except Exception as e:
        return f"exception occurred: {e}"
    finally:
        db.close()

