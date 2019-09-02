# coding:utf-8

"""
数据库接口
@DatabaseInterface
@Author:Feng
@Date:2019-08-30
@QQ:960059842
"""

# 导入接口类的必要模块，作用：让定义的接口强制按照这个规范去执行，不按规范执行就会报错，这种格式就表示的是抽象类。
from abc import ABCMeta, abstractmethod


class DatabaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def execQuery(self, sql):
        pass

    @abstractmethod
    def execNonQuery(self, sql, tuple=None):
        pass

    @abstractmethod
    def execMany(self, sql, data):
        pass
