import os
import re


def filter_elements(file_set):
    filtered_list = list()
    m4s_pattern = r".*.m4s"

    for ele in file_set:
        extension = get_last_element(ele)
        print("extension= ", extension)

        if re.search(m4s_pattern, extension):
            filtered_list.append(ele)
        elif extension == ".videoInfo":
            filtered_list.append(ele)

    print("\nfiltered_list: ", filtered_list)
    return filtered_list


def get_last_element(string):
    # 按地址分隔符进行截取，得到一个数组
    path_parts = os.path.split(string)
    # 数组中的最后一个元素
    return path_parts[1]
