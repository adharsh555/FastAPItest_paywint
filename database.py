from sqslalchemy import create_engine
from sqlalchemy.orm import sessionmaker,


engine = create_engine(D_url)
SessionLocal=sessionmaker(bind=engine,autocommit=False)
Base = declarative_base()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
