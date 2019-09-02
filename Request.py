# coding:utf-8

"""
Request 工具类
@Excel
@Author:Feng
@Date:2019-08-30
@QQ:960059842
"""

import requests
import json
import os
from Tools.Path import Path

class Request:
    """
    POST
    """

    def post(self, url, data=None, headers=None):
        res = requests.post(url=url, json=data, headers=headers)
        return json.loads(res.text)

    """
    GET
    """

    def get(self, url, data=None, headers=None):
        # verify=False
        res = requests.get(url=url, json=data, headers=headers)
        return json.loads(res.text)

    """
    DownFile
    """

    def downFile(self, url, downFilePath):
        # 下载
        request = requests.get(url)
        # 判断文件是否存在不存在删除
        if os.path.isfile(downFilePath):
            os.remove(downFilePath)

        # 判断路径是否存在不存在则删除
        downPath = Path().getDicName(downFilePath)
        if os.path.exists(downPath):
            pass
        else:
            os.makedirs(downPath)

        with open(downFilePath, "wb") as code:
            code.write(request.content)


if __name__ == '__main__':
    request = Request()
    url = 'https://mingti.etledu.com/api/Exam/GetServerTime'
    result = request.post(url=url, data=None, headers=None)

    print(result)
