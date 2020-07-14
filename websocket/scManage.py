# -*- coding:utf-8 -*-

# Copyright(C), 2020-2020,  Co.,Ltd.
# ProjectName : VMM
# FileName : scManage.py
# Author : lvyandi
# Version : 0.10
# Date : 2020-07-13 09:16:57
# Description :

from apps import socketio
from websocket.business import pcu


socketio.on_event('login', pcu.login,namespace='/ws/')
socketio.on_event('get_pcu',pcu.get_pcu,namespace='/ws/')
socketio.on_event('logout',pcu.logout,namespace='/ws/')


socketio.on_event('connect',pcu.connect,namespace='/ws/')
socketio.on_event('disconnect',pcu.disconnect,namespace='/ws/')
