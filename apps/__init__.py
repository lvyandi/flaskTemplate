# -*- coding:utf-8 -*-

# Copyright(C), 2020-2020,  Co.,Ltd.
# ProjectName : flaskTemplate
# FileName : __init__.py.py
# Author : lvyandi
# Version : 0.10
# Date : 2020-07-09 11:45:57
# Description :
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(allow_upgrades=True, engineio_logger=True,transport='websocket',logger=True)

def create_app():
    app = Flask(__name__, template_folder='', static_folder='')

    socketio.init_app(app, cors_allowed_origins='*')
    return app