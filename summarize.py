import files_list
import filter_files
import compare_files
import assemble_obj
import get_directories
import forge_obj
import deals_content
from Constants import MineConstants
import paramters


def generate_summarize_json(media_info):
    media_array = []
    media_array.append(media_info)
    deals_content.append_to_file(media_array, MineConstants.summarize_file())
    deals_content.replace_string_in_file(MineConstants.summarize_file(), "][", ",")


def assign(origin_path):
    # 获取origin_path目录下的文件路径集合
    f_set = files_list.get_files_set(origin_path)

    # 筛选出符合条件的文件路径
    filter_array = filter_files.filter_elements(f_set)

    # 获取文件大小排序信息
    sort_dict = compare_files.compare_files(filter_array)

    # 根据获取得到的文件大小排序信息，组装更稳定的数据类
    video_info_obj = assemble_obj.get_assemble_obj(sort_dict)

    # 构建JSON数据类
    media_info = forge_obj.forge_media_info(video_info_obj, origin_path)
    generate_summarize_json(media_info)


def invoking():
    dirs_set = get_directories.get_dirs(paramters.resource_directory)
    for index in dirs_set:
        print("index: ", str(index))
        assign(index)


invoking()
