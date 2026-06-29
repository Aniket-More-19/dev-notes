from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class NoteResponse(BaseModel):
    id: UUID
    note: str
    created_at: datetime
    updated_at: datetime


class NoteRequest(BaseModel):
    note: str = Field(min_length = 5)
    
    class Config:
        json_schema_extra = {
            'example': {
                'note' : 'Update .Dockerfile of dev-notes backend',
            }
        }


class MessageResponse(BaseModel):
    message: str

