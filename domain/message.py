class Message:
    def __init__(self, patient_id, text, created_at, origin):
        self.patient_id = patient_id
        self.text = text
        self.created_at = created_at
        self.origin = origin
