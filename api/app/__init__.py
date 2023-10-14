import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = bytes(os.getenv("APP_SECRET_KEY"), "utf-8")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_PATH")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.module.controllers import *
