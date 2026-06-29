from fastapi import HTTPException
from app.schemas.note import NoteRequest
from sqlalchemy.orm import Session
from sqlalchemy import text
from uuid import UUID


class NoteService:
    async def get_all_notes(self, db: Session):
        query = text("""
            SELECT id, note, created_at, updated_at 
            FROM notes 
            ORDER BY created_at DESC;
        """)
        result = db.execute(query)

        return result.mappings().all()

    async def get_note_by_id(self, note_id: UUID, db: Session):
        query = text("""
            SELECT id, note, created_at, updated_at
            FROM notes
            WHERE id = :note_id;
        """)

        result = db.execute(query, {"note_id": note_id})
        note = result.mappings().first()

        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return note


    async def create_note(self, note_request: NoteRequest, db: Session):
        try:
            query = text("""
                INSERT INTO notes (note)
                VALUES (:note)
                RETURNING id, note, created_at, updated_at;
            """)

            result = db.execute(query, {"note": note_request.note})
            note = result.mappings().first()
            db.commit()
            return note
        
        except Exception:
            db.rollback()
            raise

    async def update_note(self, note_id: UUID, updated_note: NoteRequest, db: Session):
        try:
            query = text("""
                UPDATE notes
                SET
                    note = :note
                WHERE
                    id = :note_id
                RETURNING id, note, created_at, updated_at;
            """)

            result = db.execute(query, {"note_id": note_id, "note": updated_note.note})

            if result.rowcount == 0:
                raise HTTPException(
                    status_code=404,
                    detail="Note not found"
                )

            note = result.mappings().first()
            db.commit()

            return note
        
        except Exception:
            db.rollback()
            raise

    async def delete_note(self, note_id: UUID, db: Session):
        try: 
            query = text("""
                DELETE FROM notes
                WHERE id = :note_id;
            """)
            result = db.execute(query, {"note_id": note_id})

            if result.rowcount == 0:
                raise HTTPException(
                    status_code=404, 
                    detail="Note not found"
                )
            
            db.commit()
            return {"message": "Note deleted successfully"}
        except Exception:
            db.rollback()
            raise