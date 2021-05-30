import pandas
from domain.message import Message


class DB:

    # receive message and insert it into the csv file
    @staticmethod
    def insert_message(message):
        df = pandas.read_csv('./dbFiles/message.csv')
        df = df.append(message.__dict__, ignore_index=True)
        df.to_csv('./dbFiles/message.csv', index=False)

    # receive patient and return its messages
    @staticmethod
    def get_patient_messages(patient_id):
        df = pandas.read_csv('./dbFiles/message.csv')
        patient_df = df[df.patient_id == patient_id]

        patient_messages = []
        for index, row in patient_df.iterrows():
            patient_messages.append(Message(*(row.values.tolist())))
        patient_messages.reverse()
        return patient_messages
