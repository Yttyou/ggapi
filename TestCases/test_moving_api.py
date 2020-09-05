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
    @pytest.mark.all
    @pytest.mark.all
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

    # 广场动态
    @pytest.mark.all
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

    # 给动态列表中第一条发布的动态操作
    @pytest.mark.all
    def test_api_002_a(self):
        titel = "给动态列表中第一条发布的动态点赞操作"
        data = MovingApiData.api_data_002_a
        data['parame']['f_table_id'] = STATE_ID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：第一个动态的点赞总数和点赞状态")
            try:
                assert response['ret'] is not None
                if response['ret']['status'] == 0:
                    logging.info("取消点赞成功。当前第一个动态点赞的总数为 {} ".format(response['ret']['like_count']))
                else:
                    logging.info("点赞成功。当前第一个动态点赞的总数为 {} ".format(response['ret']['like_count']))
            except:
                logging.exception("点赞操作失败！")
            else:
                logging.info("检查③：再次点赞操作第一个动态的点赞总数和点赞状态")
                response = share_request_data(titel, data)
                try:
                    assert response['ret'] is not None
                    if response['ret']['status'] == 0:
                        logging.info("取消点赞成功。当前第一个动态点赞的总数为 {} ".format(response['ret']['like_count']))
                    else:
                        logging.info("点赞成功。当前第一个动态点赞的总数为 {} ".format(response['ret']['like_count']))
                except:
                    logging.exception("点赞操作失败！")

    # 发布一个动态(视频)
    @pytest.mark.all
    def test_api_002(self):
        titel = "发布一个动态(视频)"
        data = MovingApiData.api_data_002
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("检查成功.发布动态(视频)正常")
        except:
            logging.exception("检查失败.发布动态(视频)出现问题！")
            raise

    # 发布一个动态(图片)
    @pytest.mark.all
    def test_api_002_b(self):
        titel = "发布一个动态(图片)"
        data = MovingApiData.api_data_002_b
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("检查成功.发布动态(图片)正常.")
        except:
            logging.exception("检查失败.发布动态(图片)出现问题！")
            raise

    # 给自己发布的动态点赞操作
    @pytest.mark.all
    def test_api_003_a(self):     # （自己发布的一条动态成为第一条）
        titel = "给自己发布的动态点赞操作"
        data = MovingApiData.api_data_002_a
        data['parame']['f_table_id'] = STATE_ID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：第一个动态的点赞总数和点赞状态")
            try:
                assert response['ret'] is not None
                if response['ret']['status'] == 0:
                    logging.info("取消点赞成功。当前第一个动态点赞的总数为 {} ".format(response['ret']['like_count']))
                else:
                    logging.info("点赞成功。当前第一个动态点赞的总数为 {} ".format(response['ret']['like_count']))
            except:
                logging.exception("点赞操作失败！")
            else:
                logging.info("检查③：再次点赞操作第一个动态的点赞总数和点赞状态")
                response = share_request_data(titel, data)
                try:
                    assert response['ret'] is not None
                    if response['ret']['status'] == 0:
                        logging.info("取消点赞成功。当前第一个动态点赞的总数为 {} ".format(response['ret']['like_count']))
                    else:
                        logging.info("点赞成功。当前第一个动态点赞的总数为 {} ".format(response['ret']['like_count']))
                except:
                    logging.exception("点赞操作失败！")

    # 动态点赞错误流
    @pytest.mark.all
    def test_api_003_b(self):
        titel = "动态点赞错误流"
        data = MovingApiData.api_data_003_b
        response = share_request_data(titel, data)
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
                global STATE_ID
                STATE_ID = response['ret'][0]['id']
                logging.info("检查成功。个人动态详情页共有 {} 个动态".format(len(response['ret'])))
            except:
                logging.exception("检查失败！返回动态列表数据为空或异常！")
                raise

    # 删除动态
    @pytest.mark.all
    def test_api_003_c(self):
        titel = "删除动态"
        data = MovingApiData.api_data_003_c
        data['parame']['id'] = STATE_ID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 删除动态(动态ID不存在)
    @pytest.mark.all
    def test_api_003_d(self):
        titel = "动态ID不存在"
        data = MovingApiData.api_data_003_d
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 删除动态(非自己发的动态)
    @pytest.mark.all
    def test_api_003_e(self):
        titel = "删除动态(非自己发的动态)"
        data = MovingApiData.api_data_003_e
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
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
    @pytest.mark.all
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

    # 给动态评论
    @pytest.mark.all
    def test_api_008(self):
        titel = "给动态评论"
        logging.info("前置条件：获取动态列表中第一个动态id")
        data = MovingApiData.api_data_003
        response = share_request(titel, data)
        global STATE_ID
        STATE_ID = response['ret'][0]['id']
        data = MovingApiData.api_data_008
        data['parame']['f_table_id'] = STATE_ID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 获取动态评论及礼物列表
    @pytest.mark.all
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

    # 广场-关注-关注动态展示位
    @pytest.mark.all
    def test_api_010(self):
        titel = "广场-关注-关注动态展示位"
        data = MovingApiData.api_data_010
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：关注列表动态数据")
            try:
                assert len(response['ret']) > 0
                logging.info("检查成功，动态有 {} 条".format(len(response['ret'])))
            except:
                logging.exception("检查失败！没有返回数据")
                raise









