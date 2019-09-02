# coding:utf-8

"""
数据库
@Database
@Author:Feng
@Date:2019-08-30
@QQ:960059842
"""

# 导入枚举类
from enum import Enum
from Tools.SqLite import SqLite
from Tools.MSSQL import MSSQL
from Tools.MySql import MySql


def getDatabase(database, args):
    if database == database.SQLITE:
        return SqLite(dbPath=args["dbPath"])
    elif database == database.MSSQL:
        return MSSQL(
            host=args["host"], user=args["user"], pwd=args["pwd"], name=args["name"]
        )
    elif database == database.MYSQL:
        return MySql(
            host=args["host"],
            user=args["user"],
            pwd=args["pwd"],
            name=args["name"],
            port=args["port"],
        )

    raise (NameError, "不支持的数据库类型")


def execQuery(db, sql):
    return db.execQuery(sql)


def execNonQuery(db, sql, tuple=None):
    db.execNonQuery(sql)


def execMany(db, sql, data):
    db.execMany(sql, data)


class database(Enum):
    MSSQL = 1
    SQLITE = 2
    MYSQL = 3


if __name__ == "__main__":

    """
    MSSQL
    """
    args = {"host": ".", "user": "sa", "pwd": "feng", "name": "DncZeus"}
    db = getDatabase(database.MSSQL, args)

    data = execQuery(db, "SELECT * FROM dbo.City")
    for row in data:
        print(row)

    # 更新
    # newsql="update webuser set name='%s' where id=1"%u'测试'
    # ExecNonQuery(db,newsql)

    """
    SqLite
    """
    dbPath = r"D:\Projects\Python\Test\Tools\TestFiles\Teacher.db"
    args = {"dbPath": dbPath}
    db = getDatabase(database.SQLITE, args)

    sql = "DELETE FROM Teacher"
    execNonQuery(db, sql)

    # SqLite占位符是? 其他的占位符为%s
    # 插入Sql
    insertSql = "INSERT INTO Teacher(UserID,UserCode,UserName,UserPwd,TelePhone,ImgMap) VALUES(?,?,?,?,?,?)"
    # 插入list
    listInsert = []

    insertTuple = ["1", "001", "赵", "001", "188-8888-8881", "1"]
    listInsert.append(tuple(insertTuple))
    insertTuple = ["2", "002", "钱", "002", "188-8888-8882", "2"]
    listInsert.append(tuple(insertTuple))
    insertTuple = ["3", "003", "孙", "003", "188-8888-8883", "3"]
    listInsert.append(tuple(insertTuple))
    insertTuple = ["4", "004", "李", "004", "188-8888-8884", "4"]
    listInsert.append(tuple(insertTuple))

    print(listInsert)
    execMany(db, insertSql, listInsert)

    data = execQuery(db, "SELECT * FROM Teacher")
    for row in data:
        print(row)

    """
    MYSQL
    """
    args = {
        "host": "localhost",
        "user": "root",
        "pwd": "feng",
        "name": "Test",
        "port": 3306,
    }
    db = getDatabase(database.MYSQL, args)
