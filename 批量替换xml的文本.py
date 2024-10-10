import os
import re
# 请做好备份
def replace_text_in_xml(folder_path, old_text, new_text):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # 使用正则表达式替换文本
                updated_content = re.sub(old_text, new_text, content)

                # 写回文件
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

# 指定文件夹路径、要替换的文本和替换后的文本
folder_path = "coco_plate_head_3.1/archive/xml"
old_text = r"licence"
new_text = r"plate"

replace_text_in_xml(folder_path, old_text, new_text)
