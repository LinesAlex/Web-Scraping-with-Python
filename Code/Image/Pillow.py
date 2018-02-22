# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:32:21 2018

@author: 11796
"""
from PIL import Image
import argparse

# 创建解析对象
parser = argparse.ArgumentParser()

# 向对象中添加命令行参数和选项
# 添加输入文件参数
parser.add_argument('file')
# 添加输出文件参数
parser.add_argument('-o', '--output')
# 添加输出字符画宽参数
parser.add_argument('-width', type = int, default = 80)
# 添加输出字符画高参数
parser.add_argument('-height', type = int, default = 80)
# 获取参数数据，使用parse_args()解析 解析对象
args = parser.parse_args()

class character():
    def __init__(self):
        self.IMG = args.file
        self.WIDTH = args.width
        self.HEIGHT = args.height
        self.OUTPUT = args.output
        # 不同字符代表不同色块，字符最好不要重复
        self.ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        self.txt = ''

    # 将256灰度映射到70个字符上
    # 图片格式为RGB的*im.getpixel((j,i)后会得到三个参数r（red），g（green），b（blue）；RGBA得到四个参数r，g，b，alpha(透明度，0表示完全透明)
    # im.getpixel((j,i))得到一个由r, g, b, alpha(如果有的话)构成的元祖，加上*号即表示拆分元祖分别赋值引用
    def get_char(self, r, g, b, alpha = 256):
        # 如果是透明的，则输出空格
        if alpha == 0:
                return ' '
        length = len(self.ascii_char)
        # r,g,b转换为灰度值，白色是255，黑色是0
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        # 单元字符的灰度值大小
        unit = (256.0 + 1)/length
        # 字符从小到大表示灰度值，已知灰度值大小，一个字符表示的灰度值大小，求该灰度值由第几个字符表示，ascii_char[i]
        return self.ascii_char[int(gray/unit)]

    def convert(self):
        im = Image.open(self.IMG)
        # im.resize(size,filter)
        # 变量filter为NEAREST、BILINEAR、BICUBIC或者ANTIALIAS之一
        # 如果忽略，或者图像模式为“1”或者“P”，该变量设置为NEAREST，速度快
        # ANTIALIAS 抗锯齿，质量最高；BICUBIC 三次样条插；BILINEAR 线性插值法
        im = im.resize((self.WIDTH,self.HEIGHT), Image.NEAREST)
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                self.txt += self.get_char(*im.getpixel((j,i)))
            self.txt += '\n'
    def save(self):
        if self.OUTPUT:
            with open(self.OUTPUT,'w') as f:
                f.write(self.txt)
        else:
            with open("output.txt",'w') as f:
                f.write(self.txt)
    def start(self):
        self.convert();
        self.save();

if __name__ == '__main__':
    c = character()
    c.start()