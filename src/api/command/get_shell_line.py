import os
from director_info import DirectoryInfo


# 有声版
def build_command_line(name_param, dir_info: DirectoryInfo, output_path):
    video_name = dir_info.new_video_path
    audio_name = dir_info.new_audio_path
    print(
        "\nbuild_command_line-video_name: ",
        video_name,
        "\nbuild_command_line-audio_name: ",
        audio_name,
    )

    separator = os.sep
    name_array = os.path.split(name_param)
    print(
        "\nbuild_command_line-output_path: ",
        output_path,
        "\nbuild_command_line-name_array: ",
        name_array,
    )

    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
    command_line = [
        "ffmpeg -i ",
        str(video_name),
        " -i ",
        str(audio_name),
        " -c:v copy -c:a aac -strict experimental ",
        output_path,
        str(separator),
        str(name_array[1]),
    ]

    command_line = "".join(command_line)
    print("\nbuild_commmand_line: ", command_line)

    return command_line
