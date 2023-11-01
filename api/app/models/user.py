from app import db, Base
from sqlalchemy.orm import relationship


class User(db.Model, Base):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    messages = relationship("Message", back_populates="sender")

    rooms = relationship("UserRoom", back_populates="users")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "Username: {}".format(self.username)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        # users = User.query.all()
        # result = []
        # for user in users:
        #     obj = {"id": user.id, "username": user.username}
        #     result.append(obj)
        # return result
        return db.session.query(User).all()

    @staticmethod
    def get_user_by_id(user_id):
        return db.get_or_404(User, user_id, description="Invalid Information")

    @staticmethod
    def get_user_by_username(username):
        return db.session.query(User).filter_by(username=username).first()
