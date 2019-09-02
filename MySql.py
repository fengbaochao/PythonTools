# coding:utf-8

"""
MySql 工具类
@MySql
@Author:Feng
@Date:2019-08-30
@QQ:960059842
"""

import pymysql

from Tools.DatabaseInterface import DatabaseInterface


class MySql(DatabaseInterface):
    def __init__(self, host, user, pwd, name, port):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.name = name
        self.port = port

    def __getConnect(self):
        if not self.name:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.pwd,
            db=self.name,
            port=self.port,
            charset="utf8",
        )
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def execQuery(self, sql):
        cur = self.__getConnect()
        cur.execute(sql)
        data = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return data

    def execNonQuery(self, sql, tuple=None):
        cur = self.__getConnect()
        cur.execute(sql, tuple)
        self.conn.commit()
        self.conn.close()

    def execMany(self, sql, data):
        cur = self.__getConnect()
        cur.executemany(sql, data)
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    ms = MySql(host="localhost", user="root", pwd="feng", name="Test", port=3306)

    sql = "DELETE FROM Teacher"
    ms.execNonQuery(sql)

    # 插入Sql
    insertSql = "INSERT INTO Teacher(UserID,UserCode,UserName,UserPwd,TelePhone,ImgMap) VALUES(%s,%s,%s,%s,%s,%s)"
    # 插入list
    listInsert = []

    insertTuple = [1, "001", "赵", "001", "188-8888-8881", "1"]
    listInsert.append(tuple(insertTuple))
    # insertTuple = ["2", "002", "钱", "002", "188-8888-8882", "2"]
    # listInsert.append(tuple(insertTuple))
    # insertTuple = ["3", "003", "孙", "003", "188-8888-8883", "3"]
    # listInsert.append(tuple(insertTuple))
    # insertTuple = ["4", "004", "李", "004", "188-8888-8884", "4"]
    # listInsert.append(tuple(insertTuple))

    # print(listInsert)
    # ms.execMany(insertSql, listInsert)
    ms.execNonQuery(insertSql, tuple(insertTuple))

    data = ms.execQuery("SELECT * FROM Teacher")
    for row in data:
        print(row)

    # newsql = "update Teacher set UserName='%s' where UserID=%d" % ('测试', 1)
    # ms.execNonQuery(newsql)
