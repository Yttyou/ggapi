"""  用来写一些基础的方法  """
import random

class BaseDef:

    # 随机生成字符串
    def random_str_china(self):
        val = random.randint(0x4e00, 0x9fbf)
        return chr(val)

    # 生成一个手机号
    def random_iphone(self):
        code = '132'
        for i in range(8):
            num = random.randint(0,9)
            code = code+str(num)
        print(code)
        return code

if __name__ == '__main__':
    a=BaseDef().random_iphone()
    print(a)