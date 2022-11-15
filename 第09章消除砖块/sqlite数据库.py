# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : sqlite数据库.py
# @Time    : 2022/10/28 19:06
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$

# -*- coding:utf-8 -*-

import sqlite3
import traceback


def catch_except(func):
    # 捕获错误
    def inner_func(*args, **kwargs):
        try:
            info = func(*args, **kwargs)
            return info
        except Exception as ex:
            traceback.print_exc()
            # raise ex
            print("未完成")
            pass

    return inner_func


class SqliteDB(object):
    def __init__(self, database="test.db", isolation_level="", ignore_exc=False):
        """
        :param database:
        :param isolation_level:事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        :param ignore_exc:忽略错误，True直接提交，False回滚事务
        return:
        """
        self.database = database
        self.isolation_level = isolation_level
        self.ignore_exc = ignore_exc

        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        :param self:
        return:返回当前类，以调用更多的方法
        获取游标用当前类的方法
        """
        self.enter()
        return self

    @catch_except
    def enter(self):
        # 获取与数据库的连接
        self.connection = sqlite3.connect(
            database=self.database, isolation_level=self.isolation_level
        )
        # 获取游标
        self.cursor = self.connection.cursor()

        # 获取或设置数据操作语句的返回值，如 INSERT、UPDATE 和 DELETE
        # 默认情况下，该 Pragma 为 false，这些语句不返回任何东西。如果设置为 true，每个所提到的语句将返回一个单行单列的表，由一个单一的整数值组成，该整数表示操作影响的行
        # info=self.run("PRAGMA count_changes=true;")
        # print (info)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type:如果抛出异常,这里获取异常的类型
        :param exc_val:如果抛出异常,这里显示异常内容
        :param exc_tb:如果抛出异常,这里显示所在位置
        return:
        """
        # 提交事务
        self.exit(exc_type)
        # 关闭连接，游标
        self.cursor.close()
        self.connection.close()

    @catch_except
    def exit(self, exc_type):
        if not exc_type is None:
            # 异常发生时，回滚事务
            self.connection.rollback()
            return self.ignore_exc
        else:
            self.connection.commit()

    def getCursor(self):
        return self.cursor

    def getConnections(self):
        return self.connection

    @catch_except
    def run(self, sql):
        self.cursor.execute(sql)
        # 将查询到的剩余的结果,以列表形式返回
        info = self.cursor.fetchall()
        return info

    def table_info(self, table):
        # 表的字段信息
        info = self.run(f"PRAGMA table_info({table})")
        return info

    def table_data(self, table):
        # 表的资料信息
        info = self.run(f"select * from {table}")
        return info

    def table_name(self):
        # 表的表名
        info = self.run("select name from sqlite_master where type='table' order by name")
        return info

    def database_info(self):
        # 列出了所有的数据库连接,返回一个单行三列的表格，
        # 每当打开或附加数据库时，会给出数据库中的序列号，它的名称和相关的文件
        info = self.run("PRAGMA database_list")
        return info

    def __repr__(self):
        return self.database_info()

    @catch_except
    def insert_data(self, table, data):
        """
        sql = 'INSERT INTO user (id, name, age) values (?, ?, ?)'
        data = [
                (1, 'Alice', 21),
                (2, 'Bob', 22),
                (3, 'Chris', 23)
                ]
        """
        n = len(data[0])
        if n:
            p = "?"
            a = "," + p
            for i in range(n - 1):
                p += a

        sql = "INSERT INTO " + str(table) + " values(" + p + ")"
        print(sql)

        self.cursor.executemany(sql, data)

    def getChanges(self):
        # 被打开以来更改的次数，删除，插入，修改
        return self.connection.total_changes

    def get_foreign_key(self, table):
        # 返回外键列表
        return self.run(f"PRAGMA foreign_key_list({table});")


if __name__ == "__main__":  # 建表
    with SqliteDB("test") as d:
        info = d.table_name()
        print(info)
        print(d.table_info("user"))
        print(d.table_data("user"))
