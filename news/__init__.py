from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    news = Flask(__name__)
    news.config.from_object(config[config_name])
    config[config_name].init_app(news)

    db.init_app(news)

    from .main import main as main_blueprint
    news.register_blueprint(main_blueprint)

    return news

