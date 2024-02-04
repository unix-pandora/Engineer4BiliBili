import os


def get_dirs(folder_path):
    # 初始化集合
    dirs = set()

    # 遍历文件夹路径中的所有目录
    for dir_name in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir_name)

        # 如果是目录，则加入集合
        if os.path.isdir(dir_path):
            dirs.add(dir_path)

    print("\nget_directories: ", dirs)
    return dirs


def get_dir_list(folder_path):
    directories_list = list()

    # 遍历文件夹路径中的所有目录
    for dir_name in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir_name)

        # 如果是目录，则加入集合
        if os.path.isdir(dir_path):
            directories_list.append(dir_path)

    print("\nget_directories_list: ", directories_list)
    return directories_list
