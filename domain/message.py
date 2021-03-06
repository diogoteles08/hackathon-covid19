import json
from datetime import datetime


class Message:
    def __init__(self, patient_id, text, created_at, origin, author):
        self.patient_id = patient_id
        self.text = text
        self.created_at = datetime.fromisoformat(created_at) if isinstance(created_at, str) else created_at
        self.origin = origin
        self.author = author

    def to_json(self):
        return json.dumps(
            {
                "patientId": self.patient_id,
                "text": self.text,
                "createdAt": self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "origin": self.origin,
                "author": self.author,
            }
        )
