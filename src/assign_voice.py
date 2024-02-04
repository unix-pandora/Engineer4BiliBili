import os
import files_list
import filter_files
import compare_files
import assemble_obj
import process_json
import build_new_path
import get_shell_line
import execute_shell
import get_binary_cont
import modify_bin_cont
from director_info import DirectoryInfo
from Constants import MineConstants


def edit_m4s_bytes(video_info_obj: DirectoryInfo, origin_path: str, media_name: str):
    file_path = ""

    if media_name == MineConstants.audio_name():
        file_path = video_info_obj.audio_path
    elif media_name == MineConstants.video_name():
        file_path = video_info_obj.video_path

    # 查看二进制文件的字节内容
    get_binary_cont.get_bin_content(file_path)
    # modified_media_file:需要被修改的媒体文件
    modified_media_file = origin_path + str(os.sep) + media_name
    # 修改二进制文件的字节内容
    modify_bin_cont.fix_m4s(file_path, modified_media_file)
    # 再次检查是否修改成功
    get_binary_cont.get_bin_content(file_path)

    return modified_media_file


def assign(origin_path, output_path):
    # 获取origin_path目录下的文件路径集合
    f_set = files_list.get_files_set(origin_path)
    # 筛选出符合条件的文件路径
    filter_array = filter_files.filter_elements(f_set)

    # 获取文件大小排序信息
    sort_dict = compare_files.compare_files(filter_array)
    # 根据获取得到的文件大小排序信息，组装更稳定的数据类
    video_info_obj = assemble_obj.get_assemble_obj(sort_dict)

    # 编辑媒体文件的二进制内容
    modified_audio_name = edit_m4s_bytes(
        video_info_obj, origin_path, MineConstants.audio_name()
    )
    video_info_obj.new_audio_path = modified_audio_name

    modified_video_name = edit_m4s_bytes(
        video_info_obj, origin_path, MineConstants.video_name()
    )
    video_info_obj.new_video_path = modified_video_name

    # 处理JSON数据内容
    dict_json = process_json.read_json_file(video_info_obj.json_path)
    dict_json["type"] = MineConstants.voice()
    # 最终的文件名称路径
    final_file_path = build_new_path.get_new_file_path(dict_json, output_path)

    # 构建命令语句
    command_line = get_shell_line.build_command_line(
        final_file_path, video_info_obj, output_path
    )
    # 执行命令
    execute_shell.execute(command_line)


def invoking(dir_list, output_folder):
    for i in dir_list:
        assign(i, output_folder)
