"""   动态相关-api接口参数   """

from TestData.api_data import iphone,pwd,api_url
from Common.BaseDef import BaseDef
from Common.path_config import testdatafile_path


# 动态相关测试数据
class MovingApiData:

    # 登录参数
    api_data_001 = {"url": api_url + "newapi/api/user/login",
                       "parame": {"account_type": "2",
                                  "phonenum": iphone,
                                  "verify_code": 1111,
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # 给动态列表中第一条发布的动态点赞
    api_data_002_a = {"url": api_url + "oldapi/api/state/state_info/like",
                    "parame": {
                               "f_table_type": 'user_state',
                               "f_table_id":''
                               },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 发布一个动态(视频)
    api_data_002 = {"url": api_url + "newapi/api/userState/sendState",
                       "parame": {"title": "😘😘这是一个api接口动态视频测试-"+ BaseDef().random_str_china(),
                                  "video": 'https://static.gg6.com.cn/up/2108086815991862290357548.mp4',
                                  "video_cover": 'https://static.gg6.com.cn/up/2108086815991862290357548.mp4?x-oss-process=video/snapshot,t_10000,m_fast',
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # 发布一个动态(图片)
    api_data_002_b = {"url": api_url + "newapi/api/userState/sendState",
                    "parame": {"title": "这是一个api接口动态图片测试-" + BaseDef().random_str_china(),
                               "pic": 'http://www.chinanews.com/cul/2018/01-08/U322P4T8D8418615F107DT20180108102000.jpg,'
                                        'https://pic1.zhimg.com/v2-3b4fc7e3a1195a081d0259246c38debc_b.jpg',
                               },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 广场动态
    api_data_003 = {"url": api_url + "oldapi/api/state/statelist/states_all",
                       "parame": {
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # 动态点赞错误流(id不存在)
    api_data_003_b = {"url": api_url + "oldapi/api/state/state_info/like",
                    "parame": {
                               "f_table_type": 'user_state',
                               "f_table_id":45125
                               },
                    "Method": "post",
                    "expect": 2000013
                    }

    # 删除动态
    api_data_003_c = {"url": api_url + "newapi/api/userState/deleteById",
                      "parame": {
                          "id": ''
                      },
                      "Method": "post",
                      "expect": 2000000
                      }

    # 删除动态(动态ID不存在)
    api_data_003_d = {"url": api_url + "newapi/api/userState/deleteById",
                      "parame": {
                          "id": 99999
                      },
                      "Method": "post",
                      "expect": 2008001
                      }

    # 非自己发的动态
    api_data_003_e = {"url": api_url + "newapi/api/userState/deleteById",
                      "parame": {
                          "id": 142
                      },
                      "Method": "post",
                      "expect": 2008002
                      }

    # 广场-关注-关注动态展示位
    api_data_004 = {"url": api_url + "oldapi/api/state/statelist/states_attend",
                       "parame": {
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # 广场-关注-关注动态展示位
    api_data_005 = {"url": api_url + "oldapi/api/state/statelist/state_visiter",
                       "parame": {
                                    'visiter': ''
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }

    # 动态详情
    api_data_006 = {"url": api_url + "oldapi/api/state/state_info/state_info",
                    "parame": {
                        'id': ''
                    },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 动态详情(动态id不存在)
    api_data_007 = {"url": api_url + "oldapi/api/state/state_info/state_info",
                    "parame": {
                        'id': 9999
                    },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 给动态评论
    api_data_008 = {"url": api_url + "newapi/api/comment/send",
                    "parame": {
                        'f_table_type': 'user_state',
                        'f_table_id': '',
                        'comment': 'api自动化评论-'+BaseDef().random_str_china()
                    },
                    "Method": "post",
                    "expect": 2000000
                    }

    # 获取动态评论及礼物列表
    api_data_009 = {"url": api_url + "newapi/api/userState/getComment",
                       "parame": {
                                    "state_id": ''
                                  },
                       "Method": "get",
                       "expect": 2000000
                      }

    # 广场-关注-关注动态展示位
    api_data_010 = {"url": api_url + "oldapi/api/state/statelist/states_attend",
                       "parame": {
                                  },
                       "Method": "post",
                       "expect": 2000000
                      }



