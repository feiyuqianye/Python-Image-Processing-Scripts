"""
@author: 绯雨千叶
"""
# 把视频按预设定的帧截取存为图片，新增了对丢帧图片的处理
import cv2
import os

def export_frames_from_video(video_path, save_dir, gap, count):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    frame_index = 0
    consecutive_errors = 0  # 连续错误计数

    while True:
        ret, frame = video.read()

        # 如果读取帧失败，则跳过当前帧
        if not ret:
            consecutive_errors += 1
            print(f"跳过损坏的帧：{video_path} 在帧索引 {frame_index}")
            if consecutive_errors > 100:  # 假设100个连续错误足够判断视频损坏
                print(f"视频文件可能严重损坏，停止处理：{video_path}")
                break
            continue
        else:
            consecutive_errors = 0  # 重置连续错误计数

        # 计算帧索引
        frame_index += 1

        # 根据间隔导出帧图片
        if frame_index % gap == 0:
            #frame_bgra = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            save_path = os.path.join(save_dir, f"{count:05d}.jpg")
            try:
                cv2.imwrite(save_path, frame) #frame_bgra
                print(f"成功保存帧图片：{save_path}")
            except Exception as e:
                print(f"Error occurred while exporting frame: {e}")
                continue  # 继续处理下一帧
            else:
                count += 1

    # 关闭视频文件
    video.release()

    return count

def batch_export_frames_from_videos(video_folder, save_dir, gap):
    # 创建保存路径
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 支持的视频文件格式
    video_formats = (".mp4", ".avi", ".mov", ".mkv")

    # 获取视频文件列表
    video_files = [f for f in os.listdir(video_folder) if f.lower().endswith(video_formats)]

    total_count = 0

    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
        total_count = export_frames_from_video(video_path, save_dir, gap, total_count)

    print(f"总共成功导出 {total_count} 张帧图片到 {save_dir}")

# 主函数
if __name__ == '__main__':
    VIDEO_FOLDER = r"D:\云感\数据集\d20230910"  # 视频文件夹路径,可以有中文
    SAVE_DIR = r"D:\tupian"    # 帧图片保存路径,不存在的话会自己创建，不能有中文
    GAP = 25  # 每隔多少帧导出一张图片

    batch_export_frames_from_videos(VIDEO_FOLDER, SAVE_DIR, GAP)
