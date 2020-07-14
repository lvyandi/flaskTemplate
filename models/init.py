# -*- coding:utf-8 -*-

# Copyright(C), 2020-2020,  Co.,Ltd.
# ProjectName : flaskTemplate
# FileName : init.py
# Author : lvyandi
# Version : 0.10
# Date : 2020-07-09 11:46:33
# Description :

from models.model import base, eg, db, Students


def init_db():
    base.metadata.create_all(bind=eg)


def del_db():
    base.metadata.drop_all(eg)


def init_students():
    # student = Students(uuid='1121ds111ds1',name='wwwww2dsddsdwww')
    # student.add()
    student = db.query(Students).first()
    print(student.age)
    student.age = 3
    db.commit()
    print(student)

def init_meta():
    print(base.metadata.__class__)
    print(base.metadata.__dict__)
    print(base.metadata.tables['student'].__dict__['columns'])
    print(base.metadata)



if __name__ == '__main__':
    # del_db()
    # init_db()
    init_students()
    # init_meta()
    pass