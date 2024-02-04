import director_info
from Constants import MineConstants


def get_assemble_obj(sort_dictionary):
    path_obj = director_info.DirectoryInfo(
        sort_dictionary[MineConstants.max()],
        sort_dictionary[MineConstants.med()],
        sort_dictionary[MineConstants.min()],
        "",
        "",
    )

    print("\n", "path_obj: ", path_obj)
    return path_obj
