from app import db, Base
from sqlalchemy.orm import relationship


class UserRoom(db.Model, Base):
    __tablename__ = "user_room"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    users = relationship("User", back_populates="rooms")

    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), primary_key=True)
    rooms = relationship("Room", back_populates="users")

    def __init__(self, user_id, room_id):
        self.user_id = user_id
        self.room_id = room_id

    def save(self):
        db.session.add(self)
        db.session.commit()
