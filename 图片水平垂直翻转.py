# -*- coding: utf-8 -*-
"""
@author: 绯雨千叶
"""
from PIL import Image
import os
import shutil

# 输入原始图像文件夹路径
input_dir = './teeth/img1'
# 创建目标文件夹
output_dir = './teeth/img2'
os.makedirs(output_dir, exist_ok=True)


# 复制原图并保存
def copy_and_save(image_path, output_path):
    shutil.copy(image_path, output_path)


# 水平翻转并保存
def horizontal_flip_and_save(image_path, output_path):
    img = Image.open(image_path)
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_img = flipped_img.convert('RGB')  # 转换为RGB模式
    flipped_img.save(output_path)


# 垂直翻转并保存
def vertical_flip_and_save(image_path, output_path):
    img = Image.open(image_path)
    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_img = flipped_img.convert('RGB')  # 转换为RGB模式
    flipped_img.save(output_path)


# 先水平翻转再垂直翻转并保存
def horizontal_and_vertical_flip_and_save(image_path, output_path):
    img = Image.open(image_path)
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
    flipped_img = flipped_img.convert('RGB')  # 转换为RGB模式
    flipped_img.save(output_path)


# 处理每张图片
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # 只处理jpg和png格式的图片
        image_path = os.path.join(input_dir, filename)

        # 复制原图
        output_path = os.path.join(output_dir, filename)
        copy_and_save(image_path, output_path)

        # 水平翻转并保存
        output_path = os.path.join(output_dir, 'horizontal_' + filename)
        horizontal_flip_and_save(image_path, output_path)

        # 垂直翻转并保存
        output_path = os.path.join(output_dir, 'vertical_' + filename)
        vertical_flip_and_save(image_path, output_path)

        # 先水平翻转再垂直翻转并保存
        output_path = os.path.join(output_dir, 'horizontal_vertical_' + filename)
        horizontal_and_vertical_flip_and_save(image_path, output_path)
