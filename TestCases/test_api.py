"""  接口测试用例  """
import requests
import json
import pytest
from Common import logger
import logging
import json
from Common.BaseDef import BaseDef
from Common.api_request import ApiRequest
from TestData.api_data import UserData,LiveRoomApi,GiftApi,ChatRoomApi,OtherApi
from TestData.api_data import OrderApi, SkillRelatedApi
from TestData import api_data
from Common import path_config
import random
import time

TOKEN = ''      # 用来存储token
KEYS = ''       # 用来存储key
PL_TOKEN = ''   # 用来存储大神的token
PL_KEYS = ''    # 用来存储大神的key
ID = ''         # 用来存储用户id或聊天室id
NICK_NAME = '更改昵称'  # 用来存储用户的昵称
UUID = ''       # 用来存储UUID
STATE_ID = ''    # 用来存储动态id
STATE_USER_ID = '' # 用来存储发送动态用户的id
TRADE_NO = ''      # 存储订单流失号
ORDER_AMOUNT = ''   # 存储订单金额
GB_Amount = ''      # 存储用户的呱币余额
PL_GB_Amount = ''   # 存储大神当前的呱币收入

BY_MIC_ID = []     # 房主通过用户上麦麦位id
MIC_USER_ID = ''    # 麦位上的用户id

SKILL_ID = ''      # 大神的技能ID
ORDER_ID = ''      # 订单ID
USID = ''          # 技能id

chat_item_list = []        # 聊天室麦位列表
user_A_udid = ''           # 房间中用户A的udid
user_B_udid = ''           # 房间中用户B的udid

APPLY_MIKE_USER_list = ''    # 申请上麦列表

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

# 大神使用的请求(使用的token、key不同)
def player_share_request(titel, data):
    logging.info("=================================================================")
    logging.info("api接口测试场景：{}".format(titel))
    logging.info("===请求参数为：")
    logging.info(data)
    logging.info("TOKEN的值：{}".format(PL_TOKEN))
    logging.info("KEYS的值：{}".format(PL_KEYS))
    res = ApiRequest().http_request(data["url"], data["parame"], data["Method"], PL_TOKEN, PL_KEYS)
    response = json.loads(res.text, encoding='utf-8')
    logging.info("本次请求响应结果如下：")
    logging.info(response)
    return response

# 大神使用的请求(使用的token、key不同)
def player_share_request_data(titel, data):
    logging.info("=================================================================")
    logging.info("api接口测试场景：{}".format(titel))
    logging.info("===请求参数为：")
    logging.info(data)
    logging.info("TOKEN的值：{}".format(PL_TOKEN))
    logging.info("KEYS的值：{}".format(PL_KEYS))
    res = ApiRequest().http_request_data(data["url"], data["parame"], data["Method"], PL_TOKEN, PL_KEYS)
    response = json.loads(res.text, encoding='utf-8')
    logging.info("本次请求响应结果如下：")
    logging.info(response)
    return response

# 获取聊天室中-有效的礼物（钻石）
def get_gift_a():
    data = GiftApi.api_get_gift_a
    titel = "获取有效的礼物（钻石）"
    response = share_request(titel, data)
    gift_bumber = len(response["ret"]["data"])          # 礼物个数
    gift = response["ret"]["data"][random.randint(0,4)]    # 1-5序列礼物中随机选中一个礼物
    gift_name = gift["name"]
    gift_id = gift["id"]
    logging.info("获取到的钻石礼物个数为：{} 个".format(gift_bumber))
    logging.info("其中一个礼物名称为 ‘{}’，礼物id为 ‘{}’".format(gift_name, gift_id))
    return gift_id  # 返回礼物id

# 获取聊天室中-过期的礼物（钻石）
def get_gift_b():
    data = GiftApi.api_get_gift_b
    titel = "获取聊天室中-过期的礼物（钻石）"
    response = share_request(titel, data)
    gift_bumber = len(response["ret"]["data"])    # 礼物个数
    gift = response["ret"]["data"][random.randint(0,4)]    # 1-5序列礼物中随机选中一个礼物
    gift_name = gift["name"]
    gift_id = gift["id"]
    logging.info("获取到的钻石礼物个数为：{} 个".format(gift_bumber))
    logging.info("其中一个礼物名称为 ‘{}’，礼物id为 ‘{}’".format(gift_name, gift_id))
    return gift_id  # 返回礼物id

# 获取呱币礼物(有效)
def get_gift_c():
    data = GiftApi.api_get_gift_c
    titel = "获取呱币礼物(有效)"
    response = share_request(titel, data)
    gift_bumber = len(response["ret"]["data"])    # 礼物个数
    gift = response["ret"]["data"][random.randint(0,4)]    # 1-5序列礼物中随机选中一个礼物
    gift_name = gift["name"]
    gift_id = gift["id"]
    logging.info("获取到的有效呱币礼物个数为：{} 个".format(gift_bumber))
    logging.info("第一个礼物名称为 ‘{}’，礼物id为 ‘{}’".format(gift_name, gift_id))
    return gift_id  # 返回礼物id

# 获取呱币礼物(无效)
def get_gift_d():
    data = GiftApi.api_get_gift_d
    titel = "获取呱币礼物(无效)"
    response = share_request(titel, data)
    gift_bumber = len(response["ret"]["data"])    # 礼物个数
    gift = response["ret"]["data"][random.randint(0,4)]    # 1-5序列礼物中随机选中一个礼物
    gift_name = gift["name"]
    gift_id = gift["id"]
    logging.info("获取到的无效呱币礼物个数为：{} 个".format(gift_bumber))
    logging.info("第一个礼物名称为 ‘{}’，礼物id为 ‘{}’".format(gift_name, gift_id))
    return gift_id  # 返回礼物id

# 获取礼盒(有效)
def get_box():
    data = GiftApi.api_get_box
    titel = "获取礼盒(有效)"
    response = share_request(titel, data)
    box_bumber = len(response["ret"]["data"])    # 礼盒个数
    if box_bumber <= 3:
        box = response["ret"]["data"][random.randint(0,box_bumber-1)]
    else:
        box = response["ret"]["data"][random.randint(0,4)]    # 1-5序列礼盒中随机选中一个礼物
    gift_name = box["name"]
    box_id = box["id"]
    logging.info("获取到的有效礼盒个数为：{} 个".format(box_bumber))
    logging.info("第一个礼盒名称为 ‘{}’，礼盒id为 ‘{}’".format(gift_name, box_id))
    return box_id  # 返回礼盒id

# 将数据写入文件
def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    file.writelines(data)
    file.close()
    print("保存文件成功")

"""  以下是测试用例   """

