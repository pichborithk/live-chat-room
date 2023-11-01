from app import db
from sqlalchemy.orm import relationship


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    sender = relationship("User", back_populates="messages")

    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))
    room = relationship("Room", back_populates="messages")

    def __init__(self, text, sender_id, room_id):
        self.text = text
        self.sender_id = sender_id
        self.room_id = room_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        messages = db.session.query(Message)
        result = []
        for message in messages:
            obj = {
                "id": message.id,
                "text": message.text,
                "sender": message.sender.username,
            }
            result.append(obj)

        return result
