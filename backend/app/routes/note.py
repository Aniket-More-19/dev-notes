from fastapi import FastAPI, Path, Query, HTTPException, status
from app.models.note import Note, NoteRequest
from app.routes.router import router
from app.services.note import NoteService


app = FastAPI()

# get all notes
@router.get("/notes/", status_code=status.HTTP_200_OK)
async def get_all_notes():
    note_service = NoteService()
    response = await note_service.get_all_notes()
    return response

# get a note by it's id
@router.get("/notes/{note_id}", status_code=status.HTTP_200_OK)
async def get_note_by_id(note_id: int = Path(gt=0)):
    note_service = NoteService()
    response = await note_service.get_note_by_id(note_id)
    return response
    
# create a new note
@router.post("/notes/createNote", status_code=status.HTTP_201_CREATED)
async def create_note(note_request: NoteRequest):
    note_service = NoteService()
    response = await note_service.create_note(note_request)
    return response

# update a note
@router.put("/notes/updateNote", status_code=status.HTTP_200_OK)
async def update_note(note_id: int, updatedNnote: NoteRequest):
    note_service = NoteService()
    response = await note_service.update_note(note_id, updatedNnote)
    return response
    
# delete note by id
@router.delete("/notes/deleteNote/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int):
    note_service = NoteService()
    response = await note_service.delete_note(note_id)
    return response
    