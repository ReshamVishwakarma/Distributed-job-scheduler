from app.db.database import engine, Base
from app.models import job  # ensures model is imported

def init_db():
    Base.metadata.create_all(bind=engine)
