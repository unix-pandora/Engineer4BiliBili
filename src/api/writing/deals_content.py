import os


def append_to_file(content, text_path):
    # 如果content不是字符串类型，将其转换为字符串
    if not isinstance(content, str):
        content = str(content)

    # 检查文件是否存在，如果不存在则创建
    if not os.path.exists(text_path):
        open(text_path, "w").close()

    # 打开文件并追加内容
    with open(text_path, "a", encoding="utf-8") as file:
        file.write(content)


def replace_string_in_file(text_path, old_string, new_string):
    # 打开文件并读取内容
    with open(text_path, "r", encoding="utf-8", errors="replace") as file:
        filedata = file.read()

    # 替换字符串
    filedata = filedata.replace(old_string, new_string)

    # 将替换后的内容写回文件
    with open(text_path, "w", encoding="utf-8", errors="replace") as file:
        file.write(filedata)
