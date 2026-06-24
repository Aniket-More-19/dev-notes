from typing import Optional
from pydantic import BaseModel, Field

class Note:
    id: int
    note: str
    created_at: str
    updated_at: str

    def __init__(self, id: int, note: str, created_at: str, updated_at: str):
        self.id = id
        self.note = note
        self.created_at = created_at
        self.updated_at = updated_at


class NoteRequest(BaseModel):
    id: Optional[int] = None
    note: str = Field(min_length = 5)
    created_at: str
    updated_at: str

    class Config:
        json_schema_extra = {
            'example': {
                'id' : 1,
                'note' : 'Update .Dockerfile of dev-notes backend',
                'created_at' : '2026-06-14T12:40:48.111Z',
                'updated_at' : '2026-06-14T12:40:48.111Z',
            }
        }