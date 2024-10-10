#情况：xml文件名和里面的filename文件名不一致，要把filename修改为和xml文件名一样的图片名字
import os
import xml.etree.ElementTree as ET

def batch_process_xml_files(folder_path):
    # 遍历目标文件夹中的所有XML文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            xml_file = os.path.join(folder_path, filename)

            # 解析XML文件
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # 获取XML文件名（不包括扩展名）
            xml_file_name = os.path.splitext(filename)[0]

            # 修改<filename>部分的内容为与XML文件名一致
            for elem in root.iter('filename'):
                elem.text = f'{xml_file_name}.jpg'

            # 保存修改后的XML文件
            tree.write(xml_file)

# 指定包含XML文件的文件夹路径
folder_path = r'C:\Users\train_xml_8000'

# 执行批量处理XML文件的函数
batch_process_xml_files(folder_path)
