"""  接口测试用例  """

import pytest
from Common import logger
import logging
import json
from Common.api_request import ApiRequest
from TestData.api_data import UserData,LiveRoomApi
from TestData import api_data
from Common import path_config

TOKEN = ''      # 用来存储token
KEYS = ''       # 用来存储key
ID = ''         # 用来存储用户id
NICK_NAME = '更改昵称'  # 用来存储用户的昵称

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

class TestUserRelated:

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
        data = UserData.api_data_025_a     # 第一次绑定
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
        data = UserData.api_data_026     # 第一次绑定
        data = UserData.api_data_026     # 重复绑定
        response = share_request(titel, data)
        try:
            assert response['code'] == data["expect"]
            logging.info("code断言成功.")
        except:
            logging.exception("code断言失败了！")
            raise


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
    @pytest.mark.demo
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













