# -*- coding:utf-8 -*-

# Copyright(C), 2020-2020,  Co.,Ltd.
# ProjectName : flaskTemplate
# FileName : utils.py
# Author : lvyandi
# Version : 0.10
# Date : 2020-07-10 15:32:30
# Description : test postgresql tablespace
import subprocess
import sys
import time

import psycopg2


from settings import SQL_HOST,SQL_PORT,SQL_DATABASE,SQL_PASSWORD,SQL_USERNAME


class SQL:
    def __init__(self,host='127.0.0.1',port='5432',user='postgres',password='postgres',database='template'):
        self.host = host
        self.user = user
        self.passward = password
        self.database = database

        self.conn = psycopg2.connect(database=database, user=user, password=password, host=host,port=port)
        self.cursor = self.conn.cursor()


    def get_tablenac(self):
        sql = 'select spcname, pg_tablespace_location(oid) from pg_tablespace;'
        sql = 'select * from pg_tablespace;'
        return self.execute(sql)

    def add_tabnac(self, tablenac, path):
        sql = "create tablespace {} location {};".format(tablenac,path)
        return self.popen(sql)

    def del_tabnac(self, tablenac):
        sql = "drop tablespace {};".format(tablenac)
        return self.popen(sql)

    def alter_tb_to_tabnac(self, tablename, tablenac):
        sql = 'alter table {} set tablespace {};'.format(tablename, tablenac)
        return self.popen(sql)

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            print(repr(e))
            return False
        finally:
            self.conn.commit()

    def popen(self, nosql, user=None,password=None, database=None):
        if not user:user=self.user
        if not password:password=self.passward
        if not database:database=self.database
        cmd = '''psql -c "{}" {} {}'''.format(nosql,database,user)
        print(cmd)
        res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               shell=True)
        time.sleep(1)
        res.stdin.write(bytes(password, 'utf-8'))
        res.stdin.write(bytes('\n', 'utf-8'))
        res.stdin.flush()
        res.stdin.close()
        for line in res.stdout.readlines():
            line = str(line,'utf-8').replace('\n','')
            if line:print(line)


    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            print('exit')
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(repr(e))



if __name__ == '__main__':
    sql1 = "select * from student;"
    sql2 = "show data_directory;"
    sql3 = "select spcname, pg_tablespace_location(oid) from pg_tablespace;"
    sql4 = "select pg_database.datname from pg_database"

    sql5 = '''select relname, relkind, relpages,pg_size_pretty(pg_relation_size(a.oid)),reltablespace,relowner  
                from pg_class a, pg_tablespace tb  
                where a.relkind in ('r', 'i')  
                and a.reltablespace=tb.oid  
                and tb.spcname=ts_demo'  
                order by a.relpages desc;'''

    sql6='''select relname, relkind, relpages,pg_size_pretty(pg_relation_size(a.oid)), tb.spcname  
             from pg_class a, pg_tablespace tb  
            where a.reltablespace = tb.oid  
             and a.relkind in ('r', 'i')  
            order by a.relpages desc;'''
    with SQL() as f:
        # print(f.add_tabnac('ts_ts',"'/test'"))
        # print(f.del_tabnac('ts_ts'))
        print(f.get_tablenac())
        # print(f.execute(sql2))
        # print(f.execute(sql4))
        # print(f.execute(sql5))
        # for x in f.execute(sql6):
        #     print(x)







