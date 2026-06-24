import uuid
from app.database import Base
from sqlalchemy import Column, String, TIMESTAMP, Uuid
from sqlalchemy.sql import func


class Note(Base):
    __tablename__ = "notes"


    id = Column(Uuid, primary_key=True, nullable=False, default=uuid.uuid4)
    note = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
