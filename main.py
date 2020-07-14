# -*- coding:utf-8 -*-

# Copyright(C), 2020-2020,  Co.,Ltd.
# ProjectName : flaskTemplate
# FileName : main.py
# Author : lvyandi
# Version : 0.10
# Date : 2020-07-09 11:46:47
# Description :
from apps import create_app, socketio

import websocket

app = create_app()


if __name__ == '__main__':
    socketio.run(app, host='192.168.25.127', port=5001,debug=True)
    # app.run()