# 用户相关
class TestUserRelated:

    # 批量手机号注册
    @pytest.mark.login
    def test_iphone_login(self):
        iphone_list = []
        titel = "批量手机号注册"
        number = 1
        iphone = int(BaseDef().random_iphone())
        success_number =0           # 记录注册成功次数
        while number <=50:
            data = UserData.api_iphone_login
            data['parame']['phonenum'] = iphone
            response = share_request(titel, UserData.api_iphone_login)
            logging.info("第 {} 次注册。。。手机号为 {}".format(number,iphone))
            time.sleep(1)
            if response['code'] == data["expect"]:
                token = response["ret"]["token"]  # 获取登录的token
                key = response["ret"]["key"]
                data = token+","+key+"\n"
                text_save('F:\API_TEST\TestData\sd.csv', data)
                iphone_list.append(iphone)
                success_number = success_number+1
                if success_number >=50:
                    break
                logging.info("注册成功！")
            else:
                logging.exception("注册失败！")
            number = number + 1
            iphone = iphone + 1
        print(iphone_list)
        logging.info(iphone_list)

    # 手机号注册-输入错误手机号
    @pytest.mark.all
    def test_api_001(self):
        titel = "手机号注册-输入错误手机号"
        data = UserData.api_data_001
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 手机号注册
    @pytest.mark.all
    def test_api_002(self):
        titel = "手机号注册"
        data = UserData.api_data_002
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 发送验证码（登录时）
    @pytest.mark.all
    def test_api_send_code_01(self):
        titel = "发送验证码（登录时）"
        data = UserData.api_send_code_01
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 发送验证码（忘记密码）
    @pytest.mark.all
    def test_api_send_code_02(self):
        titel = "发送验证码（忘记密码）"
        data = UserData.api_send_code_02
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 注册成功后验证用户是否存在
    @pytest.mark.all
    def test_api_003(self):
        titel = "注册成功后验证用户是否存在"
        data = UserData.api_data_003
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 手机号登录-手机号未注册
    @pytest.mark.all
    def test_api_004(self):
        titel = "手机号登录-手机号未注册"
        data = UserData.api_data_004
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 手机号登录-输入错误的密码
    @pytest.mark.all
    def test_api_005(self):
        titel = "手机号登录-输入错误的密码"
        data = UserData.api_data_005
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            try:
                assert response['message'] == data["message"]
                logging.info("message断言成功.")
            except:
                logging.exception("message断言失败了！实际结果为'{}',期望结果为'{}'".format(response['message'],data["message"]))
                raise

    # 忘记密码
    @pytest.mark.all
    def test_api_006(self):
        titel = "忘记密码"
        data = UserData.api_data_006_a
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            # 修改密码成功后使用旧密码登录，预期结果失败
            logging.info("===== 验证1：修改密码成功后使用旧密码登录，预期结果失败 =====")
            data = UserData.api_data_006_b
            response = share_request(titel, data)
            try:
                assert response['code'] == data["expect"]
                logging.info("code断言成功.")
            except:
                logging.exception("code断言失败了！实际结果为'{}',期望结果为'{}'".format(response['code'],data["expect"]))
                raise
            else:
                # 修改密码成功后使用新密码登录，可登录成功
                logging.info("===== 验证2：修改密码成功后使用新密码登录，可登录成功 =====")
                data = UserData.api_data_006_c
                response = share_request(titel, data)
                try:
                    assert response['code'] == data["expect"]
                    logging.info("code断言成功.")
                except:
                    logging.exception("code断言失败了！实际结果为'{}',期望结果为'{}'".format(response['code'], data["expect"]))
                    raise

    # 手机号登录-正确场景
    @pytest.mark.ytt
    @pytest.mark.gift
    @pytest.mark.play
    @pytest.mark.demo
    def test_api_007(self):
        titel = "手机号登录-正确场景"
        logging.info("用例前置：将账号修改密码还原为'{}'".format(api_data.pwd))
        data = UserData.api_data_007_a
        global TOKEN, KEYS, ID
        res = ApiRequest().http_request(data["url"], data["parame"], data["Method"], TOKEN, KEYS)
        response = res.json()
        logging.info("本次请求响应结果如下：")
        logging.info(response)
        data = UserData.api_data_007_b
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
            TOKEN = response["ret"]["token"]         # 获取登录的token
            KEYS = response["ret"]["key"]
            ID = response["ret"]["id"]
            logging.info("获取登录后的token的值为：{}".format(TOKEN))
        except:
            logging.exception("code断言失败了！")
            raise

    # (登录后)修改密码
    @pytest.mark.all
    def test_api_008(self):
        titel = "(登录后)修改密码"
        data = UserData.api_data_008_a
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            # 修改密码成功后使用旧密码登录，预期结果失败
            logging.info("===== 验证1：修改密码成功后使用旧密码登录，预期结果失败 =====")
            data = UserData.api_data_008_b
            response = share_request(titel, data)
            try:
                assert response['code'] == data["expect"]
                logging.info("code断言成功.")
            except:
                logging.exception("code断言失败了！实际结果为'{}',期望结果为'{}'".format(response['code'], data["expect"]))
                raise
            else:
                # 修改密码成功后使用新密码登录，可登录成功
                logging.info("===== 验证2：修改密码成功后使用新密码登录，可登录成功 =====")
                data = UserData.api_data_008_c
                response = share_request(titel, data)
                try:
                    assert response['code'] == data["expect"]
                    logging.info("code断言成功.")
                except:
                    logging.exception("code断言失败了！实际结果为'{}',期望结果为'{}'".format(response['code'], data["expect"]))
                    raise

    # 获取个人信息
    @pytest.mark.all
    def test_api_009(self):
        titel = "获取个人信息"
        data = UserData.api_data_009
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 更新个人信息
    @pytest.mark.all
    def test_api_010(self):
        titel = "更新个人信息"
        data = UserData.api_data_010
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            try:
                assert response['ret']["nick_name"] == data["expect_name"]
                global NICK_NAME
                NICK_NAME = response['ret']["nick_name"]
                logging.info("用户昵称检查成功")
            except:
                logging.exception("用户昵称检查失败了！实际结果是'{}'，期望结果是'{}'".format(response['ret']["nick_name"],data["expect_name"]))
                raise

    # 根据id获取用户信息-id存在
    @pytest.mark.all
    def test_api_011(self):
        titel = "根据id获取用户信息-id存在"
        data = UserData.api_data_011
        data["parame"]["id"] = ID
        logging.info("获取到ID的值为'{}'".format(ID))
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 根据id获取用户信息-id不存在
    @pytest.mark.all
    def test_api_012(self):
        titel = "根据id获取用户信息-id不存在"
        data = UserData.api_data_012
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 获取用户列表
    @pytest.mark.all
    def test_api_013(self):
        titel = "获取用户列表"
        data = UserData.api_data_013
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            try:
                user_number = len(response['ret']["data"])
                assert user_number > int(data["usernumber"])
                logging.info("检查成功，列表中用户数为：{}".format(user_number))
            except:
                logging.exception("获取列表中的用户数量异常！")
                raise

    # 获取用户列表-筛选带装扮
    @pytest.mark.all
    def test_api_014(self):
        titel = "获取用户列表-筛选带装扮"
        data = UserData.api_data_014
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查列表中用户的数量")
            try:
                user_number = len(response['ret']["data"])
                assert user_number > int(data["usernumber"])
                logging.info("检查成功，列表中用户数为：{}".format(user_number))
            except:
                logging.exception("获取列表中的用户数量异常！")
                raise

    # 获取用户列表-通过uuid筛选
    @pytest.mark.all
    def test_api_015(self):
        titel = "获取用户列表-通过uuid筛选"
        data = UserData.api_data_015
        data["parame"]["search_word"] = ID
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            try:
                user_number = len(response['ret']["data"])
                assert user_number == int(data["usernumber"])
                logging.info("检查成功，列表中用户数为：{}".format(user_number))
            except:
                logging.exception("获取列表中的用户数量异常！")
                raise

    # 获取用户列表-通过昵称模糊筛选
    @pytest.mark.all
    def test_api_016(self):
        titel = "获取用户列表-通过昵称模糊筛选"
        data = UserData.api_data_016
        data["parame"]["search_word"] = NICK_NAME
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            try:
                user_number = len(response['ret']["data"])
                assert user_number == int(data["usernumber"])
                logging.info("检查成功，列表中用户数为：{}".format(user_number))
            except:
                logging.exception("获取列表中的用户数量异常！")
                raise

    # 获取用户列表-通过昵称完全匹配
    @pytest.mark.all
    def test_api_017(self):
        titel = "获取用户列表-通过昵称完全匹配"
        data = UserData.api_data_017
        data["parame"]["accurate_search_word"] = NICK_NAME
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            try:
                user_number = len(response['ret']["data"])
                assert user_number == int(data["usernumber"])
                logging.info("检查成功，列表中用户数为：{}".format(user_number))
            except:
                logging.exception("获取列表中的用户数量异常！")
                raise

    # 获取实人认证审核状态
    @pytest.mark.all
    def test_api_018(self):
        titel = "获取实人认证审核状态"
        data = UserData.api_data_018
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
            AUDIT_STATUS = response['ret']['audit_status']
            logging.info("此时用户认证的审核状态为: {}".format(AUDIT_STATUS))
        except:
            logging.exception("code断言失败了！")
            raise

    # 发起阿里云实人认证请求
    @pytest.mark.all
    def test_api_019(self):
        titel = "发起阿里云实人认证请求"
        data = UserData.api_data_019
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 获取兴趣列表
    @pytest.mark.all
    def test_api_020(self):
        titel = "获取兴趣列表"
        data = UserData.api_data_020
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查兴趣的个数")
            ret_number = len(response['ret'])
            try:
                assert ret_number >= 0
                logging.info("兴趣个数检查成功！共有 {} 个兴趣".format(ret_number))
            except:
                logging.exception("兴趣个数检查异常！")
                raise

    # 根据条件（页码）赛选获取兴趣列表
    @pytest.mark.all
    def test_api_021(self):
        titel = "根据条件（页码）赛选获取兴趣列表"
        data = UserData.api_data_021
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查兴趣的个数")
            ret_number = len(response['ret'])
            try:
                assert ret_number >= 0
                logging.info("兴趣个数检查成功！共有 {} 个兴趣".format(ret_number))
            except:
                logging.exception("兴趣个数检查异常！")
                raise

    # 绑定/取消第三方账号（微信）
    @pytest.mark.all
    def test_api_022(self):
        titel = "绑定/取消第三方账号（微信）"
        logging.info("获取用户是否绑定微信的状态。。。")
        data = UserData.api_data_022_a
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("通过状态对用户进行绑定/解绑操作")
            if response['ret']['is_exist'] == "0":
                logging.info("当前账号还没有绑定微信，接下来进行绑定操作。。")
                data = UserData.api_data_022_b
                response = share_request(titel, data)
                try:
                    assert response['code'] == data["expect"]
                    logging.info("code断言成功.")
                except:
                    logging.exception("code断言失败了！")
                    raise
                else:
                    logging.info("绑定微信后再次获取状态。。。")
                    data = UserData.api_data_022_a
                    response = share_request(titel, data)
                    try:
                        assert response['ret']['is_exist'] == "1"
                        logging.info("绑定成功，状态为'{}'".format(response['ret']['is_exist']))
                    except:
                        logging.exception("绑定微信发生错误，绑定后状态为'{}'！".format(response['ret']['is_exist']))
                        raise
            else:
                logging.info("当前账号已绑定微信，接下来进行解绑。。")
                data = UserData.api_data_022_c
                response = share_request(titel, data)
                try:
                    assert response['code'] == data["expect"]
                    logging.info("code断言成功.")
                except:
                    logging.exception("code断言失败了！")
                    raise
                else:
                    logging.info("解绑微信后再次获取状态。。。")
                    data = UserData.api_data_022_a
                    response = share_request(titel, data)
                    try:
                        assert response['ret']['is_exist'] == "0"
                        logging.info("解绑成功，状态为'{}'".format(response['ret']['is_exist']))
                    except:
                        logging.exception("解绑微信发生错误，解绑后状态为'{}'！".format(response['ret']['is_exist']))
                        raise

    # 绑定/取消第三方账号（QQ）
    @pytest.mark.all
    def test_api_023(self):
        titel = "绑定/取消第三方账号（QQ）"
        logging.info("获取用户是否绑定QQ的状态。。。")
        data = UserData.api_data_023_a
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("通过状态对用户进行绑定/解绑QQ操作")
            if response['ret']['is_exist'] == "0":
                logging.info("当前账号还没有绑定QQ，接下来进行绑定操作。。")
                data = UserData.api_data_023_b
                response = share_request(titel, data)
                try:
                    assert response['code'] == data["expect"]
                    logging.info("code断言成功.")
                except:
                    logging.exception("code断言失败了！")
                    raise
                else:
                    logging.info("绑定QQ后再次获取状态。。。")
                    data = UserData.api_data_023_a
                    response = share_request(titel, data)
                    try:
                        assert response['ret']['is_exist'] == "1"
                        logging.info("绑定成功，状态为'{}'".format(response['ret']['is_exist']))
                    except:
                        logging.exception("绑定QQ发生错误，绑定后状态为'{}'！".format(response['ret']['is_exist']))
                        raise
            else:
                logging.info("当前账号已绑定QQ，接下来进行解绑。。")
                data = UserData.api_data_023_c
                response = share_request(titel, data)
                try:
                    assert response['code'] == data["expect"]
                    logging.info("code断言成功.")
                except:
                    logging.exception("code断言失败了！")
                    raise
                else:
                    logging.info("解绑QQ后再次获取状态。。。")
                    data = UserData.api_data_023_a
                    response = share_request(titel, data)
                    try:
                        assert response['ret']['is_exist'] == "0"
                        logging.info("解绑成功，状态为'{}'".format(response['ret']['is_exist']))
                    except:
                        logging.exception("解绑QQ发生错误，解绑后状态为'{}'！".format(response['ret']['is_exist']))
                        raise

    # 绑定/取消第三方账号（appleId）
    @pytest.mark.all
    def test_api_024(self):
        titel = "绑定/取消第三方账号（appleId）"
        logging.info("获取用户是否绑定appleId的状态。。。")
        data = UserData.api_data_024_a
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("通过状态对用户进行绑定/解绑appleId操作")
            if response['ret']['is_exist'] == "0":
                logging.info("当前账号还没有绑定appleId，接下来进行绑定操作。。")
                data = UserData.api_data_024_b
                response = share_request(titel, data)
                try:
                    assert response['code'] == data["expect"]
                    logging.info("code断言成功.")
                except:
                    logging.exception("code断言失败了！")
                    raise
                else:
                    logging.info("绑定appleId后再次获取状态。。。")
                    data = UserData.api_data_024_a
                    response = share_request(titel, data)
                    try:
                        assert response['ret']['is_exist'] == "1"
                        logging.info("绑定成功，状态为'{}'".format(response['ret']['is_exist']))
                    except:
                        logging.exception("绑定appleId发生错误，绑定后状态为'{}'！".format(response['ret']['is_exist']))
                        raise
            else:
                logging.info("当前账号已绑定appleId，接下来进行解绑。。")
                data = UserData.api_data_024_c
                response = share_request(titel, data)
                try:
                    assert response['code'] == data["expect"]
                    logging.info("code断言成功.")
                except:
                    logging.exception("code断言失败了！")
                    raise
                else:
                    logging.info("解绑appleId后再次获取状态。。。")
                    data = UserData.api_data_024_a
                    response = share_request(titel, data)
                    try:
                        assert response['ret']['is_exist'] == "0"
                        logging.info("解绑成功，状态为'{}'".format(response['ret']['is_exist']))
                    except:
                        logging.exception("解绑appleId发生错误，解绑后状态为'{}'！".format(response['ret']['is_exist']))
                        raise

    # 重复绑定第三方账号(QQ)
    @pytest.mark.all
    def test_api_025(self):
        titel = "重复绑定第三方账号(QQ)"
        data = UserData.api_data_025_a
        share_request(titel, data)          # 第一次绑定
        time.sleep(2)
        data = UserData.api_data_025_b     # 重复绑定
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 重复取消绑定第三方账号(微信)
    @pytest.mark.all
    def test_api_026(self):
        titel = "重复取消绑定第三方账号(微信)"
        data = UserData.api_data_026
        share_request(titel, data)       # 第一次绑定
        time.sleep(2)
        data = UserData.api_data_026     # 重复绑定
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise


