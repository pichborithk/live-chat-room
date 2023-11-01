from app import db, Base

from sqlalchemy.orm import relationship


class Room(db.Model, Base):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True, nullable=False)

    messages = relationship("Message", back_populates="room")

    users = relationship("UserRoom", back_populates="rooms")

    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return "Room: {}".format(self.code)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_code():
        rooms = db.session.query(Room).all()
        result = []
        for room in rooms:
            result.append(room.code)
        return result

    # @staticmethod
    # def get_user_by_id(user_id):
    #     return db.get_or_404(User, user_id, description="Invalid Information")
    #
    # @staticmethod
    # def get_user_by_username(username):
    #     return db.session.query(User).filter_by(username=username).first()
