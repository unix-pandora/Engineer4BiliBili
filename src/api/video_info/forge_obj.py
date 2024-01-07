import process_json
from media_info import MediaInfo
from Constants import MineConstants

def forge_media_info(video_info_obj,origin_path):
  # 处理JSON数据内容
  dict_json=process_json.read_json_file(video_info_obj.json_path)
  
  # 默认设为有声模式
  media=MediaInfo(MineConstants.voice(),origin_path,dict_json['title'])
  print('media',media.__str__())
  
  media_info_dict={'type':media.type,'title':media.title,'path':media.path}
  
  return media_info_dict
  
  