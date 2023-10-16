from app import db
from sqlalchemy.orm import relationship


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    sender = relationship("User", back_populates="messages")

    def save(self):
        db.session.add(self)
        db.session.commit()
