import random
def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    file.writelines(data)
    file.close()
    print("保存文件成功")


if __name__ == '__main__':
    data ="aaabbb"+"\n"
    text_save('F:\API_TEST\TestData\sd.csv',data)