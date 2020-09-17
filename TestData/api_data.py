"""  用来存储api测试数据  """

from Common.BaseDef import BaseDef
import time
import datetime

# 注册/登录手机号
iphone = '13297025029'
pwd = 'aaa111'
new_pwd = 'bbb000'
update_pwd = '111aaa'
code_iphone = '13297025057'     # 可接受验证码的手机号

player_iphone = '13299999999'   # 玩家大神手机号(**注意：这里账号是配套的不能随意更改)
player_uid = 75766566           # 大神的uid

Room_iphone = '18602753258'     # 房主账号
Room_id = '1200064'             # 聊天室id

# api_url = "https://ggapi.qwdj.com/"        # 测试服
api_url = "https://preggapi.qwdj.com/"        # 预发布

random_number = BaseDef().random_str_china()     # 获取一个随机数

stime = int(time.mktime(time.strptime((datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')))    # 获取1小时后的时间戳

class UserData:

    # 批量手机号登陆注册
    api_iphone_login = {"url": api_url + "newapi/api/user/register",
                    "parame": {"account_type": "1",
                               "password":"c9a1520e172b07abceba847739b664bc",
                               "phonenum": '',
                               "verify_code": '1111',
                               },
                    "Method": "post",
                    "expect": 2000000
                    }

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

    # 获取已经开起聊天室的id
    api_data_034_a = {"url": api_url + "newapi/api/chatroom/getListByCon",
                    "parame": {"is_open": '1'
                               },
                    "Method": "get",
                    "expect": 2000000,
                    }

    # 根据id获取聊天室信息(id不存在)
    api_data_034_b = {"url": api_url + "newapi/api/chatroom/getById",
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

    # 用户A登录
    api_data_040_a = {"url": api_url + "newapi/api/user/login",
                       "parame": {"account_type": "2",
                                  "phonenum": '13259512655',
                                  "verify_code": 1111,
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # 用户B登录
    api_data_041_a = {"url": api_url + "newapi/api/user/login",
                      "parame": {"account_type": "2",
                                 "phonenum": '13259512656',
                                 "verify_code": 1111,
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 用户C登录
    api_data_042_a = {"url": api_url + "newapi/api/user/login",
                      "parame": {"account_type": "2",
                                 "phonenum": '13259512657',
                                 "verify_code": 1111,
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 上麦申请
    api_data_040 = {"url": api_url + "newapi/api/chatroomMikeApply/apply",
                       "parame": {
                                  "chatroom_id": Room_id,
                                  "type": 1
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # 用户取消申请上麦
    api_data_040_b = {"url": api_url + "newapi/api/chatroomMikeApply/cancel",
                       "parame": {
                                  "chatroom_id": Room_id
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # 用户C加入房间
    api_data_040_c = {"url": api_url + "newapi/api/chatroom/join",
                      "parame": {
                          "chatroom_id": Room_id
                      },
                      "Method": "get",
                      "expect": 2000000
                      }

    # 房主登录
    api_data_Homeowner_login = {"url": api_url + "newapi/api/user/login",
                                "parame": {"account_type": "2",
                                            "phonenum": Room_iphone,
                                            "verify_code": 1111,
                                            },
                                "Method": "post",
                                "expect": 2000000
                                }

    # 房主开启聊天室
    api_data_043 = {"url": api_url + "newapi/api/chatroomAdmin/chatroom/open",
                                "parame": {
                                            "type": "31"
                                            },
                                "Method": "post",
                                "expect": 2000000
                                }

    # 获取聊天室麦位申请列表
    api_data_044 = {"url": api_url + "newapi/api/chatroomMikeApply/getListByCon",
                                "parame": {
                                            "chatroom_id": Room_id
                                            },
                                "Method": "get",
                                "expect": 2000000
                                }

    # 房主将用户A取消主持
    api_data_045_a = {"url": api_url + "newapi/api/chatroomAdmin/chatroomMc/cancelMc",
                        "parame": {
                                    "chatroom_id": Room_id,
                                    "user_id": ''
                                    },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 房主将用户A设置为主持
    api_data_045_b = {"url": api_url + "newapi/api/chatroomAdmin/chatroomMc/setMc",
                                "parame": {
                                            "chatroom_id": Room_id,
                                            "user_id": ''
                                            },
                                "Method": "post",
                                "expect": 2000000
                                }

    # 获取聊天室主持列表
    api_data_046 = {"url": api_url + "newapi/api/chatroomMc/getListByCon",
                                "parame": {
                                            "chatroom_id": Room_id,
                                            },
                                "Method": "get",
                                "expect": 2000000
                                }

    # 聊天室中查看用户信息
    api_data_047 = {"url": api_url + "newapi/api/chatroom/user",
                                "parame": {
                                            "chatroom_id": Room_id,
                                            "user_id": ''
                                            },
                                "Method": "get",
                                "expect": 2000000
                                }

    # 房主更新聊天室信息
    api_data_048 = {"url": api_url + "newapi/api/chatroomAdmin/chatroom/edit",
                                "parame": {
                                            "chatroom_id": Room_id,
                                            "name": '直播间-'+BaseDef().random_str_china()
                                            },
                                "Method": "post",
                                "expect": 2000000
                                }

    # 房主给与申请上麦通过
    api_data_049 = {"url": api_url + "newapi/api/chatroomAdmin/chatroomMikeApply/approve",
                    "parame": {
                        "user_id" : '',
                        "chatroom_id": Room_id,
                        "chatroom_mike_apply_id": ''  # 麦位申请编号
                    },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 房主设置麦位锁定
    api_data_048_a = {"url": api_url + "newapi/api/chatroomAdmin/chatroomMike/setLock",
                                "parame": {
                                            "chatroom_id": Room_id,
                                            "chatroom_mike_id": ''        # 麦位编号
                                            },
                                "Method": "post",
                                "expect": 2000000
                                }

    # 房主设置麦位锁定取消
    api_data_048_b = {"url": api_url + "newapi/api/chatroomAdmin/chatroomMike/cancelLock",
                      "parame": {
                          "chatroom_id": Room_id,
                          "chatroom_mike_id": ''  # 麦位编号
                      },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 房主给与申请上麦驳回
    api_data_050 = {"url": api_url + "newapi/api/chatroomAdmin/chatroomMikeApply/reject",
                                "parame": {
                                            "chatroom_id": Room_id,
                                            "chatroom_mike_apply_id": ''        # 麦位申请编号
                                            },
                                "Method": "post",
                                "expect": 2000000
                                }

    # 房主将用户抱下麦
    api_data_051 = {"url": api_url + "newapi/api/chatroomAdmin/chatroomMike/underMike",
                    "parame": {
                        "chatroom_id": Room_id,
                        "chatroom_mike_id": ''  # 麦位编号
                    },
                    "Method": "post",
                    "expect": 2000000
                    }









# 礼物相关测试数据
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

    # 获取礼盒(有效)
    api_get_box = {"url": api_url + "newapi/api/box/getListByCon",
                      "parame": {"is_show": "1",    # 1 展示有效
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

    # 根据条件获取礼盒列表
    api_data_050_a = {"url": api_url + "newapi/api/box/getListByCon",
                      "parame": {'is_show': "1"
                                },
                      "Method": "get",
                      "expect": 2000000,
                     }

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

    # 前置：获取已存在的聊天室id
    api_data_061_a = {"url": api_url + "newapi/api/chatroom/getListByCon",
                      "parame": {"is_open": '1'
                                 },
                      "Method": "get",
                      "expect": 2000000,
                      }

    # 加入聊天室-房间编号存在（通过全局变量ID传参）
    api_data_061_b = {"url": api_url + "newapi/api/chatroom/join",
                      "parame": {"chatroom_id":''
                               },
                      "Method": "get",
                      "expect": 2000000,
                    }

    # 聊天室送钻石礼物(正确流)
    api_data_061_c = [{"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送1钻石礼物",
                       "parame": {"chatroom_id": '',      # 聊天室id
                                 "gift_id": '',          # 礼物id
                                 "amount": 1,            # 礼物数量
                                 "to_chatroom_user_id_with_mike_pos_arr": []    # 收礼用户id和麦位号
                                },
                       "Method": "post",
                       "expect": 2000000,
                      },
                      {"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送2个钻石礼物",
                       "parame": {"chatroom_id": '',  # 聊天室id
                                  "gift_id": '',  # 礼物id
                                  "amount": 2,  # 礼物数量
                                  "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                  },
                       "Method": "post",
                       "expect": 2000000,
                       },
                      {"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送10个钻石礼物",
                       "parame": {"chatroom_id": '',  # 聊天室id
                                  "gift_id": '',  # 礼物id
                                  "amount": 10,  # 礼物数量
                                  "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                  },
                       "Method": "post",
                       "expect": 2000000,
                       },
                      ]

    # 聊天室送钻石礼物(错误流)
    api_data_062 = [{"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送0个钻石礼物",
                       "parame": {"chatroom_id": '',      # 聊天室id
                                 "gift_id": '',          # 礼物id
                                 "amount": 0,            # 礼物数量
                                 "to_chatroom_user_id_with_mike_pos_arr": []    # 收礼用户id和麦位号
                                },
                       "Method": "post",
                       "expect": 2006008,
                      },
                      {"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送-1个钻石礼物",
                       "parame": {"chatroom_id": '',  # 聊天室id
                                  "gift_id": '',  # 礼物id
                                  "amount": -1,  # 礼物数量
                                  "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                  },
                       "Method": "post",
                       "expect": 2006008,
                       },
                      {"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送None个钻石礼物",
                       "parame": {"chatroom_id": '',  # 聊天室id
                                  "gift_id": '',  # 礼物id
                                  "amount": None,  # 礼物数量
                                  "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                  },
                       "Method": "post",
                       "expect": 2001003,
                       },
                        {"url": api_url + "newapi/api/gift/sendChatroomGift",
                         "api_title": "礼物个数amount值为True",
                         "parame": {"chatroom_id": '',  # 聊天室id
                                    "gift_id": '',  # 礼物id
                                    "amount": True,  # 礼物数量
                                    "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                    },
                         "Method": "post",
                         "expect": 2001003,
                         },
                      ]

    # 聊天室送呱币礼物
    api_data_063 = [{"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送1呱币礼物",
                       "parame": {"chatroom_id": '',      # 聊天室id
                                 "gift_id": '',          # 礼物id
                                 "amount": 1,            # 礼物数量
                                 "to_chatroom_user_id_with_mike_pos_arr": []    # 收礼用户id和麦位号
                                },
                       "Method": "post",
                       "expect": 2006002,
                      },
                      {"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送0个呱币礼物",
                       "parame": {"chatroom_id": '',  # 聊天室id
                                  "gift_id": '',  # 礼物id
                                  "amount": 0,  # 礼物数量
                                  "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                  },
                       "Method": "post",
                       "expect": 2006008,
                       },
                      {"url": api_url + "newapi/api/gift/sendChatroomGift",
                       "api_title": "送10个呱币礼物",
                       "parame": {"chatroom_id": '',  # 聊天室id
                                  "gift_id": '',  # 礼物id
                                  "amount": True,  # 礼物数量
                                  "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                  },
                       "Method": "post",
                       "expect": 2001003,
                       },
                      ]

    # 聊天室送礼盒（正确流）
    api_data_064 = [{"url": api_url + "newapi/api/gift/sendChatroomBox",
                       "api_title": "送1个礼盒",
                       "parame": {"chatroom_id": '',      # 聊天室id
                                 "box_id": '',          # 礼盒id
                                 "amount": 1,            # 礼盒数量
                                 "to_chatroom_user_id_with_mike_pos_arr": []    # 收礼用户id和麦位号
                                },
                       "Method": "post",
                       "expect": 2000000,
                      },
                      {"url": api_url + "newapi/api/gift/sendChatroomBox",
                       "api_title": "送2个礼盒",
                       "parame": {"chatroom_id": '',
                                  "box_id": '',
                                  "amount": 2,
                                  "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                  },
                       "Method": "post",
                       "expect": 2000000,
                       },
                      ]

    # 聊天室送礼盒（错误流）
    api_data_065 = [{"url": api_url + "newapi/api/gift/sendChatroomBox",
                       "api_title": "送0个礼盒",
                       "parame": {"chatroom_id": '',      # 聊天室id
                                 "box_id": '',          # 礼盒id
                                 "amount": 0,            # 礼盒数量
                                 "to_chatroom_user_id_with_mike_pos_arr": []    # 收礼用户id和麦位号
                                },
                       "Method": "post",
                       "expect": 2006008,
                      },
                      {"url": api_url + "newapi/api/gift/sendChatroomBox",
                       "api_title": "送-1个礼盒",
                       "parame": {"chatroom_id": '',
                                  "box_id": '',
                                  "amount": -1,
                                  "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                  },
                       "Method": "post",
                       "expect": 2006008,
                       },
                    {"url": api_url + "newapi/api/gift/sendChatroomBox",
                     "api_title": "送None个礼盒",
                     "parame": {"chatroom_id": '',
                                "box_id": '',
                                "amount": 2001003,
                                "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                },
                     "Method": "post",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/gift/sendChatroomBox",
                     "api_title": "礼盒数amount值为True",
                     "parame": {"chatroom_id": '',
                                "box_id": '',
                                "amount": True,
                                "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                },
                     "Method": "post",
                     "expect": 2001003,
                     }
                      ]

    # 聊天室送礼盒-聊天室不存在
    api_data_066 = {"url": api_url + "newapi/api/gift/sendChatroomBox",
                       "parame": {"chatroom_id": 1200000,      # 聊天室id
                                 "box_id": '',          # 礼盒id
                                 "amount": 1,            # 礼盒数量
                                 "to_chatroom_user_id_with_mike_pos_arr": []    # 收礼用户id和麦位号
                                },
                       "Method": "post",
                       "expect": 2005001
                      }

    # 聊天室送礼盒-礼盒id不存在
    api_data_067 = {"url": api_url + "newapi/api/gift/sendChatroomBox",
                     "parame": {"chatroom_id": '',
                                "box_id": '',
                                "amount": 1,
                                "to_chatroom_user_id_with_mike_pos_arr": []  # 收礼用户id和麦位号
                                },
                     "Method": "post",
                     "expect": 2006011,
                     }

    # 获取礼物订单列表
    api_data_068 = [{"url": api_url + "newapi/api/giftOrder/getListByCon",
                     'api_title': "正确流组合筛选",
                     "parame": {"page": '2',
                                "level": '2',
                                "type": '1',
                                "is_contribute": 1
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/giftOrder/getListByCon",
                     'api_title': "等级0：带A用户信息，呱币礼物",
                     "parame": {"page": '1',
                                "level": '0',
                                "type": '2',
                                "is_contribute": 0
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    {"url": api_url + "newapi/api/giftOrder/getListByCon",
                     'api_title': "默认筛选",
                     "parame": {
                                },
                     "Method": "get",
                     "expect": 2000000,
                     },
                    ]


# 技能相关
class SkillRelatedApi:

    # 获取技能列表
    skill_data_001 = {"url": api_url + "oldapi/api/skill/skill_list/list",
                      "parame": {
                      },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 大神技能列表
    skill_data_002 = {"url": api_url + "oldapi/api/skill/my_index/group_list",
                      "parame": {
                      },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 大神技能列表
    skill_data_003 = {"url": api_url + "oldapi/api/skill/skill_list/state_visiter",
                      "parame": {'visiter': player_uid
                      },
                      "Method": "post",
                      "expect": 2000000,
                      }



# 陪玩订单相关
class OrderApi:

    # 获取大神列表
    order_data_001 = {"url": api_url + "oldapi/api/skill/skill_list/god_list",
                      "parame": {'perpage': 10
                      },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 用户提交订单（错误流）
    order_data_002 = [{"url": api_url + "oldapi/api/orders/operate_order/submit",
                       'api_title': "用户id不存在",
                       "parame": {'receiver': 1000000,
                                 'skill_id': 57,
                                 'num': 1,
                                 'user_skill_id': 7,
                                 'stime': stime,
                                 'mark': "api自动化测试",
                                 },
                      "Method": "post",
                      "expect": 2001003,
                      },
                      {"url": api_url + "oldapi/api/orders/operate_order/submit",
                       'api_title': "技能id错误",
                       "parame": {'receiver': 58908854,
                                  'skill_id': 88,
                                  'num': 1,
                                  'user_skill_id': 7,
                                  'stime': stime,
                                  'mark': "api自动化测试",
                                  },
                       "Method": "post",
                       "expect": 2001003,
                       },
                      {"url": api_url + "oldapi/api/orders/operate_order/submit",
                       'api_title': "数量为0",
                       "parame": {'receiver': 58908854,
                                  'skill_id': 57,
                                  'num': 0,
                                  'user_skill_id': 7,
                                  'stime': stime,
                                  'mark': "api自动化测试",
                                  },
                       "Method": "post",
                       "expect": 2001003,
                       },
                      {"url": api_url + "oldapi/api/orders/operate_order/submit",
                       'api_title': "数量为-1",
                       "parame": {'receiver': 58908854,
                                  'skill_id': 57,
                                  'num': -1,
                                  'user_skill_id': 7,
                                  'stime': stime,
                                  'mark': "api自动化测试",
                                  },
                       "Method": "post",
                       "expect": 2001003,
                       },
                      {"url": api_url + "oldapi/api/orders/operate_order/submit",
                       'api_title': "用户技能id错误",
                       "parame": {'receiver': 58908854,
                                  'skill_id': 999,
                                  'num': 1,
                                  'user_skill_id': 45,
                                  'stime': stime,
                                  'mark': "api自动化测试",
                                  },
                       "Method": "post",
                       "expect": 2001003,
                       },
                      ]


    # 用户提交订单（正确流）
    order_data_003 = {"url": api_url + "oldapi/api/orders/operate_order/submit",
                      "parame": {'receiver': '',
                                 'skill_id': '',
                                 'num': 1,
                                 'user_skill_id': '',
                                 'stime': stime,
                                 'mark': "api自动化测试",
                                },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 用户取消订单
    order_data_004 = {"url": api_url + "oldapi/api/orders/operate_order/cancel_order",
                      "parame": {'order_id': '',
                                 "reason": "你好菜，不想玩了，下次再来！"
                                },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 查询取消订单状态
    order_data_004_a = {"url": api_url + "oldapi/api/orders/operate_order/getOrderStu",
                      "parame": {
                                 "trade_no": "你好菜，不想玩了，下次再来！"
                                 },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 订单支付-正确流
    order_data_006 = {"url": api_url + "oldapi/api/orders/operate_order/paysubmit",
                      "parame": {"order_id": "",
                                 "paytype": "3"  # 1-支付宝，2-微信，3-余额
                                 },
                      "Method": "post",
                      "expect": 2000000,
                      }

    # 大神登录账号
    order_data_007_a = {"url": api_url + "newapi/api/user/login",
                      "parame": {"account_type": "2",
                                 "phonenum": player_iphone,
                                 "verify_code": 1111,
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 大神同意接单
    order_data_007_b = {"url": api_url + "oldapi/api/orders/operate_order/take_order",
                      "parame": {
                                 "order_id": ''
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 大神点击立即服务
    order_data_008 = {"url": api_url + "oldapi/api/orders/operate_order/server",
                      "parame": {
                                 "order_id": ''
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 用户同意立即服务
    order_data_009 = {"url": api_url + "oldapi/api/orders/operate_order/agree_server",
                      "parame": {
                                 "order_id": ''
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 查询钱包首页-获取余额
    order_data_010 = {"url": api_url + "newapi/api/userWallet/index",
                      "parame": {
                      },
                      "Method": "get",
                      "expect": 2000000
                      }

    # 用户确认完成
    order_data_011 = {"url": api_url + "oldapi/api/orders/operate_order/done_order",
                      "parame": {
                                 "order_id": ''
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 大神拒单
    order_data_012 = {"url": api_url + "oldapi/api/orders/operate_order/refuse_order",
                      "parame": {
                                 "order_id": ''
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 用户拒绝立即服务
    order_data_013_a = {"url": api_url + "oldapi/api/orders/operate_order/refuse_server",
                      "parame": {
                                 "order_id": ''
                                 },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 用户申请退款
    order_data_013_b = {"url": api_url + "newapi/api/gameOrderRefundApply/apply",
                        "parame": {
                            "game_order_id": '',      # 陪玩订单id
                            "apply_reason": "0",
                            "apply_target": "0",
                            "target_id": player_uid,
                            "apply_type": "0"
                        },
                        "Method": "post",
                        "expect": 2000000
                        }

    # 大神同意退款
    order_data_013_c = {"url": api_url + "oldapi/api/orders/operate_refund/agree_refund",
                      "parame": {
                                 "order_id": '',
                                 "rfid": ''
                                 },
                      "Method": "post",
                      "expect": 2000000
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


