"""  用来存储api测试数据  """

from Common.BaseDef import BaseDef
# 注册/登录手机号
iphone = '13297025059'
pwd = 'aaa111'
new_pwd = 'bbb000'
update_pwd = '111aaa'

api_url = "https://ggapi.qwdj.com/"

random_number = BaseDef().random_str_china()     # 获取一个随机数


class UserData:
    # 手机号注册_输出错误的手机号
    api_data_001 = {"url": api_url + "newapi/api/user/register",
                    "parame": {"account_type": "1",
                               "phonenum": "1320000",
                               "password": pwd,
                               "verify_code": '1111',
                               },
                    "Method": "post",
                    "expect": 2001003
                    }

    # 手机号注册-输入正确的手机号
    api_data_002 = {"url":api_url+"newapi/api/user/register",
                    "parame": {"account_type": "1",
                                  "phonenum": iphone,
                                  "password": pwd,
                                  "verify_code": '1111',
                                },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 注册成功后验证用户是否存在
    api_data_003 = {"url": api_url + "newapi/api/user/isExist",
                    "parame": {
                               "phonenum": iphone
                               },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 手机号登录-手机号未注册
    api_data_004 = {"url":api_url+"newapi/api/user/login",
                    "parame": {"account_type": "1",
                                  "phonenum": "13298000000",
                                  "password": pwd,
                                },
                    "Method": "post",
                    "expect": 2003018
                    }

    # 手机号登录-输入错误的密码
    api_data_005 = {"url":api_url+"newapi/api/user/login",
                    "parame": {"account_type": "1",
                                  "phonenum": iphone,
                                  "password": "111111",
                                },
                    "Method": "post",
                    "expect": 2003021,
                    "message": "用户密码错误"
                   }

    # 忘记密码
    api_data_006_a = {"url": api_url + "newapi/api/user/forgetPassword",
                    "parame": {"account_type": "1",
                               "phonenum": iphone,
                               "verify_code": "0000",
                               "password": new_pwd,
                               },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 忘记密码-使用旧密码登录
    api_data_006_b = {"url": api_url + "newapi/api/user/login",
                      "parame": {"account_type": "1",
                                 "phonenum": iphone,
                                 "password": pwd,
                                 },
                      "Method": "post",
                      "expect": 2003021
                      }

    # 忘记密码-使用新密码登录
    api_data_006_c = {"url": api_url + "newapi/api/user/login",
                      "parame": {"account_type": "1",
                                 "phonenum": iphone,
                                 "password": new_pwd,
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 手机号登录-正常场景(前置：将用户密码还原)
    api_data_007_a = {"url": api_url + "newapi/api/user/forgetPassword",
                      "parame": {"account_type": "1",
                                 "phonenum": iphone,
                                 "verify_code": "0000",
                                 "password": pwd,
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 手机号登录-正常场景
    api_data_007_b = {"url": api_url + "newapi/api/user/login",
                       "parame": {"account_type": "1",
                                  "phonenum": iphone,
                                  "password": pwd,
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # (登录后)修改密码
    api_data_008_a = {"url": api_url + "newapi/api/user/changePassword",
                      "parame": {
                                  "password": update_pwd,
                                  "verify_code": "1111",
                                  },
                      "Method": "post",
                      "expect": 2000000
                     }

    # 修改密码-使用旧密码登录
    api_data_008_b = {"url": api_url + "newapi/api/user/login",
                      "parame": {"account_type": "1",
                                 "phonenum": iphone,
                                 "password": pwd,
                                 },
                      "Method": "post",
                      "expect": 2003021
                      }

    # 修改密码-使用新密码登录
    api_data_008_c = {"url": api_url + "newapi/api/user/login",
                      "parame": {"account_type": "1",
                                 "phonenum": iphone,
                                 "password": update_pwd,
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 获取个人信息
    api_data_009 = {"url": api_url + "newapi/api/user/getSelfInfo",
                    "parame": {
                               },
                      "Method": "get",
                      "expect": 2000000
                      }

    # 更新个人信息
    api_data_010 = {"url": api_url + "newapi/api/user/updateBySelf",
                    "parame": {"nick_name": "更改昵称-{}".format(random_number),
                               "weight": "62"
                               },
                    "Method": "post",
                    "expect": 2000000,
                    "expect_name": "更改昵称-{}".format(random_number)
                    }

    # 根据id获取用户信息-id存在  (id通过用例中全局变量传递)
    api_data_011 = {"url": api_url + "newapi/api/user/getById",
                    "parame": {"id": ""
                               },
                    "Method": "get",
                    "expect": 2000000,
                    }

    # 根据id获取用户信息-id不存在
    api_data_012 = {"url": api_url + "newapi/api/user/getById",
                    "parame": {"id": "800000"
                               },
                    "Method": "get",
                    "expect": 2000000,
                    }

    # 获取用户列表
    api_data_013 = {"url": api_url + "newapi/api/user/getListByCon",
                    "parame": {
                               },
                    "Method": "get",
                    "expect": 2000000,
                    "usernumber": "0"
                    }

    # 获取用户列表-筛选带装扮
    api_data_014 = {"url": api_url + "newapi/api/user/getListByCon",
                    "parame": {"level": "2"
                               },
                    "Method": "get",
                    "expect": 2000000,
                    "usernumber": "0"
                    }

    # 获取用户列表-通过uuid筛选（通过全局变量中的ID传参）
    api_data_015 = {"url": api_url + "newapi/api/user/getListByCon",
                    "parame": {"search_word": ""
                               },
                    "Method": "get",
                    "expect": 2000000,
                    "usernumber": "1"
                    }

    # 获取用户列表-通过昵称模糊筛选（通过全局变量中的NICK_NAME传参）
    api_data_016 = {"url": api_url + "newapi/api/user/getListByCon",
                    "parame": {"search_word": ""
                               },
                    "Method": "get",
                    "expect": 2000000,
                    "usernumber": "1"
                    }

    # 获取用户列表-通过昵称完全匹配（通过全局变量中的NICK_NAME传参）
    api_data_017 = {"url": api_url + "newapi/api/user/getListByCon",
                    "parame": {"accurate_search_word": ""
                               },
                    "Method": "get",
                    "expect": 2000000,
                    "usernumber": "1"
                    }

    # 获取实人认证审核状态(返回值audit_status的状态)
    api_data_018 = {"url": api_url + "newapi/api/userAliRpRecord/getAuditStatus",
                      "parame": {
                               },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 发起阿里云实人认证请求
    api_data_019 = {"url": api_url + "newapi/api/userAliRpRecord/describeVerifyToken",
                      "parame": {
                               },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 获取兴趣列表
    api_data_020 = {"url": api_url + "newapi/api/interest/getListByCon",
                      "parame": {
                               },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 根据条件（页码）赛选获取兴趣列表
    api_data_021 = {"url": api_url + "newapi/api/interest/getListByCon",
                      "parame": {"page":"2"
                               },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 获取用户是否绑定微信的状态
    api_data_022_a = {"url": api_url + "newapi/api/user/isExistBindThirdLogin",
                      "parame": {"phonenum": iphone,
                                 "account_type": "5"
                               },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 绑定微信
    api_data_022_b = {"url": api_url + "newapi/api/user/setBindThirdLogin",
                      "parame": {"account_type": "5",
                                 "open_id": "52111111"
                               },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 解绑微信
    api_data_022_c = {"url": api_url + "newapi/api/user/cancelBindThirdLogin",
                      "parame": {"account_type": "5",
                               },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 获取用户是否绑定QQ的状态
    api_data_023_a = {"url": api_url + "newapi/api/user/isExistBindThirdLogin",
                      "parame": {"phonenum": iphone,
                                 "account_type": "6"
                               },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 绑定QQ
    api_data_023_b = {"url": api_url + "newapi/api/user/setBindThirdLogin",
                      "parame": {"account_type": "6",
                                 "open_id": "3000001"
                               },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 解绑QQ
    api_data_023_c = {"url": api_url + "newapi/api/user/cancelBindThirdLogin",
                      "parame": {"account_type": "6",
                               },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 获取用户是否绑定appleId的状态
    api_data_024_a = {"url": api_url + "newapi/api/user/isExistBindThirdLogin",
                      "parame": {"phonenum": iphone,
                                 "account_type": "7"
                               },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 绑定appleId
    api_data_024_b = {"url": api_url + "newapi/api/user/setBindThirdLogin",
                      "parame": {"account_type": "7",
                                 "open_id": "1324521521@qq.com"
                               },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 解绑appleId
    api_data_024_c = {"url": api_url + "newapi/api/user/cancelBindThirdLogin",
                      "parame": {"account_type": "7",
                               },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 绑定QQ
    api_data_025_a = {"url": api_url + "newapi/api/user/setBindThirdLogin",
                      "parame": {"account_type": "6",
                                 "open_id": "45121546"
                                 },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 重复QQ
    api_data_025_b = {"url": api_url + "newapi/api/user/setBindThirdLogin",
                      "parame": {"account_type": "6",
                                 "open_id": "324581524"
                                 },
                      "Method": "post",
                      "expect": 2003024,
                      }

    # 解绑微信
    api_data_026 = {"url": api_url + "newapi/api/user/cancelBindThirdLogin",
                      "parame": {"account_type": "5",
                               },
                      "Method": "post",
                      "expect": 2003012,
                      }


class LiveRoomApi:

    # 首页直播间推荐列表
    api_data_027 = {"url": api_url + "oldapi/api/chatroom/recom_list/list",
                    "parame": {
                               },
                    "Method": "post",
                    "expect": 2000000,
                    }

    # 首页-动态推荐位(默认)
    api_data_028 = {"url": api_url + "oldapi/api/chatroom/recom_list/index_recom",
                    "parame": {
                               },
                    "Method": "post",
                    "expect": 2000000,
                    }

    # 首页-动态推荐位(选择展示)
    api_data_029 = {"url": api_url + "oldapi/api/chatroom/recom_list/index_recom",
                    "parame": {"page": "2",
                               "perpage": "5"
                               },
                    "Method": "post",
                    "expect": 2000000,
                    }

    # 首页-娱乐交友，游戏组队直播间
    api_data_030 = {"url": api_url + "oldapi/api/chatroom/recom_list/room_enter",
                    "parame": {
                               },
                    "Method": "post",
                    "expect": 2000000,
                    }

    # 检查派单大厅列表展示及个数
    api_data_031 = {"url": api_url + "oldapi/api/chatroom/send_order_hall/list",
                    "parame": {
                               },
                    "Method": "post",
                    "expect": 2000000,
                    }