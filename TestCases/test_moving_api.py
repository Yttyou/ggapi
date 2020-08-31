"""  动态相关-接口测试用例  """
import requests
import json
import pytest
from Common import logger
import logging
import json
from Common.BaseDef import BaseDef
from Common.api_request import ApiRequest
from TestData.moving_api_data import MovingApiData

from Common import path_config
import random
import time


TOKEN = ''      # 用来存储token
KEYS = ''       # 用来存储key
ID = ''         # 用户id
UID = ''        # 用户uid
STATE_ID = ''   # 动态id

# 共用部分
def share_request(titel, data):
    logging.info("=================================================================")
    logging.info("api接口测试场景：{}".format(titel))
    logging.info("===请求参数为：")
    logging.info(data)
    logging.info("TOKEN的值：{}".format(TOKEN))
    logging.info("KEYS的值：{}".format(KEYS))
    res = ApiRequest().http_request(data["url"], data["parame"], data["Method"], TOKEN, KEYS)
    response = json.loads(res.text, encoding='utf-8')
    logging.info("本次请求响应结果如下：")
    logging.info(response)
    return response

def share_request_data(titel, data):
    logging.info("=================================================================")
    logging.info("api接口测试场景：{}".format(titel))
    logging.info("===请求参数为：")
    logging.info(data)
    logging.info("TOKEN的值：{}".format(TOKEN))
    logging.info("KEYS的值：{}".format(KEYS))
    res = ApiRequest().http_request_data(data["url"], data["parame"], data["Method"], TOKEN, KEYS)
    response = json.loads(res.text, encoding='utf-8')
    logging.info("本次请求响应结果如下：")
    logging.info(response)
    return response


# 动态相关
class TestMovingApi:

    # 用户登录
    @pytest.mark.demo
    def test_api_001(self):
        titel = "手机号登录-正确场景"
        data = MovingApiData.api_data_001
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
            global TOKEN, KEYS, ID, UID
            TOKEN = response["ret"]["token"]  # 获取登录的token
            KEYS = response["ret"]["key"]
            ID = response["ret"]["id"]
            UID = response["ret"]["uuid"]
            logging.info("获取登录后的token的值为：{}".format(TOKEN))
        except:
            logging.exception("code断言失败了！")
            raise

    # 发布一个动态
    @pytest.mark.all
    def test_api_002(self):
        titel = "发布一个动态"
        data = MovingApiData.api_data_002
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            try:
                assert response['ret'] is not None
                logging.info("检查成功，返回中有数据")
            except:
                logging.exception("检查失败！返回没有数据")

    # 广场动态
    @pytest.mark.demo
    def test_api_003(self):
        titel = "广场动态"
        data = MovingApiData.api_data_003
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查动态返回有无数据")
            try:
                assert response['ret'] is not None
                global STATE_ID
                STATE_ID = response['ret'][0]['id']
                logging.info("检查成功，获取第一个动态id为 {}".format(STATE_ID))
            except:
                logging.exception("检查失败！返回动态列表中没有数据或异常！")
                raise

    # 广场-关注-关注动态展示位
    @pytest.mark.all
    def test_api_004(self):
        titel = "广场-关注-关注动态展示位"
        data = MovingApiData.api_data_004
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 个人主页详情-动态列表
    @pytest.mark.all
    def test_api_005(self):
        titel = "个人主页详情-动态列表"
        data = MovingApiData.api_data_005
        data['parame']['visiter'] = UID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：动态列表数据检查")
            try:
                assert response['ret'] is not None
                logging.info("检查成功。个人动态详情页共有 {} 个动态".format(len(response['ret'])))
            except:
                logging.exception("检查失败！返回动态列表数据为空或异常！")
                raise

    # 动态详情
    @pytest.mark.all
    def test_api_006(self):
        titel = "动态详情"
        data = MovingApiData.api_data_006
        data['parame']['id'] = STATE_ID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：动态列表数据检查")
            try:
                assert response['ret'] is not None
                logging.info("检查成功。动态的标题内容为 {}".format(response['ret']['title']))
            except:
                logging.exception("检查失败！返回动态为空或异常！")
                raise

    # 动态详情(动态id不存在)
    @pytest.mark.demo
    def test_api_007(self):
        titel = "动态详情(动态id不存在)"
        data = MovingApiData.api_data_007
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise



    # 获取动态评论及礼物列表
    # @pytest.mark.demo
    def test_api_009(self):
        titel = "获取动态评论及礼物列表"
        data = MovingApiData.api_data_009
        data['parame'] = STATE_ID
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise













