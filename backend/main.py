from fastapi import FastAPI

app = FastAPI()

notes = [
    {
        "id": 1,
        "note": "Write .Dockerfile for dev-notes backend",
        "created_at": "2026-06-01T12:00:00Z",
        "updated_at": "2026-06-01T12:00:00Z",
    },
    {
        "id": 2,
        "note": "Add CI workflow for dev-notes",
        "created_at": "2026-06-01T12:00:00Z",
        "updated_at": "2026-06-01T12:00:00Z",
    },
    {
        "id": 3,
        "note": "Check failing tests for note.py",
        "created_at": "2026-06-01T12:00:00Z",
        "updated_at": "2026-06-01T12:00:00Z",
    },
]

@app.get("/")
async def getAllNotes():
    return {"notes": notes}

@app.get("/{id}")
async def getNoteById(id: int):
    for note in notes:
        if note["id"] == id:
            return note
    return {"error": "Note not found"}

@app.post("/createNote")
async def createNote(note: dict):
    notes.append({
        "id": len(notes) + 1,
        "note": note["note"],
        "created_at": note["created_at"],
        "updated_at": note["updated_at"],
    })

@app.put("/updateNote")
async def updateNote(id: int, updatedNote: dict):
    for note in notes:
        if note["id"] == id:
            note["todo"]=updatedNote["todo"]
            note["created_at"]=updatedNote["created_at"]
            note["updated_at"]=updatedNote["updated_at"]
            break

@app.delete("/deleteNote/{id}")
async def deleteNote(id: int):
    for note in notes:
        if note["id"] == id:
            notes.pop(notes.index(note))
            return {"message": "Note deleted successfully"}