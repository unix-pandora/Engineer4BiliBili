import process_json
import assign_voice
import assign_silence
from Constants import MineConstants
import paramters

voice_files_list = []
silence_files_list = []


def divide_by_type(dict_param):
    if dict_param["type"] == MineConstants.voice():
        voice_files_list.append(dict_param["path"])
    elif dict_param["type"] == MineConstants.silence():
        silence_files_list.append(dict_param["path"])


def invoking():
    summarize_json_list = process_json.read_json_file(MineConstants.summarize_file())
    print("summarize_json[i]", summarize_json_list[0])

    for i, j in enumerate(summarize_json_list):  # 枚举
        # d = ast.literal_eval(str(j))
        # print('index:{}, value:{}'.format(i,d))
        print("j", j["type"])
        divide_by_type(j)

    print("voice_files_list", voice_files_list)
    print("silence_files_list", silence_files_list)


def centrality():
    invoking()
    # silence_files_list 传给 assign_silence, voice_files_list 传给 assign_voice
    assign_voice.invoking(voice_files_list, paramters.output_directory)
    assign_silence.invoking(silence_files_list, paramters.output_directory)


centrality()
