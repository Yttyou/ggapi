"""   动态相关-api接口参数   """

from TestData.api_data import iphone,pwd,api_url
from Common.BaseDef import BaseDef
from Common.path_config import testdatafile_path

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

    # 发布动态视频
    api_data_002 = {"url": api_url + "newapi/api/userState/sendState",
                       "parame": {"title": "这是一个动态测试-"+ BaseDef().random_str_china(),
                                  "video": testdatafile_path+'\\1111.jpeg',
                                  "video_cover": testdatafile_path + '\\5555.mp4',
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


    # 广场-关注-关注动态展示位
    api_data_009 = {"url": api_url + "newapi/api/userState/getComment",
                       "parame": {
                                    "state_id": ''
                                  },
                       "Method": "get",
                       "expect": 2000000
                      }






