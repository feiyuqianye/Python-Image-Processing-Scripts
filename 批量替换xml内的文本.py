import os

def replace_text_in_files(source_folder, dest_folder):
    # 创建目标文件夹
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹中的所有.xml文件
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.xml'):
                source_file = os.path.join(root, file)
                dest_file = os.path.join(dest_folder, file)

                # 读取源文件内容并进行文本替换
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    replaced_content = content.replace('cyan_ball', 'ball') \     #把cyan_ball替换为ball，下方同理
                        .replace('red_ball', 'ball') \
                        .replace('blue_ball', 'ball') \
                        .replace('yellow_ball', 'ball')

                # 将替换后的内容写入目标文件夹中的文件
                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(replaced_content)

    print(f"文件处理完成，已将所有.xml文件中的指定文本替换并保存到 {dest_folder}")


# 设置源文件夹和目标文件夹路径
source_folder = r'D:\云感\数据集\小球识别\val_xml1'
dest_folder = r'D:\云感\数据集\小球识别\val_xml'

# 执行替换操作
replace_text_in_files(source_folder, dest_folder)
