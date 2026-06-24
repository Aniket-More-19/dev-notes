from typing import Optional
from fastapi import HTTPException
from app.schemas.note import Note, NoteRequest


NOTES = [
    Note(1, "Write .Dockerfile for dev-notes backend", "2026-06-01T12:00:00Z", "2026-06-01T12:00:00Z"),
    Note(2, "Update CI workflow for dev-notes", "2026-06-01T12:00:00Z", "2026-06-01T12:00:00Z"),
    Note(3, "Check failing tests for note.py", "2026-06-01T12:00:00Z", "2026-06-01T12:00:00Z"),
]


class NoteService:
    async def get_all_notes(self):
        return NOTES
    
    async def get_note_by_id(self, note_id: int):
        for note in NOTES:
            if note.id == note_id:
                return note
        raise HTTPException(status_code=404, detail="Note not found")

    async def create_note(self, note_request: NoteRequest):
        new_note = Note(**note_request.model_dump())
        NOTES.append(new_note)
        return new_note

    async def update_note(self, note_id: int, updatedNnote: NoteRequest):
        for i, note in enumerate(NOTES):
            if note.id == note_id:
                updated_note = Note(**updatedNnote.model_dump())
                NOTES[i] = updated_note
                return updated_note
        raise HTTPException(status_code=404, detail="Product not found")


    async def delete_note(self, note_id: int):
        for i, note in enumerate(NOTES):
            if note.id == note_id:
                NOTES.pop(i)
                return
        raise HTTPException(status_code=404, detail="Product not found")