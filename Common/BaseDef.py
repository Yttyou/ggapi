"""  用来写一些基础的方法  """
import random

class BaseDef:
    # 随机生成字符串
    def random_str_china(self):
        val = random.randint(0x4e00, 0x9fbf)
        return chr(val)


if __name__ == '__main__':
    a=BaseDef().random_str_china()
    print(a)