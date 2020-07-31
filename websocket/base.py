# -*- coding:utf-8 -*-

# Copyright(C), 2020-2020,  Co.,Ltd.
# ProjectName : VMM
# FileName : base.py
# Author : lvyandi
# Version : 0.10
# Date : 2020-07-13 09:09:41
# Description :

import flask
from flask_socketio import emit


class Base(object):
    onlineSocket = dict()

    def login(self, username):
        print('begin...')
        socketio = flask.current_app.extensions['socketio']
        sid = flask.request.sid
        print(sid)
        self.onlineSocket[username] = sid
        message = []
        for x in range(10): message.append({'title': str(x), 'desc': str(x)})
        emit('getMessage', message)
        print('user login success', self.onlineSocket)

    def get_pcu(self):
        emit('getLogin', len(self.onlineSocket.keys()))
        print('get pcu', self.onlineSocket)

    def logout(self, username):
        try:
            self.onlineSocket.pop(username)
            emit('getLogin', len(self.onlineSocket.keys()))
            print('user logout!!', self.onlineSocket)
        except KeyError:
            pass

    def emit(self, event, msg, username=None):
        try:
            room = self.onlineSocket[username] if username is not None else None
            emit(event, msg, room=room)
        except:
            pass

    def connect(self):
        socketio = flask.current_app.extensions['socketio']
        sid = flask.request.sid
        print("websocket connect success")

        # test thread



    def disconnect(self):
        print("websocket disconnect success")

    pass


