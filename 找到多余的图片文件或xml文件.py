#找到多余的图片文件或xml文件，避免出现漏标注的情况
import os
import shutil

jpg_folder = r'D:\download\挖机铲斗\img-real'  # 指定.jpg文件的文件夹路径
xml_folder = r'D:\download\挖机铲斗\xml-real'  # 指定.xml文件的文件夹路径
extra_folder = r'D:\download\挖机铲斗\extra_folder'  #指定多余文件的存放位置

# 检查extra_folder是否存在，如果不存在则创建
if not os.path.exists(extra_folder):
    os.makedirs(extra_folder)

jpg_files = set([filename.split('.')[0] for filename in os.listdir(jpg_folder) if filename.endswith('.jpg')])
xml_files = set([filename.split('.')[0] for filename in os.listdir(xml_folder) if filename.endswith('.xml')])

# # 找到在.xml文件夹中存在,但在.jpg文件夹中不存在的文件(xml文件多了)
# extra_xml_files = xml_files - jpg_files
# extra_xml_count = len(extra_xml_files)
#
# for file in extra_xml_files:
#     # 构建原文件路径
#     src_file = os.path.join(xml_folder, f"{file}.xml")
#     # 构建目标文件路径
#     dst_file = os.path.join(extra_folder, f"{file}.xml")
#     # 移动文件
#     shutil.move(src_file, dst_file)
#     print(f"{file}.xml 文件已移动到 {extra_folder}")
# print(f"发现 {extra_xml_count} 个多余的.xml文件:")

# 找到在.jpg文件夹中存在,但在.xml文件夹中不存在的文件(图片文件多了)
extra_jpg_files = jpg_files - xml_files
extra_jpg_count = len(extra_jpg_files)

for file in extra_jpg_files:
    # 构建原文件路径
    src_file = os.path.join(jpg_folder, f"{file}.jpg")
    # 构建目标文件路径
    dst_file = os.path.join(extra_folder, f"{file}.jpg")
    # 移动文件
    shutil.move(src_file, dst_file)
    print(f"{file}.jpg 文件已移动到 {extra_folder}")
print(f"发现 {extra_jpg_count} 个多余的.jpg文件:")
