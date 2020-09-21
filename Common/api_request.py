"""  发起HTTP请求方法  """
import requests
from Common import logger
import logging
import random
import string
import json

class ApiRequest:
    # 接口请求头，每个接口必传
    def http_headers(self,Token,keys):
        """
        :param Token: 传入token
        :return: 返回请求头headers
        """
        if Token == '':
            Token = 'E0BFB7F8B55B7293F39C641D76790F75D25A34B9C2A87DB380ECD7F7115882EC'
        if keys == '':
            keys = 'D951406E0C41E664DBA079F6E0D066F9D25A34B9C2A87DB380ECD7F7115882EC'
        headers = {"Authorization": "Bear " + Token,
                   "clientKey": keys,
                   "random": ''.join(random.sample(string.ascii_letters + str(random.randint(9999999, 100000000)), k=32)),
                   "lng": "116.397128",
                   "lat": "39.916527",
                   "mac": ''.join(random.sample(string.ascii_letters + str(random.randint(9999999, 100000000)), k=15)),
                   "deviceinfo": "iOS 11.3",
                   "ip": "223.75.238.173",
                   "appversion": "1.0.2",
                   "apppt": "2",
                   "isNoEncryption": "1",
                   "channelId": "1",         # 配置说明：呱呱--1；团团--29
                   }
        return headers

    def http_request(self, URL, Param, Method, Token, keys):
        header = self.http_headers(Token,keys)
        logging.info("本次请求头：")
        logging.info(header)
        if Method.upper() == "GET":
            try:
                response=requests.get(URL, headers=header, params=Param)
                time_data = response.elapsed.total_seconds()
                logging.info("本次get请求响应时间为：{}".format(time_data))
            except Exception as e:
                logging.exception("get请求出错：{0}".format(e))
                raise e
        elif Method.upper() == "POST":
            try:
                response=requests.post(URL,headers=header,json=Param,verify=False)
                time_data = response.elapsed.total_seconds()
                logging.info("本次post请求响应时间为：{}".format(time_data))
                logging.info("post接口请求成功！")
            except Exception as e:
                logging.exception("post请求出错：{0}".format(e))
                raise e
        else:
            logging.info("请求类型出错了！")
            response = "请求类型出错了！"
        return response

    def http_request_data(self, URL, Param, Method, Token, keys):
        header = self.http_headers(Token,keys)
        logging.info("本次请求头：")
        logging.info(header)
        if Method.upper() == "GET":
            try:
                response=requests.get(URL, headers=header, params=Param)
                time_data = response.elapsed.total_seconds()
                logging.info("本次get请求响应时间为：{}".format(time_data))
            except Exception as e:
                logging.exception("get请求出错：{0}".format(e))
                raise e
        elif Method.upper() == "POST":
            try:
                response=requests.post(URL,data=Param,headers=header,verify=False)
                time_data = response.elapsed.total_seconds()
                logging.info("本次post请求响应时间为：{}".format(time_data))
                logging.info("post接口请求成功！")
            except Exception as e:
                logging.exception("post请求出错：{0}".format(e))
                raise e
        else:
            logging.info("请求类型出错了！")
            response = "请求类型出错了！"
        return response

