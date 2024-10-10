import os
import glob
import shutil


class BatchRename():
    def __init__(self):
        self.path = './测试视频'  # 表示需要命名处理的文件夹
        self.save_path = './测试视频'  # 保存重命名后的地址
        self.start_index = 1  # 排序的初始值

    def rename(self):
        filelist = sorted(glob.glob(os.path.join(self.path, '*.avi')) + glob.glob(os.path.join(self.path, '*.mp4')) + glob.glob(os.path.join(self.path, '*.mov')))
        i = self.start_index  # 设置初始值
        if not os.path.exists(self.save_path):  # 如果保存路径不存在，则创建
            os.makedirs(self.save_path)
        for src in filelist:  # 遍历源文件列表
            _, ext = os.path.splitext(src)  # 获取文件扩展名
            new_name = '{:04d}{}'.format(i, ext)  # 新的文件名
            dst = os.path.join(self.save_path, new_name)  # 目标文件路径
            shutil.copy2(src, dst)  # 复制文件到目标位置
            print('renaming {} to {}'.format(os.path.basename(src), new_name))
            i += 1  # 递增序号

        print('Total {} videos renamed and rearranged.'.format(len(filelist)))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
