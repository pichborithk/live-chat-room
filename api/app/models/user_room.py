from app import db, Base
from sqlalchemy.orm import relationship


class UserRoom(db.Model, Base):
    __tablename__ = "user_room"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    user = relationship("User", back_populates="user_rooms")

    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), primary_key=True)
    room = relationship("Room", back_populates="room_users")

    def __init__(self, user_id, room_id):
        self.user_id = user_id
        self.room_id = room_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "UserRoom: {}".format(self.rooms)
