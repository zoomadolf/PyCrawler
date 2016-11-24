# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: kevin
@license: Apache Licence 
@contact: liujiezhang@bupt.edu.cn
@site: 
@software: PyCharm Community Edition
@file: mysql.py
@time: 16/11/24 上午10:39
"""

import MySQLdb
import time


class DB(object):
    # 实例化数据库

    def __init__(self, db_name='test'):
        # 连接数据库
        self.connect = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='zlj521226',
            db=db_name,
            charset='utf8'
        )
        # 获取游标
        self.cursor = self.connect.cursor()

    def connect(self):
        '''
        复写connect方法
        :return:
        '''
        return self.connect

    def cursor(self):
        '''
        复写cursor方法
        :return:
        '''
        return self.cursor

    def close(self):
        '''
        关闭数据库
        :return:
        '''
        self.cursor.close()

    def commit(self):
        '''
        提交更改
        :return:
        '''
        self.connect.commit()

    def roolback(self):
        '''
        回滚
        :return:
        '''
        self.connect.rollback()


class M(DB):

    def __init__(self):
        # 继承DB类
        DB.__init__(self)

    def creatTable(self, args_dict):  # Todo 前期先在mysql手动建表
        '''
        创建数据表
        :param table_name: 表名
        :args_dict:字段名,类型 dict格式
        :return:
        '''
        pass

    def insertOne(self, table, data):
        '''
        单条数据插入
        :param table:指定插入的表名
        :param data:插入数据 dict格式
        :return:
        '''
        if not isinstance(data, dict):
            raise KeyError("Insert data is not a dict")
        if not dict:
            raise ValueError("data is empty!")
        # sql语句格式
        sql = "insert into {0}({1}) values({2})".format(
            table, ','.join(data.keys()), ','.join(['%s'] * len(data.keys())))
        # 数据格式
        param = tuple(data.values())
        try:
            # 插入数据
            retrun_n = DB.cursor(self).execute(sql, param)
        except:
            raise('Failed insert data.')
        # 提交事务
        DB.commit(self)
        print 'insert', retrun_n

    def insertAll(self,table,data):
        '''
        多条数据插入
        :param table: 指定插入表名
        :param data: 多条数据 [dict,dict]
        :return:
        '''
        if not (data and isinstance(data,list) and isinstance(data[0],dict)):
            raise KeyError('Insert data is illegal!')
        # sql语句格式
        sql = "insert into {0}({1}) values({2})".format(
            table, ','.join(data[0].keys()), ','.join(['%s'] * len(data[0].keys())))
        # 数据格式
        param = tuple(map(lambda x:tuple(x.values()),data))
        try:
            # 多条插入数据
            retrun_n = DB.cursor(self).executemany(sql, param)
        except:
            raise('Failed insert data.')
        # 提交事务
        DB.commit(self)
        print 'insert', retrun_n

if __name__ == '__main__':
    db_test = DB('test')
    table_test = M()

    data = [{'name': 'Evd', 'create_time': int(time.time())},{'name': 'Fvd', 'create_time': int(time.time())}]
    table_test.insertAll('test2', data)
