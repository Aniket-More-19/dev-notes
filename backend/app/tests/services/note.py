import unittest
from uuid import uuid4
from unittest.mock import MagicMock
from app.services.note import NoteService
from app.schemas.note import NoteRequest
from datetime import datetime


class TestNote(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.db = MagicMock()
        self.result = MagicMock()
        self.service = NoteService()

    async def test_get_all_notes(self):
        note_id1 = uuid4()
        note_id2 = uuid4()

        fake_notes = [
            {
                "id": note_id2,
                "note": "sample note 2",
                "created_at": "2026-07-02T14:26:59.129136+05:30",
                "updated_at": "2026-07-02T14:26:59.129136+05:30"
            },
            {
                "id": note_id1,
                "note": "sample note 1",
                "created_at": "2026-07-02T14:26:49.712436+05:30",
                "updated_at": "2026-07-02T14:26:49.712436+05:30"
            },
        ]

        self.db.execute.return_value = self.result
        self.result.mappings.return_value.all.return_value = fake_notes

        returned_notes = await self.service.get_all_notes(self.db)

        self.assertEqual(returned_notes, fake_notes)
        self.db.execute.assert_called_once()


    async def test_get_note_by_id(self):
        note_id = uuid4()

        fake_note = {
            "id": note_id,
            "note": "sample note 1",
            "created_at": "2026-07-02T14:26:49.712436+05:30",
            "updated_at": "2026-07-02T14:26:49.712436+05:30"
        }

        self.db.execute.return_value = self.result
        self.result.mappings.return_value.first.return_value = fake_note

        returned_note = await self.service.get_note_by_id(note_id, self.db)

        self.assertEqual(returned_note, fake_note)
        self.db.execute.assert_called_once()

        query = self.db.execute.call_args.args[0]
        params = self.db.execute.call_args.args[1]

        self.assertEqual(params, {"note_id": note_id})
        self.assertIn("WHERE id = :note_id", str(query))

    async def test_create_note(self):
        note_request = NoteRequest(note="This is a sample create note")

        note_id = uuid4()
        now = datetime.now()

        expected_note = {
            "id": note_id,
            "note": note_request.note,
            "created_at": now,
            "updated_at": now,
        }
        
        self.db.execute.return_value = self.result
        self.result.mappings.return_value.first.return_value = expected_note

        returned_note = await self.service.create_note(note_request, self.db)
        
        self.db.execute.assert_called_once()
        self.db.commit.assert_called_once()

        self.assertEqual(returned_note, expected_note)

        query = self.db.execute.call_args.args[0]
        params = self.db.execute.call_args.args[1]

        self.assertEqual(params, {"note": note_request.note})
        self.assertIn("INSERT INTO notes", str(query))
        self.assertIn("VALUES (:note)", str(query))
        
        self.db.rollback.assert_not_called()

    async def test_update_note(self):

        note_request = NoteRequest(note="This is a sample update note")
        note_id = uuid4()
        expected_note = {
            "id": note_id,
            "note": note_request.note,
            "created_at": "2026-07-02T14:26:49.712436+05:30",
            "updated_at": datetime.now(),
        }
    
        self.db.execute.return_value = self.result
        self.result.mappings.return_value.first.return_value = expected_note

        returned_note = await self.service.update_note(note_id, note_request, self.db)

        self.db.execute.assert_called_once()
        self.db.commit.assert_called_once()

        self.assertEqual(returned_note, expected_note)
        
        query = self.db.execute.call_args.args[0]
        params = self.db.execute.call_args.args[1]

        self.assertIn("note = :note", str(query))
        self.assertIn("id = :note_id", str(query))
        self.assertIn("UPDATE notes", str(query))
        self.assertIn("RETURNING id, note, created_at, updated_at", str(query))

        self.assertEqual(params, {"note_id": note_id, "note": note_request.note})

        self.db.rollback.assert_not_called()

    async def test_delete_note(self):
        note_id = uuid4()

        expected_message = {
            "message": "Note deleted successfully"
        }

        self.db.execute.return_value = self.result
        self.result.rowcount = 1

        returned_message  = await self.service.delete_note(note_id, self.db)

        self.db.execute.assert_called_once()
        self.db.commit.assert_called_once()
        self.assertEqual(expected_message, returned_message)

        query = self.db.execute.call_args.args[0]
        params = self.db.execute.call_args.args[1]

        self.assertIn("DELETE FROM notes", str(query))
        self.assertIn("WHERE id = :note_id", str(query))
        self.assertEqual(params, {"note_id": note_id})

        self.db.rollback.assert_not_called()