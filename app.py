from flask import Flask, request, jsonify
from flask_cors import cross_origin
from datetime import datetime

from db import DB
from domain.message import Message

app = Flask(__name__)


@app.route('/message', methods=['POST'])
@cross_origin()
def send_message():
    json = request.json
    message = Message(
        json["patientId"],
        json["text"],
        datetime.strptime(json["createdAt"], '%Y-%m-%dT%H:%M:%S.%fZ'),
        json["origin"],
        json["author"]
    )
    DB.insert_message(message)
    return jsonify(status=204)


@app.route('/feed/<int:patient_id>', methods=['GET'])
@cross_origin()
def get_feed(patient_id):
    # Retrieve all the feed of a patient, including all messages and medias
    message_list = [msg.to_json() for msg in DB.get_patient_messages(patient_id)]
    return jsonify(
        status=200,
        response=message_list,
        content_type='application/json',
    )


if __name__ == '__main__':
    app.run()
