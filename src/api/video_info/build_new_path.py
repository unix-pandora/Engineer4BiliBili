import os


def get_new_file_path(json_dict, output_path):
    avid = json_dict["aid"]
    title = json_dict["title"]
    page = json_dict["p"]
    type = json_dict["type"]

    print("\n", "get_new_file_path:", avid, title, page, type)
    video_name = (
        str(avid) + "-" + str(title) + "-" + str(page) + "-" + str(type) + ".mp4"
    )

    # 创建一个包含需要替换的字符的列表
    replace_chars = [
        "【",
        "】",
        "《",
        "》",
        "|",
        "｜",
        "）",
        "（",
        "（",
        ")",
        "。",
        "{",
        "}",
        "？",
        "[",
        "]",
        ";",
        "；",
        "#",
        "&",
        "*",
        "@",
        "！",
        "『",
        "』",
        "~",
        "%",
        "^",
        "_",
        "「",
        "」",
        "“",
        "”",
        " ",
        ",",
        "：",
        "/",
        "(",
        ")",
        "，",
        "。",
    ]

    # 遍历列表进行替换
    for char in replace_chars:
        video_name = video_name.replace(char, "")

    video_name = output_path + os.sep + video_name
    print("\n", "get_new_file_path video name: ", str(video_name))

    return video_name
