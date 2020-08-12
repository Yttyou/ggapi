"""  项目中文件路径处理  """

import os

# 项目文件根路径
base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 测试报告-html路径
testreport_path = os.path.join(base_path,"HtmlTestReport")

# 脚本运行log路径
logs_path = os.path.join(base_path,"Logs")

# 测试数据路径
testdatas_path = os.path.join(base_path,"TestData")

# 测试用例路径
testcases_path = os.path.join(base_path,"TestCases")