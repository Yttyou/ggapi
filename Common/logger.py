"""  日志文件  """
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from Common.path_config import logs_path

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
logfile = logs_path+"/api_{0}.log".format(curTime)
fh = logging.FileHandler(logfile, mode='a',encoding='utf-8')
fh.setLevel(logging.INFO)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)
