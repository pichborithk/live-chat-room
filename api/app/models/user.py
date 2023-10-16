from app import db
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    messages = relationship("Message", back_populates="sender")

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
        return db.session.query(User)

    @staticmethod
    def get_user_by_username(username):
        return db.session.query(User).filter_by(username=username).first()