# 直播间
class TestLiveRoom:

    # 首页直播间推荐列表
    @pytest.mark.all
    def test_api_027(self):
        titel = "首页直播间推荐列表"
        data = LiveRoomApi.api_data_027
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查直播间个数并获取第一个直播间名字")
            live_room_number = len(response['ret'])
            one_room_name = response['ret'][0]["name"]
            try:
                assert live_room_number > 0
                logging.info("检查成功，有找到直播间，其中一个直播间名字为 '{}'".format(one_room_name))
            except:
                logging.exception("查找直播间发现异常！")
                raise

    # 首页-动态推荐位(默认)
    @pytest.mark.all
    def test_api_028(self):
        titel = "首页-动态推荐位(默认)"
        data = LiveRoomApi.api_data_028
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查直播间个数并获取第一个直播间名字")
            live_room_number = len(response['ret'])
            one_room_name = response['ret'][0]["title"]
            try:
                assert live_room_number > 0
                logging.info("检查成功，有找到直播间，其中一个直播间名字为 '{}'".format(one_room_name))
            except:
                logging.exception("查找直播间发现异常！")
                raise

    # 首页-动态推荐位(选择展示)
    @pytest.mark.all
    def test_api_029(self):
        titel = "首页-动态推荐位(选择展示)"
        data = LiveRoomApi.api_data_029
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查直播间个数并获取第一个直播间名字")
            live_room_number = len(response['ret'])
            one_room_name = response['ret'][0]["title"]
            try:
                assert live_room_number > 0
                logging.info("检查成功，有找到 {} 个直播间，其中一个直播间名字为 '{}'".format(live_room_number,one_room_name))
            except:
                logging.exception("查找直播间发现异常！")
                raise

    # 首页-娱乐交友，游戏组队直播间
    @pytest.mark.all
    def test_api_030(self):
        titel = "首页-娱乐交友，游戏组队直播间"
        data = LiveRoomApi.api_data_030
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise

    # 检查派单大厅列表展示及个数
    @pytest.mark.all
    def test_api_031(self):
        titel = "检查派单大厅列表展示及个数"
        data = LiveRoomApi.api_data_031
        response = share_request(titel, data)
        number = len(response["ret"])
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功,且派单任务共有 {} 个".format(number))
        except:
            logging.exception("code断言失败了！")
            raise


