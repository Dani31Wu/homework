# User: link
# Date: 2023/9/9
# File: 读写文件
import os.path

file_path = os.path.join(os.path.dirname(__file__), './files/rw_file.txt')
file_content = '你好，hello'
with open(file_path, 'w+', encoding='gbk') as file_:
    file_.write(file_content)

with open(file_path, 'r+') as file_:
    content = file_.read()
    print(content)

if os.path.exists(file_path):
    os.remove(file_path)
