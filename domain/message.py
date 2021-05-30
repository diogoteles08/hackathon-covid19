import json


class Message:
    def __init__(self, patient_id, text, created_at, origin, author):
        self.patient_id = patient_id
        self.text = text
        self.created_at = created_at
        self.origin = origin
        self.author = author

    def to_json(self):
        return json.dumps(
            {
                "patientId": self.patient_id,
                "text": self.text,
                "createdAt": self.created_at,
                "origin": self.origin,
                "author": self.author
            }
        )
