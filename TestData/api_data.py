"""  用来存储api测试数据  """

from Common.BaseDef import BaseDef
# 注册/登录手机号
iphone = '13297025029'
pwd = 'aaa111'
new_pwd = 'bbb000'
update_pwd = '111aaa'
code_iphone = '13297025057'     # 可接受验证码的手机号
player_iphone = '13299999999'   # 玩家大神手机号

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

    # 发送验证码（登录时）
    api_send_code_01 = {"url": api_url + "newapi/api/common/sendVerifyCode",
                        "parame": {"target": code_iphone,
                                   "target_type": '1',
                                   "type": '1',
                               },
                        "Method": "post",
                        "expect": 2000000
                        }

    # 发送验证码（忘记密码）
    api_send_code_02 = {"url": api_url + "newapi/api/common/sendVerifyCode",
                        "parame": {"target": code_iphone,
                                   "target_type": '1',
                                   "type": '2',
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
                    "parame": {"nick_name": "api自动化测试-{}".format(random_number),
                               "weight": "62"
                               },
                    "Method": "post",
                    "expect": 2000000,
                    "expect_name": "api自动化测试-{}".format(random_number)
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

class ChatRoomApi:
    # 根据条件获取聊天室信息
    api_data_032 = [{"url": api_url + "newapi/api/chatroom/getListByCon",
                    "chat_title": "页码为2时",
                     "parame": {"page":"2"
                     },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/chatroom/getListByCon",
                     "chat_title": "uuid/聊天室名，模糊搜索-83373403",
                     "parame": {"search_word": "83373403"
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/chatroom/getListByCon",
                     "chat_title": "聊天室类型-情感",
                     "parame": {"type": "31"
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/chatroom/getListByCon",
                     "chat_title": "聊天室类型-普通派单",
                     "parame": {"type": "41"
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/chatroom/getListByCon",
                     "chat_title": "派单类型聊天室",
                     "parame": {"type_classify": "3"
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/chatroom/getListByCon",
                     "chat_title": "交友聊天室开放并展示",
                     "parame": {"is_open": "1",
                                "is_show": "1",
                                "type_classify": "3",
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    ]

    # 默认展示聊天室信息
    api_data_033 = {"url": api_url + "newapi/api/chatroom/getListByCon",
                    "parame": {
                               },
                    "Method": "get",
                    "expect": 2000000,
                    }
    # 根据id获取聊天室信息(id通过全局变量传递)
    api_data_034 = {"url": api_url + "newapi/api/chatroom/getById",
                    "parame": {"id": ''
                               },
                    "Method": "get",
                    "expect": 2000000,
                    }

    # 根据id获取聊天室信息(id不存在)
    api_data_034_a = {"url": api_url + "newapi/api/chatroom/getById",
                    "parame": {"id":'110000'
                               },
                    "Method": "get",
                    "expect": 2000000,
                    }

    # 加入聊天室-房间编号不存在或错误
    api_data_035 = {"url": api_url + "newapi/api/chatroom/join",
                    "parame": {"chatroom_id":'121212'
                               },
                    "Method": "get",
                    "expect": 2005001,
                    }

    # 前置：获取已存在的聊天室id
    api_data_036_a = {"url": api_url + "newapi/api/chatroom/getListByCon",
                      "parame": {"is_open": '1'
                                 },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 加入聊天室-房间编号存在（通过全局变量UUID传参）
    api_data_036_b = {"url": api_url + "newapi/api/chatroom/join",
                    "parame": {"chatroom_id":''
                               },
                    "Method": "get",
                    "expect": 2000000,
                    }

    # 退出聊天室-已加入聊天室（通过全局变量UUID传参）
    api_data_037 = {"url": api_url + "newapi/api/chatroom/exit",
                    "parame": {"chatroom_id":''
                               },
                    "Method": "get",
                    "expect": 2000000,
                    }

    # 退出聊天室-聊天室不存在或不在房间中
    api_data_038 = {"url": api_url + "newapi/api/chatroom/exit",
                    "parame": {"chatroom_id": '1200000'
                               },
                    "Method": "get",
                    "expect": 2005001,
                    }

    # 退出聊天室-缺少聊天室id
    api_data_039 = {"url": api_url + "newapi/api/chatroom/exit",
                    "parame": {
                               },
                    "Method": "get",
                    "expect": 2001003,
                    }




class GiftApi:

    # 获取聊天室中-有效的礼物（钻石）
    api_get_gift_a = {"url": api_url + "newapi/api/gift/getListByCon",
                      "parame": {"type": "1",  # 1 钻石；2 呱币
                                 "is_at_validity": "1"  # 1有效，2 无效
                                 },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 获取聊天室中-过期的礼物（钻石）
    api_get_gift_b = {"url": api_url + "newapi/api/gift/getListByCon",
                      "parame": {"type": "1",  # 1 钻石；2 呱币
                                 "is_at_validity": "0"  # 1有效，0或空 无效
                                 },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 获取呱币礼物(有效)
    api_get_gift_c = {"url": api_url + "newapi/api/gift/getListByCon",
                      "parame": {"type": "2",  # 1 钻石；2 呱币
                                 "is_at_validity": "1"  # 1有效，0或空 无效
                                 },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 获取呱币礼物(无效)
    api_get_gift_d = {"url": api_url + "newapi/api/gift/getListByCon",
                      "parame": {"type": "2",  # 1 钻石；2 呱币
                                 "is_at_validity": "0"  # 1有效，0或空 无效
                                 },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 获取礼物列表
    api_data_050 = [{"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "不传参数",
                    "parame": {
                    },
                    "Method": "get",
                    "expect": 2000000,
                    },
                    {"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "不展示",
                     "parame": {"is_show": "0"
                     },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "展示",
                     "parame": {"is_show": "1"
                     },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "砖石",
                     "parame": {"type": "1"
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "呱币",
                     "parame": {"type": "2"
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "页码",
                     "parame": {"page": "2"
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "展示有效期内的礼物",
                     "parame": {"is_at_validity": "1"
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "分页",
                     "parame": {"is_paginate": True
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/getListByCon",
                     "api_title": "组合赛选",
                     "parame": {"is_show": "1",
                                "is_paginate": True,
                                "type": "2",
                                },
                     "Method": "get",
                     "expect": 2000000,
                     }
                    ]

    # 获取动态id
    api_data_051 = {"url": api_url + "oldapi/api/state/statelist/states_all",
                      "parame": {
                               },
                      "Method": "post",
                      "expect": 2000000,
                    }

    # 给动态的用户送礼物(正确流)    传参均通过全局变量动态获取
    api_data_052 = [{"url": api_url + "newapi/api/gift/sendTrendsGift",
                    "api_title": "1个有效呱币礼物",
                      "parame": {"to_user_id": "",          # 发送动态的用户id
                                 "user_status_id": "",      # 动态id
                                 "gift_id": "",             # 礼物编号id
                                 "amount": 1,              # 礼物数量
                               },
                      "Method": "post",
                      "expect": 2000000,
                    },
                    {"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "api_title": "多个有效呱币礼物",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": "",
                                "amount": 8,
                                },
                     "Method": "post",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "api_title": "20个有效呱币礼物",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": "",
                                "amount": 20,
                                },
                     "Method": "post",
                     "expect": 2000000,
                     },
                    ]

    # 给动态的用户送礼物(错误流)    传参均通过全局变量动态获取
    api_data_053 = [{"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "api_title": "0个有效呱币礼物",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": "",
                                "amount": 0,
                                },
                     "Method": "post",
                     "expect": 2006008,
                     },
                    {"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "api_title": "(-1个有效呱币礼物)",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": "",
                                "amount": -1,
                                },
                     "Method": "post",
                     "expect": 2006008,
                     },
                    {"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "api_title": "(礼物个数为空)",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": "",
                                "amount": None,
                                },
                     "Method": "post",
                     "expect": 2001003
                     },
                    {"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "api_title": "(礼物个数值为True)",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": "",
                                "amount": True,
                                },
                     "Method": "post",
                     "expect": 2001003
                     },
                    ]

    # 赠送动态礼物(有效的钻石礼物)    传参均通过全局变量动态获取
    api_data_054 = {"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": "",
                                "amount": 1,
                                },
                     "Method": "post",
                     "expect": 2006002,
                     }

    # 赠送动态礼物(不存在的礼物)    传参均通过全局变量动态获取
    api_data_055 = {"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": 9999,
                                "amount": 1,
                                },
                     "Method": "post",
                     "expect": 2006002,
                     }

    # ==================   赠送个人礼物  =======================

    # 赠送个人礼物(礼物数量正确流)    传参均通过全局变量动态获取
    api_data_056 = [{"url": api_url + "newapi/api/gift/sendPersonalGift",
                    "api_title": "1个有效呱币礼物",
                      "parame": {"to_user_id": "",          # 发送动态的用户id
                                 "gift_id": "",             # 礼物编号id
                                 "amount": 1,              # 礼物数量
                               },
                      "Method": "post",
                      "expect": 2000000,
                    },
                    {"url": api_url + "newapi/api/gift/sendPersonalGift",
                     "api_title": "多个有效呱币礼物",
                     "parame": {"to_user_id": "",
                                "gift_id": "",
                                "amount": 8,
                                },
                     "Method": "post",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/sendPersonalGift",
                     "api_title": "20个有效呱币礼物",
                     "parame": {"to_user_id": "",
                                "gift_id": "",
                                "amount": 20,
                                },
                     "Method": "post",
                     "expect": 2000000,
                     },
                    ]

    # 给个人礼物(错误流)    传参均通过全局变量动态获取
    api_data_057 = [{"url": api_url + "newapi/api/gift/sendPersonalGift",
                     "api_title": "0个有效呱币礼物",
                     "parame": {"to_user_id": "",
                                "gift_id": "",
                                "amount": 0,
                                },
                     "Method": "post",
                     "expect": 2006008,
                     },
                    {"url": api_url + "newapi/api/gift/sendPersonalGift",
                     "api_title": "(-1个有效呱币礼物)",
                     "parame": {"to_user_id": "",
                                "gift_id": "",
                                "amount": -1,
                                },
                     "Method": "post",
                     "expect": 2006008,
                     },
                    {"url": api_url + "newapi/api/gift/sendTrendsGift",
                     "api_title": "(礼物个数为空)",
                     "parame": {"to_user_id": "",
                                "gift_id": "",
                                "amount": None,
                                },
                     "Method": "post",
                     "expect": 2001003
                     },
                    {"url": api_url + "newapi/api/gift/sendPersonalGift",
                     "api_title": "(礼物个数值为True)",
                     "parame": {"to_user_id": "",
                                "gift_id": "",
                                "amount": True,
                                },
                     "Method": "post",
                     "expect": 2001003
                     },
                    ]

    # 赠送动态礼物(有效的钻石礼物)    传参均通过全局变量动态获取
    api_data_058 = {"url": api_url + "newapi/api/gift/sendPersonalGift",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": "",
                                "amount": 1,
                                },
                     "Method": "post",
                     "expect": 2006002,
                     }

    # 赠送动态礼物(不存在的礼物)    传参均通过全局变量动态获取
    api_data_059 = {"url": api_url + "newapi/api/gift/sendPersonalGift",
                     "parame": {"to_user_id": "",
                                "user_status_id": "",
                                "gift_id": 9999,
                                "amount": 1,
                                },
                     "Method": "post",
                     "expect": 2006002,
                     }

    # 获取个人礼物墙
    api_data_060 = {"url": api_url + "newapi/api/gift/giftWall",
                     "parame": {"user_id": ""
                                },
                     "Method": "get",
                     "expect": 2000000,
                     }
















# 其他相关api
class OtherApi:

    # 根据条件获取图文规则列表
    other_data_001 = {"url": api_url + "newapi/api/tw/getListByCon",
                      "parame": {
                               },
                      "Method": "get",
                      "expect": 2000000,
                      "title": "隐私政策"
                    }

    # 根据条件获取广告列表
    other_data_002 = {"url": api_url + "newapi/api/ad/getById",
                      "parame": {'id': '1200018'
                               },
                      "Method": "get",
                      "expect": 2000000,
                    }

