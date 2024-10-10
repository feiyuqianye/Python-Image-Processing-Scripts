# -*- coding: utf-8 -*-
"""
@author: 绯雨千叶
清华源：https://pypi.tuna.tsinghua.edu.cn/simple
"""
from PIL import Image
import os

# 定义输入和输出文件夹路径
input_folder = r'C:\Users\ball_gray1'  # 存放原始图片的文件夹
output_folder = r'C:\Users\ball_gray2'  # 存放灰度图的文件夹

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有文件名
files = os.listdir(input_folder)

# 遍历每个文件
for file in files:
    # 构建输入文件的完整路径
    input_path = os.path.join(input_folder, file)

    # 打开图像文件
    image = Image.open(input_path)

    # 转换为灰度图像
    gray_image = image.convert('L')

    # 构建输出文件的完整路径，保持文件名不变
    output_path = os.path.join(output_folder, file)

    # 保存灰度图像
    gray_image.save(output_path)

print("转换完成！")