# 聊天室相关
class TestChatRoom:

    # 根据条件获取聊天室信息
    @pytest.mark.all
    @pytest.mark.parametrize("data", ChatRoomApi.api_data_032)
    def test_api_032(self, data):
        titel = "获取聊天室信息条件-{}".format(data["chat_title"])
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查聊天室信息")
            gift_number = len(response["ret"]["data"])
            if gift_number > 0:
                one_gift_name = response["ret"]["data"][0]["name"]
                logging.info("筛选后聊天室tab中有 {} 个聊天室，其中一个聊天室名称为 '{}'".format(gift_number, one_gift_name))
            else:
                logging.info("筛选后当前列表没有聊天室！")

    # 默认展示聊天室信息
    @pytest.mark.all
    def test_api_033(self):
        titel = "默认展示聊天室信息"
        data = ChatRoomApi.api_data_033
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查聊天室信息")
            gift_number = len(response["ret"]["data"])
            if gift_number > 0:
                one_gift_name = response["ret"]["data"][0]["name"]
                logging.info("聊天室tab中有 {} 个聊天室，其中一个聊天室名称为 '{}'".format(gift_number, one_gift_name))
                global ID
                ID = response["ret"]["data"][0]["id"]
            else:
                logging.info("当前列表没有聊天室！")

    # 根据id获取聊天室信息
    @pytest.mark.all
    def test_api_034(self):
        titel = "根据id获取聊天室信息"
        logging.info("前置条件：获取已开聊天室的ID")
        data = ChatRoomApi.api_data_034_a
        response = share_request(titel, data)
        chatroom_list = response['ret']['data']
        logging.info("当前有聊天室 {} 个".format(len(chatroom_list)))
        global ID
        if len(chatroom_list) <5:
            ID = chatroom_list[0]['id']
        else:
            ID = chatroom_list[random.randint(0,4)]['id']    # 从前5个聊天室中选一个
        data = ChatRoomApi.api_data_034_b
        data["parame"]["id"] = ID
        logging.info("此时获取到的全局变量ID为：{}".format(ID))
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查搜索结果聊天室id是否正确")
            try:
                assert response['ret']["id"] == ID
                logging.info("检查成功，通过搜索聊天室id功能正常")
            except:
                logging.exception("检查失败，通过聊天室id搜索功能异常！")
                raise

    # 加入聊天室-房间编号不存在或错误
    @pytest.mark.all
    def test_api_035(self):
        titel = "加入聊天室-房间编号不存在或错误"
        data = ChatRoomApi.api_data_035
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 加入聊天室-房间编号存在
    @pytest.mark.all
    def test_api_036(self):
        titel = "加入聊天室-房间编号存在"
        logging.info("前置条件：获取已经开了聊天室的id")
        data = ChatRoomApi.api_data_036_a
        response = share_request(titel, data)
        chatroom_list = response['ret']['data']

        number = len(chatroom_list)
        logging.info("当前聊天室个数为 {} ".format(number))
        global ID
        if number <= 5:
            ID = chatroom_list[random.randint(0, number - 1)]['id']
        else:
            ID = chatroom_list[random.randint(0, 4)]['id']  # 从前5个聊天室中选一个
        data = ChatRoomApi.api_data_036_b
        data["parame"]["chatroom_id"] = ID
        logging.info("此时获取到的全局变量ID为：{}".format(ID))
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            title = response['ret']['ads'][0]['title']
            logging.info("该聊天室的标题为 ‘{}’".format(title))
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 退出聊天室-已加入聊天室
    @pytest.mark.all
    def test_api_037(self):
        titel = "退出聊天室-已加入聊天室"
        data = ChatRoomApi.api_data_037
        data["parame"]["chatroom_id"] = ID
        logging.info("此时获取到的全局变量ID为：{}".format(ID))
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 退出聊天室-聊天室不存在或不在房间中
    @pytest.mark.all
    def test_api_038(self):
        titel = "退出聊天室-聊天室不存在或不在房间中"
        data = ChatRoomApi.api_data_038
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 退出聊天室-缺少聊天室id
    @pytest.mark.all
    def test_api_039(self):
        titel = "退出聊天室-缺少聊天室id"
        data = ChatRoomApi.api_data_039
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 用户A登录，并发起上麦申请
    @pytest.mark.demo
    def test_api_040(self):
        titel = "用户A登录"
        data = ChatRoomApi.api_data_040_a
        response = share_request(titel, data)
        global TOKEN, KEYS, user_A_udid
        TOKEN = response["ret"]["token"]  # 获取登录的token
        KEYS = response["ret"]["key"]
        user_A_udid = response["ret"]["id"]
        titel = "用户A取消申请上麦"             # 为了保证用户是没有申请上麦的，所以这里需要做取消申请下麦处理
        data = ChatRoomApi.api_data_040_b
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        time.sleep(3)
        titel = "用户A申请上麦"
        data = ChatRoomApi.api_data_040
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查数据返回")
            try:
                assert len(response['ret']) > 0
                logging.info("返回数据成功，当前聊天室申请麦位数为 {} ".format(response['ret']['chatroom_mike_general_apply_num']))
            except:
                logging.exception("返回数据为空或异常！")
                raise

    # 用户B登录，并发起上麦申请
    @pytest.mark.demo
    def test_api_041(self):
        titel = "用户B登录"
        data = ChatRoomApi.api_data_041_a
        response = share_request(titel, data)
        global TOKEN, KEYS, user_B_udid
        TOKEN = response["ret"]["token"]  # 获取登录的token
        KEYS = response["ret"]["key"]
        user_B_udid = response["ret"]["id"]
        titel = "用户B取消申请上麦"             # 为了保证用户是没有申请上麦的，所以这里需要做取消申请下麦处理
        data = ChatRoomApi.api_data_040_b
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        time.sleep(3)
        titel = "用户B申请上麦"
        data = ChatRoomApi.api_data_040
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查数据返回")
            try:
                assert len(response['ret']) > 0
                logging.info("返回数据成功，当前聊天室申请麦位数为 {} ".format(response['ret']['chatroom_mike_general_apply_num']))
            except:
                logging.exception("返回数据为空或异常！")
                raise

    # 用户C登录，并加入房间获取麦位列表
    @pytest.mark.demo
    def test_api_042(self):
        titel = "用户C登录"
        data = ChatRoomApi.api_data_042_a
        response = share_request(titel, data)
        global TOKEN, KEYS
        TOKEN = response["ret"]["token"]  # 获取登录的token
        KEYS = response["ret"]["key"]

        titel = "用户C申请上麦"
        data = ChatRoomApi.api_data_040
        response = share_request(titel, data)

        titel = "加入房间"
        data = ChatRoomApi.api_data_040_c
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("获取房间的麦位情况")
            try:
                assert len(response['ret']) > 0
                global chat_item_list
                chat_item_list = response['ret']['chatroom_mike_array']  # 获取聊天室的麦位信息
            except:
                logging.exception("返回数据为空或异常！")
                raise

    # 用户D登录，并发起上麦申请
    @pytest.mark.demo
    def test_api_042_d(self):
        titel = "用户D登录"
        data = ChatRoomApi.api_data_042_d
        response = share_request(titel, data)
        global TOKEN, KEYS, user_B_udid
        TOKEN = response["ret"]["token"]  # 获取登录的token
        KEYS = response["ret"]["key"]
        user_B_udid = response["ret"]["id"]
        titel = "用户B取消申请上麦"  # 为了保证用户是没有申请上麦的，所以这里需要做取消申请下麦处理
        data = ChatRoomApi.api_data_040_b
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        time.sleep(3)
        titel = "用户D申请上麦"
        data = ChatRoomApi.api_data_040
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查数据返回")
            try:
                assert len(response['ret']) > 0
                logging.info("返回数据成功，当前聊天室申请麦位数为 {} ".format(response['ret']['chatroom_mike_general_apply_num']))
            except:
                logging.exception("返回数据为空或异常！")
                raise

    # 房主登录，开启聊天室
    @pytest.mark.demo
    def test_api_043(self):
        titel = "房主登录"
        data = ChatRoomApi.api_data_Homeowner_login
        response = share_request(titel, data)
        global TOKEN, KEYS
        TOKEN = response["ret"]["token"]  # 获取登录的token
        KEYS = response["ret"]["key"]
        titel = "开启聊天室"
        data = ChatRoomApi.api_data_043
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查房间相关数据")
            try:
                assert len(response['ret']) > 0
                logging.info("检查成功，聊天室返回有数据。")
            except:
                logging.exception("检查失败！返回的聊天室信息为空或异常")
                raise

    # 获取聊天室麦位申请列表
    @pytest.mark.demo
    def test_api_044(self):
        titel = "获取聊天室麦位申请列表"
        data = ChatRoomApi.api_data_044
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：申请列表数据")
            number = len(response['ret']['data'])
            try:
                assert number > 0
                global APPLY_MIKE_USER_list
                APPLY_MIKE_USER_list = response['ret']['data']
                logging.info("检查成功，当前房间申请上麦人数为 {}。".format(number))
            except:
                logging.exception("检查失败！返回的聊天室信息为空或异常")
                raise

    # 房主将用户A设置为主持
    @pytest.mark.demo
    def test_api_045(self):
        titel = "房主将用户A设置为主持"
        data = ChatRoomApi.api_data_045_a
        data['parame']['user_id'] = user_A_udid
        response = share_request(titel, data)       # 先取消一次主持（清理数据）
        data = ChatRoomApi.api_data_045_b
        data['parame']['user_id'] = user_A_udid
        response = share_request(titel, data)       # 设置主持
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 获取聊天室主持列表
    @pytest.mark.all
    def test_api_046(self):
        titel = "获取聊天室主持列表"
        data = ChatRoomApi.api_data_046
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 聊天室中查看用户信息
    @pytest.mark.all
    def test_api_047(self):
        titel = "聊天室中查看用户信息"
        data = ChatRoomApi.api_data_047
        data['parame']['user_id'] = APPLY_MIKE_USER_list[0]['user_id']
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：返回数据")
            try:
                assert len(response['ret'])> 0
                nick_name = response['ret']['user']['nick_name']
                logging.info("检查成功，被查看的用户昵称为 {}".format(nick_name))
            except:
                logging.exception("检查失败！聊天室中查看用户信息异常")
                raise

    # 房主更新聊天室信息
    @pytest.mark.all
    def test_api_048(self):
        titel = "房主更新聊天室信息"
        data = ChatRoomApi.api_data_048
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：修改房间数据后是否生效")
            try:
                assert response['ret']['name'] == data["parame"]['name']
                logging.info("检查成功，修改房间名称正常")
            except:
                logging.exception("检查失败！修改房间名称错误！")
                raise

    # 房主设置麦位锁定/取消
    @pytest.mark.all
    def test_api_048_a(self):
        titel = "房主设置麦位锁定"
        data = ChatRoomApi.api_data_048_a
        logging.info("获取到当前聊天室中麦位信息如下：")
        logging.info(chat_item_list)
        chatroom_mike_id = chat_item_list[0]['id']
        data['parame']['chatroom_mike_id'] = chatroom_mike_id
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            time.sleep(3)
            titel = "房主设置麦位锁定取消"
            data = ChatRoomApi.api_data_048_b
            data['parame']['chatroom_mike_id'] = chatroom_mike_id
            response = share_request(titel, data)
            try:
                assert response['code'] == data["expect"]
                logging.info("code断言成功")
            except:
                logging.exception("code断言失败了！")
                raise

    # 房主给与申请上麦通过
    @pytest.mark.all
    def test_api_049(self):
        time.sleep(3)
        titel = "房主给与申请上麦通过"
        data = ChatRoomApi.api_data_049
        logging.info("获取到当前聊天室中麦位申请列表信息如下：")
        logging.info(  APPLY_MIKE_USER_list )
        data['parame']['chatroom_mike_apply_id'] = APPLY_MIKE_USER_list[0]['id']
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：通过申请后返回数据")
            try:
                assert len(response['ret']) > 0
                global BY_MIC_ID, MIC_USER_ID
                BY_MIC_ID = response['ret']['id']
                MIC_USER_ID = response['ret']['user_id']
                logging.info("检查成功，通过申请后有返回数据")
            except:
                logging.exception("检查失败！通过申请后有返回数据！")
                raise

    # 房主设置麦位闭麦
    @pytest.mark.all
    def test_api_049_a(self):
        time.sleep(3)
        titel = "房主设置麦位闭麦"
        logging.info("获取当前聊天室麦位信息情况。。。")
        data = ChatRoomApi.api_data_040_c
        response = share_request(titel, data)
        global chat_item_list
        chat_item_list = response['ret']['chatroom_mike_array']  # 获取聊天室的麦位信息
        for item, mic in enumerate(chat_item_list):
            if mic['is_used'] == 1:
                mic_id = mic['id']
                user_id = mic['user_id']
                break
        data = ChatRoomApi.api_data_049_a
        data['parame']['chatroom_mike_id'] = mic_id
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 房主取消麦位闭麦
    @pytest.mark.all
    def test_api_049_b(self):
        time.sleep(3)
        titel = "房主取消麦位闭麦"
        for item, mic in enumerate(chat_item_list):
            if mic['is_used'] == 1:
                mic_id = mic['id']
                user_id = mic['user_id']
                break
        data = ChatRoomApi.api_data_049_b
        data['parame']['chatroom_mike_id'] = mic_id
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 房主给与申请上麦驳回
    @pytest.mark.all
    def test_api_050(self):
        titel = "房主给与申请上麦驳回"
        data = ChatRoomApi.api_data_050
        data['parame']['chatroom_mike_apply_id'] = APPLY_MIKE_USER_list[1]['id']
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：驳回申请后返回数据")
            try:
                assert len(response['ret']) > 0
                logging.info("检查成功，驳回申请后有返回数据")
            except:
                logging.exception("检查失败！驳回申请后有返回数据！")
                raise

    # 房主将用户抱下麦
    @pytest.mark.all
    def test_api_051(self):
        time.sleep(3)
        titel = "房主将用户抱下麦"
        logging.info("获取当前聊天室麦位信息情况。。。")
        data = ChatRoomApi.api_data_040_c
        response = share_request(titel, data)
        global chat_item_list
        chat_item_list = response['ret']['chatroom_mike_array']  # 获取聊天室的麦位信息
        for item,mic in enumerate(chat_item_list):
            if mic['is_used'] == 1:
                mic_id = mic['id']
                user_id = mic['user_id']
                break
        data = ChatRoomApi.api_data_051
        logging.info("获取到当前聊天室中麦上有用户的麦位id及user_id分别为：{}，{}".format(mic_id, user_id))
        data['parame']['user_id'] = user_id
        data['parame']['chatroom_mike_id'] = mic_id
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：通过申请后返回数据")
            try:
                assert len(response['ret']) > 0
                logging.info("检查成功，通过申请后有返回数据")
            except:
                logging.exception("检查失败！通过申请后有返回数据！")
                raise

    # 房主对用户设置禁言
    @pytest.mark.all
    def test_api_052(self):
        titel = "房主对用户设置禁言"
        data = ChatRoomApi.api_data_052
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 房主对用户取消禁言
    @pytest.mark.all
    def test_api_053(self):
        titel = "房主对用户取消禁言"
        data = ChatRoomApi.api_data_053
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 房主设置聊天室禁言
    @pytest.mark.demo
    def test_api_053_a(self):
        titel = "房主设置聊天室禁言"
        data = ChatRoomApi.api_data_053_a
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 房主取消聊天室禁言
    @pytest.mark.demo
    def test_api_053_b(self):
        titel = "房主取消聊天室禁言"
        data = ChatRoomApi.api_data_053_b
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # ========================    主持相关    =================================

    # 主持清空聊天室麦位宠爱值
    @pytest.mark.demo
    def test_api_054(self):
        titel = "设置用户A为主持"
        data = ChatRoomApi.api_data_045_b
        data['parame']['user_id'] = user_A_udid
        response = share_request(titel, data)       # 设置用户A为主持

        titel = "用户A登录"
        data = ChatRoomApi.api_data_040_a
        response = share_request(titel, data)
        global TOKEN, KEYS
        TOKEN = response["ret"]["token"]  # 获取登录的token
        KEYS = response["ret"]["key"]

        titel = "主持清空聊天室麦位宠爱值"
        data = ChatRoomApi.api_data_054
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 主持给申请上麦用户审核通过
    @pytest.mark.demo
    def test_api_055(self):
        titel = "获取聊天室当前麦位申请列表"
        data = ChatRoomApi.api_data_044
        response = share_request(titel, data)
        global APPLY_MIKE_USER_list
        APPLY_MIKE_USER_list = response['ret']['data']
        logging.info("检查成功，当前房间申请上麦人数为 {}。".format(len(APPLY_MIKE_USER_list)))

        titel = "主持给与申请上麦通过"
        data = ChatRoomApi.api_data_055
        logging.info("获取到当前聊天室中麦位申请列表信息如下：")
        logging.info(  APPLY_MIKE_USER_list )
        data['parame']['chatroom_mike_apply_id'] = APPLY_MIKE_USER_list[0]['id']
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：通过申请后返回数据")
            try:
                assert len(response['ret']) > 0
                global BY_MIC_ID, MIC_USER_ID
                BY_MIC_ID = response['ret']['id']
                MIC_USER_ID = response['ret']['user_id']
                logging.info("检查成功，通过申请后有返回数据")
            except:
                logging.exception("检查失败！通过申请后有返回数据！")
                raise

    # 主持设置麦位锁定/取消
    @pytest.mark.demo
    def test_api_056(self):
        titel = "主持设置麦位锁定"

        logging.info("获取当前聊天室麦位信息情况。。。")
        data = ChatRoomApi.api_data_040_c
        response = share_request(titel, data)
        global chat_item_list
        chat_item_list = response['ret']['chatroom_mike_array']  # 获取聊天室的麦位信息
        for item, mic in enumerate(chat_item_list):
            if mic['is_used'] == 0:       # 获取空麦位
                mic_id = mic['id']
                user_id = mic['user_id']
                break
        data = ChatRoomApi.api_data_056
        logging.info("获取到当前聊天室中麦位信息如下：")
        logging.info(chat_item_list)
        data['parame']['chatroom_mike_id'] = mic_id
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            time.sleep(3)
            titel = "主持设置麦位锁定取消"
            data = ChatRoomApi.api_data_056_a
            data['parame']['chatroom_mike_id'] = mic_id
            response = share_request(titel, data)
            try:
                assert response['code'] == data["expect"]
                logging.info("code断言成功")
            except:
                logging.exception("code断言失败了！")
                raise

    # 主持设置麦位闭麦
    @pytest.mark.demo
    def test_api_057(self):
        time.sleep(3)
        titel = "主持设置麦位闭麦"
        for item, mic in enumerate(chat_item_list):
            if mic['is_used'] == 1:       # 获取麦上有用户的麦位信息
                mic_id = mic['id']
                user_id = mic['user_id']
                break
        data = ChatRoomApi.api_data_057
        data['parame']['chatroom_mike_id'] = mic_id
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 主持取消麦位闭麦
    @pytest.mark.demo
    def test_api_058(self):
        time.sleep(3)
        titel = "主持取消麦位闭麦"
        for item, mic in enumerate(chat_item_list):
            if mic['is_used'] == 1:
                mic_id = mic['id']
                user_id = mic['user_id']
                break
        data = ChatRoomApi.api_data_058
        data['parame']['chatroom_mike_id'] = mic_id
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 主持给与申请上麦驳回
    @pytest.mark.demo
    def test_api_059(self):
        titel = "主持给与申请上麦驳回"
        data = ChatRoomApi.api_data_059
        data['parame']['chatroom_mike_apply_id'] = APPLY_MIKE_USER_list[1]['id']
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：驳回申请后返回数据")
            try:
                assert len(response['ret']) > 0
                logging.info("检查成功，驳回申请后有返回数据")
            except:
                logging.exception("检查失败！驳回申请后有返回数据！")
                raise

    # 主持将用户抱下麦
    @pytest.mark.demo
    def test_api_060(self):
        time.sleep(3)
        titel = "主持将用户抱下麦"
        logging.info("获取当前聊天室麦位信息情况。。。")
        data = ChatRoomApi.api_data_040_c
        response = share_request(titel, data)
        global chat_item_list
        chat_item_list = response['ret']['chatroom_mike_array']  # 获取聊天室的麦位信息
        for item,mic in enumerate(chat_item_list):
            if mic['is_used'] == 1:
                mic_id = mic['id']
                user_id = mic['user_id']
                break
        data = ChatRoomApi.api_data_060
        logging.info("获取到当前聊天室中麦上有用户的麦位id及user_id分别为：{}，{}".format(mic_id, user_id))
        data['parame']['user_id'] = user_id
        data['parame']['chatroom_mike_id'] = mic_id
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：通过申请后返回数据")
            try:
                assert len(response['ret']) > 0
                logging.info("检查成功，通过申请后有返回数据")
            except:
                logging.exception("检查失败！通过申请后有返回数据！")
                raise

    # 主持对用户设置禁言
    @pytest.mark.demo
    def test_api_061(self):
        titel = "主持对用户设置禁言"
        data = ChatRoomApi.api_data_061
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 主持对用户取消禁言
    @pytest.mark.demo
    def test_api_062(self):
        titel = "主持对用户取消禁言"
        data = ChatRoomApi.api_data_062
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 主持设置聊天室禁言
    @pytest.mark.demo
    def test_api_063(self):
        titel = "主持设置聊天室禁言"
        data = ChatRoomApi.api_data_063
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 主持取消聊天室禁言
    @pytest.mark.demo
    def test_api_064(self):
        titel = "主持取消聊天室禁言"
        data = ChatRoomApi.api_data_064
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise















