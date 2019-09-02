# coding:utf-8

"""
Path 工具类
@Path
@Author:Feng
@Date:2019-08-30
@QQ:960059842
"""

import os


class Path:
    # 获取目录下的所有文件
    def getFileList(self, dir, fileList):
        newDir = dir
        # 是否是文件
        if os.path.isfile(dir):
            fileList.append(dir)
        # 是否是文件夹
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                # 如果需要忽略某些文件夹，使用以下代码
                # if s == "xxx":
                #   continue
                newDir = os.path.join(dir, s)
                self.getFileList(newDir, fileList)
        return fileList

    def getFileList(self, dir):
        fileList = []
        if os.path.isdir(dir):
            for name in os.listdir(dir):
                filepath = os.path.join(dir, name)
                if os.path.isfile(filepath):
                    fileList.append(filepath)

        return fileList

    # 获取文件扩展名
    def getExtension(self, filepath):
        return os.path.splitext(filepath)[1]

    # 返回不具有扩展名的指定路径字符串的文件名
    def getFileNameWithoutExtension(self, filepath):
        filename = os.path.split(filepath)[1]
        return os.path.splitext(filename)[0]

    # 返回指定路径字符串的目录信息
    def getFileName(self, filepath):
        return os.path.split(filepath)[1]

    # 返回指定路径字符串的目录信息
    def getDicName(self, filepath):
        return os.path.split(filepath)[0]

    # 获取文件大小,KB
    def getFileSize(self, filePath):
        fsize = os.path.getsize(filePath)
        fsize = fsize / float(1024)
        return round(fsize)  # 保留两位小数


if __name__ == "__main__":
    filePath = r"C:\Users\FBC\Desktop\题库\011建筑电工.xlsx"
    path = Path()
    print(path.getDicName(filePath))
