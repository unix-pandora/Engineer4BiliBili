import director_info
from Constants import MineConstants

def get_assemble_obj(sort_dictionary):
  min=MineConstants.min()
  med=MineConstants.med()
  max=MineConstants.max()
  
  path_obj = director_info.DirectoryInfo(sort_dictionary[max],sort_dictionary[med],sort_dictionary[min],'','')
  
  print('\n-path_obj: ', path_obj)
  return path_obj