# 礼物
@pytest.mark.gift
class TestGift:

    # 获取礼物列表
    @pytest.mark.all
    @pytest.mark.parametrize("data", GiftApi.api_data_050)
    def test_api_050(self, data):
        titel = "获取礼物列表-{}".format(data["api_title"])
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查礼物信息")
            gift_number = len(response["ret"]["data"])
            if gift_number >0 :
                one_gift_name = response["ret"]["data"][0]["name"]
                logging.info("礼物列表有 {} 个礼物，其中一个礼物名称为 '{}'".format(gift_number,one_gift_name))
            else:
                logging.info("当前礼物列表没有礼物！")

    # 根据条件获取礼盒列表
    @pytest.mark.all
    def test_api_050_a(self):
        titel = "根据条件获取礼盒列表"
        data = GiftApi.api_data_050_a
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查礼盒信息")
            gift_number = len(response["ret"]["data"])
            if gift_number > 0:
                one_gift_name = response["ret"]["data"][0]["name"]
                logging.info("礼盒列表有 {} 个礼物，其中一个礼盒名称为 '{}'".format(gift_number, one_gift_name))
            else:
                logging.info("当前礼盒列表没有礼物！")

    # ==================   赠送动态礼物 =======================

    # 获取动态帖子id
    @pytest.mark.all
    def test_api_051(self):
        titel = "获取动态帖子id"
        data = GiftApi.api_data_051
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：需要返回动态内容")
            try:
                assert len(response['ret']) > 0
                global STATE_ID, STATE_USER_ID
                state_list = response['ret']          # 动态列表
                state = state_list[random.randint(0, 5)]     # 获取前5个动态中的一个
                STATE_ID = state["id"]
                STATE_USER_ID = state["uid"]
                logging.info("返回动态list中有 {} 个数据".format(len(state_list)))
                logging.info("其中（前5）一个动态title为 ‘{}’".format(state["title"]))
            except:
                logging.exception("检查失败！返回的动态列表没数据或异常")
                raise

    # 赠送动态礼物(礼物数量正确流)
    @pytest.mark.all
    @pytest.mark.parametrize("data", GiftApi.api_data_052)
    def test_api_052(self,data):
        titel = "（正确流）给动态送礼-{}".format(data["api_title"])
        data["parame"]["to_user_id"] = int(STATE_USER_ID)
        data["parame"]["user_status_id"] = int(STATE_ID)
        data["parame"]["gift_id"] = int(get_gift_c())
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：送礼返回的数据")
            gift_data = response['ret']['gift']
            try:
                assert gift_data is not None
                logging.info("检查成功。动态送礼有返回值，赠送的礼物名字为：‘{}’".format(gift_data['name']))
            except:
                logging.exception("检查失败！动态送礼！返回值中没有数据")
                raise

    # 赠送动态礼物(礼物数量错误流)
    @pytest.mark.all
    @pytest.mark.parametrize("data", GiftApi.api_data_053)
    def test_api_053(self, data):
        titel = "（错误流）给动态送礼-{}".format(data["api_title"])
        data["parame"]["to_user_id"] = int(STATE_USER_ID)
        data["parame"]["user_status_id"] = int(STATE_ID)
        data["parame"]["gift_id"] = int(get_gift_c())
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 赠送动态礼物(有效的钻石礼物)
    @pytest.mark.all
    def test_api_054(self):
        titel = "赠送动态礼物(有效的钻石礼物)"
        data = GiftApi.api_data_054
        data["parame"]["to_user_id"] = int(STATE_USER_ID)
        data["parame"]["user_status_id"] = int(STATE_ID)
        data["parame"]["gift_id"] = int(get_gift_a())          # 有效的钻石礼物
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 赠送动态礼物(不存在的礼物)
    @pytest.mark.all
    def test_api_055(self):
        titel = "赠送动态礼物(不存在的礼物)"
        data = GiftApi.api_data_055
        data["parame"]["to_user_id"] = int(STATE_USER_ID)
        data["parame"]["user_status_id"] = int(STATE_ID)
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # ==================   赠送个人礼物  =======================

    # 赠送个人礼物(礼物数量正确流)
    @pytest.mark.all
    @pytest.mark.parametrize("data", GiftApi.api_data_056)
    def test_api_056(self, data):
        titel = "（正确流）个人礼物-{}".format(data["api_title"])
        data["parame"]["to_user_id"] = int(STATE_USER_ID)
        data["parame"]["gift_id"] = int(get_gift_c())
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：送礼返回的数据")
            gift_data = response['ret']['user_wallet']
            try:
                assert gift_data is not None
                logging.info("检查成功。被赠送的用户id为：‘{}’".format(gift_data['id']))
            except:
                logging.exception("检查失败！动态送礼！返回值中没有数据")
                raise

    # 赠送个人礼物(礼物数量错误流)
    @pytest.mark.all
    @pytest.mark.parametrize("data", GiftApi.api_data_057)
    def test_api_057(self, data):
        titel = "（错误流）赠送个人礼物-{}".format(data["api_title"])
        data["parame"]["to_user_id"] = int(STATE_USER_ID)
        data["parame"]["gift_id"] = int(get_gift_c())
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 赠送个人礼物(有效的钻石礼物)
    @pytest.mark.all
    def test_api_058(self):
        titel = "赠送个人礼物(有效的钻石礼物)"
        data = GiftApi.api_data_058
        data["parame"]["to_user_id"] = int(STATE_USER_ID)
        data["parame"]["gift_id"] = int(get_gift_a())          # 有效的钻石礼物
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 赠送个人礼物(不存在的礼物)
    @pytest.mark.all
    def test_api_059(self):
        titel = "赠送个人礼物(不存在的礼物)"
        data = GiftApi.api_data_059
        data["parame"]["to_user_id"] = int(STATE_USER_ID)
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 获取个人礼物墙
    @pytest.mark.all
    def test_api_060(self):
        titel = "获取个人礼物墙"
        data = GiftApi.api_data_060
        data["parame"]["user_id"] = int(STATE_USER_ID)
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：返回数据")
            gift_data = response['ret']
            try:
                assert gift_data is not None
                diamond_gift_bumber = len(gift_data['diamond_gift'])
                gb_gift_bumber = len(gift_data['gb_gift'])
                logging.info("检查成功。用户’{0}‘的钻石礼物有 {1} 种，呱币礼物有 {2} 种".format(STATE_USER_ID, diamond_gift_bumber, gb_gift_bumber))
            except:
                logging.exception("检查失败！动态送礼！返回值中没有数据")
                raise

    # ==================   聊天室送礼物  =======================

    # 聊天室送钻石礼物(正确流)
    @pytest.mark.all
    @pytest.mark.parametrize("data_api", GiftApi.api_data_061_c)
    def test_api_061(self, data_api):
        titel = "聊天室送钻石礼物(正确流)"
        logging.info("前置条件：获取并进入已经开播的聊天室")
        logging.info("接下来是获取开放的聊天室id。。。")
        data = GiftApi.api_data_061_a
        response = share_request(titel, data)
        chatroom_list = response['ret']['data']
        number = len(chatroom_list)
        logging.info("当前聊天室个数为 {} ".format(number))
        global ID
        if number <= 5:
            ID = chatroom_list[random.randint(0, number - 1)]['id']
        else:
            ID = chatroom_list[random.randint(0, 4)]['id']  # 从前5个聊天室中选一个
        logging.info("接下来是进入聊天室。。。")
        data = GiftApi.api_data_061_b
        data["parame"]["chatroom_id"] = ID
        logging.info("此时获取到的全局变量聊天室的ID为：{}".format(ID))
        response = share_request(titel, data)
        logging.info("--------------- 分割线----------------------")
        logging.info("接下来是执行不同的测试场景。。")
        titel = "（正确流）聊天室送钻石礼物-{}".format(data_api["api_title"])
        data_api["parame"]["chatroom_id"] = ID
        data_api["parame"]["gift_id"] = get_gift_a()    # 动态获取礼物id（每次随机获取）
        # 先循环遍历聊天室麦位上有没有人，有则传对应的user_id和麦位，没有则传主播的
        wheat_list = response['ret']['chatroom_mike_array']       # 存储所有麦位占坑情况（不包含主播）
        user_id = ''
        pos = ''
        for index,j in enumerate(wheat_list) :
            if j['user_id'] is not None:
                user_id = j['user_id']     # 麦上的用户id
                pos = j['pos']             # 麦位
                logging.info("当前聊天室 {0} 麦位上有用户，user_id为 {1}".format(pos, user_id))
                break
        if user_id == '':
            user_id = response['ret']['chatroom']['user_id']      # 主播id
            pos = 0
            logging.info("当前聊天室没有用户上麦，主播user_id为 {}".format(user_id))
        data_api["parame"]["to_chatroom_user_id_with_mike_pos_arr"] = json.dumps([{"user_id": user_id, "mike_pos": pos}])
        response = share_request(titel, data_api)
        try:
            assert response['code'] == data_api["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：送礼后有返回数据")
            try:
                assert response['ret']['user_wallet'] is not None
                logging.info("检查成功。有返回数据")
            except:
                logging.exception("检查失败！送礼后没有返回数据")
                raise

    # 聊天室送钻石礼物(错误流)
    @pytest.mark.all
    @pytest.mark.parametrize("data_api", GiftApi.api_data_062)
    def test_api_062(self, data_api):
        titel = "聊天室送钻石礼物(错误流)"
        logging.info("前置条件：获取并进入已经开播的聊天室")
        logging.info("接下来是获取开放的聊天室id。。。")
        data = GiftApi.api_data_061_a
        response = share_request(titel, data)
        chatroom_list = response['ret']['data']
        number = len(chatroom_list)
        logging.info("当前聊天室个数为 {} ".format(number))
        global ID
        if number <= 5:
            ID = chatroom_list[random.randint(0, number - 1)]['id']
        else:
            ID = chatroom_list[random.randint(0, 4)]['id']  # 从前5个聊天室中选一个
        logging.info("接下来是进入聊天室。。。")
        data = GiftApi.api_data_061_b
        data["parame"]["chatroom_id"] = ID
        logging.info("此时获取到的全局变量聊天室的ID为：{}".format(ID))
        response = share_request(titel, data)
        logging.info("--------------- 分割线----------------------")
        logging.info("接下来是执行不同的测试场景。。")
        titel = "（正确流）聊天室送钻石礼物-{}".format(data_api["api_title"])
        data_api["parame"]["chatroom_id"] = ID
        data_api["parame"]["gift_id"] = get_gift_a()    # 动态获取礼物id（每次随机获取）
        # 先循环遍历聊天室麦位上有没有人，有则传对应的user_id和麦位，没有则传主播的
        wheat_list = response['ret']['chatroom_mike_array']       # 存储所有麦位占坑情况（不包含主播）
        user_id = ''
        pos = ''
        for index,j in enumerate(wheat_list) :
            if j['user_id'] is not None:
                user_id = j['user_id']     # 麦上的用户id
                pos = j['pos']             # 麦位
                logging.info("当前聊天室 {0} 麦位上有用户，user_id为 {1}".format(pos, user_id))
                break
        if user_id == '':
            user_id = response['ret']['chatroom']['user_id']      # 主播id
            pos = 0
            logging.info("当前聊天室没有用户上麦，主播user_id为 {}".format(user_id))
        data_api["parame"]["to_chatroom_user_id_with_mike_pos_arr"] = json.dumps([{"user_id": user_id, "mike_pos": pos}])
        response = share_request(titel, data_api)
        try:
            assert response['code'] == data_api["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 聊天室送呱币礼物
    @pytest.mark.all
    @pytest.mark.parametrize("data_api", GiftApi.api_data_063)
    def test_api_063(self, data_api):
        titel = "聊天室送呱币礼物"
        logging.info("前置条件：获取并进入已经开播的聊天室")
        logging.info("接下来是获取开放的聊天室id。。。")
        data = GiftApi.api_data_061_a
        response = share_request(titel, data)
        chatroom_list = response['ret']['data']
        number = len(chatroom_list)
        logging.info("当前聊天室个数为 {} ".format(number))
        global ID
        if number <= 5:
            ID = chatroom_list[random.randint(0, number - 1)]['id']
        else:
            ID = chatroom_list[random.randint(0, 4)]['id']  # 从前5个聊天室中选一个
        logging.info("接下来是进入聊天室。。。")
        data = GiftApi.api_data_061_b
        data["parame"]["chatroom_id"] = ID
        logging.info("此时获取到的全局变量聊天室的ID为：{}".format(ID))
        response = share_request(titel, data)
        logging.info("--------------- 分割线----------------------")
        logging.info("接下来是执行不同的测试场景。。")
        titel = "（正确流）聊天室送钻石礼物-{}".format(data_api["api_title"])
        data_api["parame"]["chatroom_id"] = ID
        data_api["parame"]["gift_id"] = get_gift_c()    # 动态获取礼物id（每次随机获取）
        # 先循环遍历聊天室麦位上有没有人，有则传对应的user_id和麦位，没有则传主播的
        wheat_list = response['ret']['chatroom_mike_array']       # 存储所有麦位占坑情况（不包含主播）
        user_id = ''
        pos = ''
        for index,j in enumerate(wheat_list) :
            if j['user_id'] is not None:
                user_id = j['user_id']     # 麦上的用户id
                pos = j['pos']             # 麦位
                logging.info("当前聊天室 {0} 麦位上有用户，user_id为 {1}".format(pos, user_id))
                break
        if user_id == '':
            user_id = response['ret']['chatroom']['user_id']      # 主播id
            pos = 0
            logging.info("当前聊天室没有用户上麦，主播user_id为 {}".format(user_id))
        data_api["parame"]["to_chatroom_user_id_with_mike_pos_arr"] = json.dumps([{"user_id": user_id, "mike_pos": pos}])
        response = share_request(titel, data_api)
        try:
            assert response['code'] == data_api["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 聊天室送礼盒（正确流）
    @pytest.mark.all
    @pytest.mark.parametrize("data_api", GiftApi.api_data_064)
    def test_api_064(self, data_api):
        titel = "聊天室送礼盒（正确流）"
        logging.info("前置条件：获取并进入已经开播的聊天室")
        logging.info("接下来是获取开放的聊天室id。。。")
        data = GiftApi.api_data_061_a
        response = share_request(titel, data)
        chatroom_list = response['ret']['data']
        number = len(chatroom_list)
        logging.info("当前聊天室个数为 {} ".format(number))
        global ID
        if number <= 5:
            ID = chatroom_list[random.randint(0, number - 1)]['id']
        else:
            ID = chatroom_list[random.randint(0, 4)]['id']  # 从前5个聊天室中选一个
        logging.info("接下来是进入聊天室。。。")
        data = GiftApi.api_data_061_b
        data["parame"]["chatroom_id"] = ID
        logging.info("此时获取到的全局变量聊天室的ID为：{}".format(ID))
        response = share_request(titel, data)
        logging.info("--------------- 分割线----------------------")
        logging.info("接下来是执行不同的测试场景。。")
        titel = "（正确流）聊天室送礼盒礼物-{}".format(data_api["api_title"])
        data_api["parame"]["chatroom_id"] = ID
        data_api["parame"]["box_id"] = get_box()    # 动态获取礼盒id（每次随机获取）
        # 先循环遍历聊天室麦位上有没有人，有则传对应的user_id和麦位，没有则传主播的
        wheat_list = response['ret']['chatroom_mike_array']       # 存储所有麦位占坑情况（不包含主播）
        user_id = ''
        pos = ''
        for index,j in enumerate(wheat_list) :
            if j['user_id'] is not None:
                user_id = j['user_id']     # 麦上的用户id
                pos = j['pos']             # 麦位
                logging.info("当前聊天室 {0} 麦位上有用户，user_id为 {1}".format(pos, user_id))
                break
        if user_id == '':
            user_id = response['ret']['chatroom']['user_id']      # 主播id
            pos = 0
            logging.info("当前聊天室没有用户上麦，主播user_id为 {}".format(user_id))
        data_api["parame"]["to_chatroom_user_id_with_mike_pos_arr"] = json.dumps([{"user_id": user_id, "mike_pos": pos}])
        response = share_request_data(titel, data_api)
        try:
            assert response['code'] == data_api["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：送礼盒有返回数据")
            try:
                assert response['ret']['user_wallet'] is not None
                logging.info("检查成功。有返回数据")
            except:
                logging.exception("检查失败！送礼后没有返回数据")
                raise

    # 聊天室送礼盒（错误流）
    @pytest.mark.all
    @pytest.mark.parametrize("data_api", GiftApi.api_data_065)
    def test_api_065(self, data_api):
        titel = "聊天室送礼盒（错误流）"
        logging.info("前置条件：获取并进入已经开播的聊天室")
        logging.info("接下来是获取开放的聊天室id。。。")
        data = GiftApi.api_data_061_a
        response = share_request(titel, data)
        chatroom_list = response['ret']['data']
        number = len(chatroom_list)
        logging.info("当前聊天室个数为 {} ".format(number))
        global ID
        if number <= 5:
            ID = chatroom_list[random.randint(0, number - 1)]['id']
        else:
            ID = chatroom_list[random.randint(0, 4)]['id']  # 从前5个聊天室中选一个
        logging.info("接下来是进入聊天室。。。")
        data = GiftApi.api_data_061_b
        data["parame"]["chatroom_id"] = ID
        logging.info("此时获取到的全局变量聊天室的ID为：{}".format(ID))
        response = share_request(titel, data)
        logging.info("--------------- 分割线----------------------")
        logging.info("接下来是执行不同的测试场景。。")
        titel = "（错误流）聊天室送礼盒礼物-{}".format(data_api["api_title"])
        data_api["parame"]["chatroom_id"] = ID
        data_api["parame"]["box_id"] = get_box()    # 动态获取礼盒id（每次随机获取）
        # 先循环遍历聊天室麦位上有没有人，有则传对应的user_id和麦位，没有则传主播的
        wheat_list = response['ret']['chatroom_mike_array']       # 存储所有麦位占坑情况（不包含主播）
        user_id = ''
        pos = ''
        for index,j in enumerate(wheat_list) :
            if j['user_id'] is not None:
                user_id = j['user_id']     # 麦上的用户id
                pos = j['pos']             # 麦位
                logging.info("当前聊天室 {0} 麦位上有用户，user_id为 {1}".format(pos, user_id))
                break
        if user_id == '':
            user_id = response['ret']['chatroom']['user_id']      # 主播id
            pos = 0
            logging.info("当前聊天室没有用户上麦，主播user_id为 {}".format(user_id))
        data_api["parame"]["to_chatroom_user_id_with_mike_pos_arr"] = json.dumps([{"user_id": user_id, "mike_pos": pos}])
        response = share_request(titel, data_api)
        try:
            assert response['code'] == data_api["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 聊天室送礼盒-聊天室不存在
    @pytest.mark.all
    def test_api_066(self):
        titel = "聊天室送礼盒-聊天室不存在"
        data = GiftApi.api_data_066
        data["parame"]["box_id"] = get_box()    # 动态获取礼盒id（每次随机获取）
        data["parame"]["to_chatroom_user_id_with_mike_pos_arr"] = json.dumps([{"user_id": 1200085, "mike_pos": 0}])
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 聊天室送礼盒-礼盒id不存在
    @pytest.mark.all
    def test_api_067(self):
        titel = "聊天室送礼盒-礼盒id不存在"
        logging.info("前置条件：获取并进入已经开播的聊天室")
        logging.info("接下来是获取开放的聊天室id。。。")
        data = GiftApi.api_data_061_a
        response = share_request(titel, data)
        chatroom_list = response['ret']['data']
        number = len(chatroom_list)
        logging.info("当前聊天室个数为 {} ".format(number))
        global ID
        if number <= 5:
            ID = chatroom_list[random.randint(0, number - 1)]['id']
        else:
            ID = chatroom_list[random.randint(0, 4)]['id']  # 从前5个聊天室中选一个
        logging.info("接下来是进入聊天室。。。")
        data = GiftApi.api_data_061_b
        data["parame"]["chatroom_id"] = ID
        logging.info("此时获取到的全局变量聊天室的ID为：{}".format(ID))
        response = share_request(titel, data)
        data = GiftApi.api_data_067
        logging.info("--------------- 分割线----------------------")
        logging.info("接下来是执行不同的测试场景。。")
        data["parame"]["chatroom_id"] = ID
        data["parame"]["box_id"] = 120000
        # 先循环遍历聊天室麦位上有没有人，有则传对应的user_id和麦位，没有则传主播的
        wheat_list = response['ret']['chatroom_mike_array']       # 存储所有麦位占坑情况（不包含主播）
        user_id = ''
        pos = ''
        for index,j in enumerate(wheat_list) :
            if j['user_id'] is not None:
                user_id = j['user_id']     # 麦上的用户id
                pos = j['pos']             # 麦位
                logging.info("当前聊天室 {0} 麦位上有用户，user_id为 {1}".format(pos, user_id))
                break
        if user_id == '':
            user_id = response['ret']['chatroom']['user_id']      # 主播id
            pos = 0
            logging.info("当前聊天室没有用户上麦，主播user_id为 {}".format(user_id))
        data["parame"]["to_chatroom_user_id_with_mike_pos_arr"] = json.dumps([{"user_id": user_id, "mike_pos": pos}])
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 获取礼物订单列表
    @pytest.mark.all
    @pytest.mark.parametrize("data", GiftApi.api_data_068)
    def test_api_068(self, data):
        titel = "获取礼物订单条件-{}".format(data["api_title"])
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查礼物订单信息")
            gift_number = len(response["ret"]["data"])
            if gift_number > 0:
                logging.info("筛选后礼物订单中有 {} 个礼物订单".format(gift_number))
            else:
                logging.info("筛选后当前列表没有礼物订单！")

# 技能相关
class TestSkillApi:

    # 获取技能列表
    @pytest.mark.all
    def test_skill_api_001(self):
        titel = "获取技能列表"
        data = SkillRelatedApi.skill_data_001
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：列表返回数据检查")
            list_number = len(response['ret'])
            try:
                assert response['ret'] is not None
                random_index = random.randint(0, list_number - 1)
                logging.info("检查成功，返回有 {} 个技能，其中一个技能为 ‘{}’".format(list_number, response['ret'][random_index]['name']))
            except:
                logging.exception("检查失败！ 返回技能数据异常")
                raise

    # 大神技能列表
    @pytest.mark.all
    def test_skill_api_002(self):
        titel = "大神技能列表"
        data = SkillRelatedApi.skill_data_002
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：列表返回数据检查")
            terminal_number = len(response['ret'])      # 分类数量
            list_number = len(response['ret']["2"]['list'])     # 手游技能数量
            try:
                assert list_number is not None
                random_index = random.randint(0, list_number - 1)
                player = response['ret']["2"]['list'][random_index]
                logging.info("检查成功，返回有 {0} 个分类，其中手游的技能有 {1} 个，其中一个大神昵称为 ‘{2}’，对应技能为 ‘{3}’".format(terminal_number, list_number, player['nick_name'],player['skill_name']))
            except:
                logging.exception("检查失败！ 返回技能数据异常")
                raise

    # 个人主页详情-技能
    @pytest.mark.all
    def test_skill_api_003(self):
        titel = "个人主页详情-技能"
        data = SkillRelatedApi.skill_data_003
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：技能列表数据")
            ret = response['ret']
            try:
                assert len(ret) >=0
                if len(ret) > 0:
                    logging.info("检查成功，有返回 {} 个技能，其中一个技能是 ‘{}’，对应的skill_id为 '{}'".format(len(ret),ret[0]['skill_name'],ret[0]['skill_id']))
                else:
                    logging.info("检查成功，该用户没有技能")
            except:
                logging.exception("检查失败，返回数据为空或异常")
                raise

# 陪玩订单相关
@pytest.mark.play
class TestOrderApi:

    @pytest.mark.all
    # 获取大神列表
    def test_order_api_001(self):
        titel = "获取大神列表"
        data = OrderApi.order_data_001
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：返回陪玩列表数据")
            order_number = len(response['ret'])
            try:
                assert order_number > 0
                nick_name = response['ret'][0]['nick_name']
                logging.info("有返回陪玩列表数据，其中给一个陪玩大神的名字为 ‘{}’".format(nick_name))
            except:
                logging.exception("返回陪玩列表数据为空或异常！")
                raise

    @pytest.mark.ytt
    @pytest.mark.all
    # 用户提交订单（正确流）
    def test_order_api_003(self):
        titel = "用户提交订单（正确流）"
        # 动态获取大神的技能id
        data = SkillRelatedApi.skill_data_003
        response = share_request_data(titel, data)
        re = response['ret'][random.randint(0,len(response['ret'])-1)]   # 随机选择一个技能
        global UUID,USID,SKILL_ID
        UUID = re['uid']
        SKILL_ID = re['skill_id']
        USID = re['usid']
        data = OrderApi.order_data_003
        data['parame']['receiver'] = UUID
        data['parame']['skill_id'] = SKILL_ID
        data['parame']['user_skill_id'] = USID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：提交成功后返回订单号及订单金额")
            Order = response['ret']
            try:
                assert Order is not None
                global ORDER_ID
                ORDER_ID = Order['order_id']
                logging.info("检查成功。返回的订单号为 {} ，需要付款金额 {} ".format(ORDER_ID, Order['paid_fee']))
            except:
                logging.exception("code断言失败了！")
                raise

    @pytest.mark.all
    # 用户提交订单（错误流）
    @pytest.mark.parametrize("data", OrderApi.order_data_002)
    def test_order_api_002(self, data):
        titel = "用户提交订单（错误流)-{}".format(data["api_title"])
        time.sleep(5)
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    @pytest.mark.all
    # 用户取消订单
    def test_order_api_004(self):
        titel = "用户取消订单"
        data = OrderApi.order_data_004
        data['parame']['order_id'] = ORDER_ID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    @pytest.mark.all
    # 用户再次提交订单
    def test_order_api_005(self):
        titel = "用户再次提交订单"
        # 动态获取大神的技能id
        data = SkillRelatedApi.skill_data_003
        response = share_request_data(titel, data)
        time.sleep(5)
        re = response['ret'][random.randint(0,len(response['ret'])-1)]   # 随机选择一个技能
        global UUID,USID,SKILL_ID
        UUID = re['uid']
        SKILL_ID = re['skill_id']
        USID = re['usid']
        data = OrderApi.order_data_003
        data['parame']['receiver'] = UUID
        data['parame']['skill_id'] = SKILL_ID
        data['parame']['user_skill_id'] = USID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：提交成功后返回订单号及订单金额")
            Order = response['ret']
            try:
                assert Order is not None
                global ORDER_ID, ORDER_AMOUNT
                ORDER_ID = Order['order_id']            # 订单id
                ORDER_AMOUNT = Order['paid_fee']        # 订单金额
                logging.info("检查成功。返回的订单号为 {} ，需要付款金额 {} ".format(ORDER_ID, ORDER_AMOUNT))
            except:
                logging.exception("code断言失败了！")
                raise

    @pytest.mark.all
    # 订单支付并检查呱币扣除数量-正确流
    def test_order_api_006(self):
        titel = "订单支付并检查呱币扣除数量-正确流"
        logging.info("获取用户支付前的呱币余额")
        data = OrderApi.order_data_010
        response = share_request_data(titel, data)
        GB_Amount = response['ret']['user_wallet_frog_coin_stored']['valid_value']    # 支付前用户的呱币余额
        data = OrderApi.order_data_006
        data['parame']['order_id'] = ORDER_ID
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("支付后，扣除金额校验")
            data = OrderApi.order_data_010
            response = share_request_data(titel, data)
            Rear_GB_Amount = response['ret']['user_wallet_frog_coin_stored']['valid_value']  # 支付后用户的呱币余额
            try:
                assert float(GB_Amount) - float(Rear_GB_Amount) == float(ORDER_AMOUNT)
                logging.info("检查成功，支付前呱币余额为 {0},订单金额为 {1},支付后呱币金额为 {2}".format(GB_Amount, ORDER_AMOUNT, Rear_GB_Amount))
            except:
                logging.info("检查失败！！支付前呱币余额为 {0},订单金额为 {1},支付后呱币金额为 {2}".format(GB_Amount, ORDER_AMOUNT, Rear_GB_Amount))
                raise

    @pytest.mark.all
    # 大神同意接单
    def test_order_api_007(self):
        titel = "大神同意接单"
        logging.info("大神登录账号。。。")
        data = OrderApi.order_data_007_a
        response = player_share_request(titel, data)      # 大神登录
        global PL_TOKEN, PL_KEYS, ID
        PL_TOKEN = response["ret"]["token"]  # 获取登录的token
        PL_KEYS = response["ret"]["key"]
        data = OrderApi.order_data_007_b
        data['parame']['order_id'] = ORDER_ID
        response = player_share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    @pytest.mark.all
    # 大神点击立即服务
    def test_order_api_008(self):
        titel = "大神点击立即服务"
        data = OrderApi.order_data_008
        data['parame']['order_id'] = ORDER_ID
        logging.info("获取到的订单号为： {}".format(ORDER_ID))
        response = player_share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    @pytest.mark.all
    # 用户同意立即服务
    def test_order_api_009(self):
        titel = "用户同意立即服务"
        data = OrderApi.order_data_009
        data['parame']['order_id'] = ORDER_ID
        logging.info("获取到的订单号为： {}".format(ORDER_ID))
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise

    # 大神查询钱包首页-获取呱币收入
    @pytest.mark.all
    def test_order_api_010(self):
        titel = "大神查询钱包首页-获取呱币收入"
        data = OrderApi.order_data_010
        response = player_share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：余额数据返回")

            try:
                assert response['ret'] is not None
                global PL_GB_Amount
                PL_GB_Amount = response['ret']["user_wallet_frog_coin_income"]["valid_value"]
                logging.info("检查成功。余额有返回数据，当前大神的呱币收入余额为：{}".format(PL_GB_Amount))
            except:
                logging.exception("检查失败！数据返回异常")
                raise

    # 用户确认完成并检查佣金到账
    @pytest.mark.all
    def test_order_api_011(self):
        titel = "用户确认完成并检查佣金到账"
        data = OrderApi.order_data_011
        data['parame']['order_id'] = ORDER_ID
        logging.info("获取到的订单号为： {}".format(ORDER_ID))
        time.sleep(5)
        response = share_request_data(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：大神的呱币收入到账是否准确")
            logging.info("订单确认前，大神的呱币收入为：{}".format(PL_GB_Amount))
            logging.info("当前订单金额为：{}".format(ORDER_AMOUNT))
            data = OrderApi.order_data_010
            response = player_share_request_data(titel, data)
            Rear_PL_GB_Amount = response['ret']["user_wallet_frog_coin_income"]["valid_value"]  # 订单确认后大神的呱币收入
            try:
                assert ORDER_AMOUNT * 0.9 + float(PL_GB_Amount) == float(Rear_PL_GB_Amount)
                logging.info("检查成功。大神收入到账准确，明细：下单前呱币收入为 {}，订单金额为 {}，订单确认后呱币收入为 {}".format(PL_GB_Amount,ORDER_AMOUNT,Rear_PL_GB_Amount))
            except:
                logging.exception("检查失败，大神到账呱币不准确或异常！")
                raise

    # 用户提交订单并支付，大神拒单
    @pytest.mark.all
    def test_order_api_012(self):
        # 用户提交订单并支付，大神拒单
        titel = '下单前查询用户呱币余额'
        logging.info("用户下单前查询呱币余额。。。")
        data = OrderApi.order_data_010
        response = share_request_data(titel, data)
        GB_Amount = response['ret']['user_wallet_frog_coin_stored']['valid_value']  # 支付前用户的呱币余额

        titel = '用户下单'
        data = SkillRelatedApi.skill_data_003
        response = share_request_data(titel, data)
        re = response['ret'][random.randint(0, len(response['ret']) - 1)]  # 随机选择一个技能
        global UUID, USID, SKILL_ID
        UUID = re['uid']
        SKILL_ID = re['skill_id']
        USID = re['usid']
        data = OrderApi.order_data_003
        data['parame']['receiver'] = UUID
        data['parame']['skill_id'] = SKILL_ID
        data['parame']['user_skill_id'] = USID
        response = share_request_data(titel, data)
        global ORDER_ID, ORDER_AMOUNT
        ORDER_ID = response['ret']['order_id']            # 订单id
        ORDER_AMOUNT = response['ret']['paid_fee']        # 订单金额

        titel = '用户支付订单'
        data = OrderApi.order_data_006
        data['parame']['order_id'] = ORDER_ID
        response = share_request_data(titel, data)

        titel = '大神拒单'
        logging.info("大神登录账号。。。")
        data = OrderApi.order_data_007_a
        response = player_share_request(titel, data)      # 大神登录
        global PL_TOKEN, PL_KEYS, ID
        PL_TOKEN = response["ret"]["token"]  # 获取登录的token
        PL_KEYS = response["ret"]["key"]
        data = OrderApi.order_data_012      # 拒单接口数据
        data['parame']['order_id'] = ORDER_ID
        response = player_share_request_data(titel, data)
        try:
            assert response["code"] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查②：订单金额原路返回至用户账号中")
            data = OrderApi.order_data_010
            response = share_request_data(titel, data)
            GB_Refund_Amount = response['ret']['user_wallet_frog_coin_stored']['valid_value']  # 退款后用户的呱币余额
            try:
                assert GB_Refund_Amount == GB_Amount      # 退款后余额 = 支付前余额
                logging.info("检查成功，退款金额准确")
            except:
                logging.exception("检查失败！支付前用户的呱币余额为 {},退款后余额为 {}".format(GB_Amount, GB_Refund_Amount))
                raise

    # 用户提交订单并支付-大神接单-大神发起立即服务-用户拒绝（申请退款）-大神同意退款
    @pytest.mark.all
    def test_order_api_013(self):
        titel = '下单前查询用户呱币余额'
        logging.info("用户下单前查询呱币余额。。。")
        data = OrderApi.order_data_010
        response = share_request_data(titel, data)
        GB_Amount = response['ret']['user_wallet_frog_coin_stored']['valid_value']  # 支付前用户的呱币余额

        titel = '用户下单'
        data = SkillRelatedApi.skill_data_003
        response = share_request_data(titel, data)
        re = response['ret'][random.randint(0, len(response['ret']) - 1)]  # 随机选择一个技能
        global UUID, USID, SKILL_ID
        UUID = re['uid']
        SKILL_ID = re['skill_id']
        USID = re['usid']
        data = OrderApi.order_data_003
        data['parame']['receiver'] = UUID
        data['parame']['skill_id'] = SKILL_ID
        data['parame']['user_skill_id'] = USID
        response = share_request_data(titel, data)
        global ORDER_ID, ORDER_AMOUNT
        ORDER_ID = response['ret']['order_id']            # 订单id
        ORDER_AMOUNT = response['ret']['paid_fee']        # 订单金额

        titel = '用户支付订单'
        data = OrderApi.order_data_006
        data['parame']['order_id'] = ORDER_ID
        response = share_request_data(titel, data)

        titel = "大神同意接单"
        logging.info("大神登录账号。。。")
        data = OrderApi.order_data_007_a
        response = player_share_request(titel, data)  # 大神登录
        global PL_TOKEN, PL_KEYS, ID
        PL_TOKEN = response["ret"]["token"]  # 获取登录的token
        PL_KEYS = response["ret"]["key"]
        data = OrderApi.order_data_007_b
        data['parame']['order_id'] = ORDER_ID
        response = player_share_request_data(titel, data)

        titel = "大神发起立即服务"
        data = OrderApi.order_data_008
        data['parame']['order_id'] = ORDER_ID
        logging.info("获取到的订单号为： {}".format(ORDER_ID))
        response = player_share_request_data(titel, data)

        titel = "用户拒绝立即服务（申请退款）"
        data = OrderApi.order_data_013_a
        data['parame']['order_id'] = ORDER_ID
        response = share_request_data(titel, data)
        try:
            assert response["code"] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            titel = '用户申请退款'
            data = OrderApi.order_data_013_b
            data['parame']['game_order_id'] = ORDER_ID
            response = share_request_data(titel, data)
            try:
                assert response["code"] == data["expect"]
                rf_id = response["ret"]["id"]           # 获取申诉id
                logging.info("检查成功，用户申请退款正常，申诉ID为 {}".format(rf_id))
            except:
                logging.exception("检查失败，用户申请退款有异常！")
                raise
            else:
                titel = "大神同意退款"
                data = OrderApi.order_data_013_c
                data['parame']['order_id'] = ORDER_ID
                data['parame']['rfid'] = rf_id
                logging.info("获取到的订单号为： {}".format(ORDER_ID))
                response = player_share_request_data(titel, data)
                try:
                    assert response["code"] == data["expect"]
                    logging.info("检查成功，退款正常")
                except:
                    logging.exception("检查失败，退款失败")
                    raise
                else:
                    data = OrderApi.order_data_010
                    response = share_request_data(titel, data)
                    GB_Refund_Amount = response['ret']['user_wallet_frog_coin_stored']['valid_value']  # 退款后用户的呱币余额
                    logging.info("检查退款呱币是否准确退回")
                    try:
                        assert GB_Refund_Amount == GB_Amount  # 退款余额 = 支付前余额
                        logging.info("检查成功，退款金额准确")
                    except:
                        logging.exception("检查失败！支付前用户的呱币余额为 {},退款后余额为 {}".format(GB_Amount, GB_Refund_Amount))
                        raise


# 其他
class TestOtherApi:

    # 根据条件获取图文规则列表
    @pytest.mark.all
    def test_other_api_01(self):
        titel = "根据条件获取图文规则列表"
        data = OtherApi.other_data_001
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise
        else:
            logging.info("检查内容展示")
            try:
                assert str(response['ret']["data"]).find(data["title"]) > 0   # 文本中有’隐私政策‘字样
                logging.info("检查内容展示成功")
            except:
                logging.exception("检查内容展示有异常。")
                raise

    # 根据条件获取广告列表
    @pytest.mark.all
    def test_other_api_02(self):
        titel = "根据条件获取广告列表"
        data = OtherApi.other_data_002
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功")
        except:
            logging.exception("code断言失败了！")
            raise




