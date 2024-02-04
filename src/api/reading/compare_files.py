import os

from collections import OrderedDict
from Constants import MineConstants


def compare_files(files_list: list):
    mark_list = [MineConstants.min(), MineConstants.med(), MineConstants.max()]
    size_list = []

    for i in files_list:
        size_list.append(os.path.getsize(i))

    file_size_dict = OrderedDict(zip(files_list, size_list))
    print("\n", "file_size_dict: ", file_size_dict)

    sorted_list = sorted(file_size_dict)
    mark_files_dict = get_mark_files(mark_list, sorted_list)

    return mark_files_dict


def get_mark_files(mark_list: list, sorted_list: list):
    size_list = []

    for item in sorted_list:
        size_list.append(item[0])

    print("\n", "mark_list: ", mark_list)
    print("\n", "size_list: ", size_list)

    mark_file_dict = OrderedDict(zip(mark_list, size_list))
    print("\n", "mark_files_dict: ", mark_file_dict)

    return mark_file_dict


def sorted(file_size_dict: dict):
    # 定义一个空列表
    sorted_list = []

    # 遍历原始字典的键值对
    for key in file_size_dict.keys():
        value = file_size_dict[key]
        # 将键值对加入到排序后的列表中
        sorted_list.append((key, value))

    bubble(sorted_list)
    print(
        "\n",
        "sorted_list: ",
        sorted_list,
    )

    # 打印排序后的结果
    for item in sorted_list:
        print(f"key={item[0]} : value={item[1]}")
    return sorted_list


def bubble(sorted_list):
    # 使用冒泡方法按照值对列表进行排序
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - 1):
            if sorted_list[j][1] > sorted_list[j + 1][1]:
                # 交换元素
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
