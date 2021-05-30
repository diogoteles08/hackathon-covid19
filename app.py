from flask import Flask, request, Response
from datetime import datetime
import json
from db import DB
from domain.message import Message

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def send_message():
    json = request.json
    message = Message(
        json["patientId"], json["text"], datetime.strptime(json["createdAt"], '%Y-%m-%dT%H:%M:%S.%fZ'), json["origin"]
    )
    DB.insert_message(message)
    return Response(status=204)


@app.route('/feed/<int:patient_id>', methods=['GET'])
def get_feed(patient_id):
    # Retrieve all the feed of a patient, including all messages and medias
    return Response(
        status=200,
        response=json.dumps([json.loads(msg.to_json()) for msg in DB.get_patient_messages(patient_id)]),
        content_type='application/json'
    )


if __name__ == '__main__':
    app.run()