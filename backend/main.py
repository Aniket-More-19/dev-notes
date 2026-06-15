from fastapi import FastAPI, Path, Query, HTTPException, status
from note import Note, NoteRequest

app = FastAPI()

NOTES = [
    Note(1, "Write .Dockerfile for dev-notes backend", "2026-06-01T12:00:00Z", "2026-06-01T12:00:00Z"),
    Note(2, "Update CI workflow for dev-notes", "2026-06-01T12:00:00Z", "2026-06-01T12:00:00Z"),
    Note(3, "Check failing tests for note.py", "2026-06-01T12:00:00Z", "2026-06-01T12:00:00Z"),
]

# get all notes
@app.get("/notes/", status_code=status.HTTP_200_OK)
async def getAllNotes():
    return NOTES

# get a note by it's id
@app.get("/notes/{note_id}", status_code=status.HTTP_200_OK)
async def getNoteById(note_id: int = Path(gt=0)):
    for note in NOTES:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

# create a new note
@app.post("/notes/createNote", status_code=status.HTTP_201_CREATED)
async def createNote(note_request: NoteRequest):
    new_note = Note(**note_request.model_dump())
    NOTES.append(new_note)
    return new_note

# update a note
@app.put("/notes/updateNote", status_code=status.HTTP_200_OK)
async def updateNote(note_id: int, updatedNote: NoteRequest):
    for i, note in enumerate(NOTES):
        if note["id"] == note_id:
            updated_note = Note(id=note_id, **updateNote.model_dump())
            NOTES[i] = updated_note
            return updated_note
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/notes/deleteNote/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteNote(id: int):
    for i, note in NOTES:
        if note["id"] == id:
            NOTES.pop(i)
            return {"message": "Note deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")