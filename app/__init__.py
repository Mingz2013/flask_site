__author__ = 'zhaojm'
import logging

from flask import Flask
from config import config
from app.controllers import activity_controller, index_controller


def create_app(config_mode):
    app = Flask(__name__)

    app.config.from_object(config[config_mode])


    from logging import FileHandler

    file_handler = FileHandler("logs/activity.log")
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)


    app.register_blueprint(index_controller.index_controller)
    app.register_blueprint(activity_controller.activity_controller)

    app.logger.debug("activity log")

    return app