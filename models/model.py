# -*- coding:utf-8 -*-

# Copyright(C), 2020-2020,  Co.,Ltd.
# ProjectName : flaskTemplate
# FileName : model.py
# Author : lvyandi
# Version : 0.10
# Date : 2020-07-09 11:46:22
# Description :
import datetime
import json

import sqlalchemy
from sqlalchemy import create_engine, Column, BigInteger, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import QueuePool

eg = create_engine("postgresql://postgres:postgres@127.0.0.1:5432/template", echo=False, pool_size=1000,
                   poolclass=QueuePool, max_overflow=1000, pool_timeout=10, pool_recycle=10)

db = scoped_session(sessionmaker(autocommit=False, autoflush=False,bind=eg,expire_on_commit=False))


class _Base(object):
    query = db.query_property()

    def add(self):
        db.add(self)
        db.commit()

    def delete(self):
        db.delete(self)
        db.commit()

    def __del__(self):
        db.remove()

    def __repr__(self):
        res = {}
        for k, v in self.__dict__.items():
            if not isinstance(v,sqlalchemy.orm.state.InstanceState):
                res[k] = str(v)
        return str(res)



base = declarative_base(cls=_Base)

# 集群
class Students(base):
    __tablename__ = 'student'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(String, unique=True)
    name = Column(String, unique=True)
    age = Column(BigInteger)
    time = Column(DateTime, default=datetime.datetime.now())

