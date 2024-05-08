"""
@author: 绯雨千叶
Github:https://github.com/feiyuqianye/Python-Image-Processing-Scripts
批量按顺序重命名文件夹中的图片文件
"""
import os
import glob
import shutil

class BatchRename():
    def __init__(self):
        self.path = './teeth/img2'      # 表示需要命名处理的文件夹
        self.save_path = './teeth/img'  # 保存重命名后的图片地址
        self.start_index = 0            # 排序的初始值

    def rename(self):
        # 获取所有图片文件路径并排序
        filelist = sorted(glob.glob(os.path.join(self.path, '*.jpg')) + glob.glob(os.path.join(self.path, '*.jpeg')) + glob.glob(os.path.join(self.path, '*.png')))
        i = self.start_index  # 设置初始值
        if not os.path.exists(self.save_path):  # 如果保存路径不存在，则创建
            os.makedirs(self.save_path)
        for src in filelist:  # 遍历源文件列表
            _, ext = os.path.splitext(src)        # 获取文件扩展名
            new_name = '{:05d}{}'.format(i, ext)  # 新的文件名
            dst = os.path.join(self.save_path, new_name)  # 目标文件路径
            shutil.copy2(src, dst)  # 复制文件到目标位置
            print('renaming {} to {}'.format(os.path.basename(src), new_name))
            i += 1  # 递增序号

        print('Total {} images renamed and rearranged.'.format(len(filelist)))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
