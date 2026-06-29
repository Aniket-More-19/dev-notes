from fastapi import status, Depends
from app.schemas.note import NoteRequest, NoteResponse, MessageResponse
from app.routes.router import router
from app.services.note import NoteService
from sqlalchemy.orm import Session
from app.database import get_db
from uuid import UUID



# get all notes
@router.get("/notes/", status_code=status.HTTP_200_OK, response_model=list[NoteResponse])
async def get_all_notes(db: Session = Depends(get_db)):
    note_service = NoteService()
    response = await note_service.get_all_notes(db)
    return response

# get a note by it's id
@router.get("/notes/{note_id}", status_code=status.HTTP_200_OK, response_model=NoteResponse)
async def get_note_by_id(note_id: UUID, db: Session = Depends(get_db)):
    note_service = NoteService()
    response = await note_service.get_note_by_id(note_id, db)
    return response
    
# create a new note
@router.post("/notes/", status_code=status.HTTP_201_CREATED, response_model=NoteResponse)
async def create_note(note_request: NoteRequest, db: Session = Depends(get_db)):
    note_service = NoteService()
    response = await note_service.create_note(note_request, db)
    return response

# update a note
@router.put("/notes/{note_id}", status_code=status.HTTP_200_OK, response_model=NoteResponse)
async def update_note(note_id: UUID, updated_note: NoteRequest, db: Session = Depends(get_db)):
    note_service = NoteService()
    response = await note_service.update_note(note_id, updated_note, db)
    return response

# delete note by id
@router.delete("/notes/{note_id}", status_code=status.HTTP_200_OK, response_model=MessageResponse)
async def delete_note(note_id: UUID, db: Session = Depends(get_db)):
    note_service = NoteService()
    response = await note_service.delete_note(note_id, db)
    return response
    