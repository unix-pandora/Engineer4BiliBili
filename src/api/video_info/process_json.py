import json
import chardet


def read_json_file(file_path):
    # 检测文件编码
    with open(file_path, "rb") as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)
        encoding = result["encoding"]
        print("encoding ", encoding)

    # 根据编码打开文件并读取内容
    with open(file_path, "r", encoding=encoding, errors="ignore") as file:
        clean_content = file.read()

        print("\nclean_content: ", clean_content)

        data = json.loads(clean_content)
        print("\nread_json_file: ", data)

    return data
