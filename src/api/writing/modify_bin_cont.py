# fix_m4s函数用于修改m4s文件头部信息
# target_path: 输入文件的路径，即需要修改的文件的位置
# output_path: 输出文件的路径，即修改后的文件保存位置
# bufsize: 缓冲区大小，默认为256MB，在读取和写入文件时，一次处理的数据量
# 函数无返回值
def fix_m4s(
    target_path: str, output_path: str, bufsize: int = 256 * 1024 * 1024
) -> None:
    # 打印输入和输出文件的路径，方便调试和记录
    print("\n", "target_path: ", target_path)
    print("\n", "output_path: ", output_path)
    # 使用assert语句检查bufsize是否大于0，如果小于或等于0，则抛出AssertionError异常
    assert bufsize > 0

    # 以二进制模式（'rb'）打开目标文件，即需要修改的文件
    with open(target_path, "rb") as target_file:
        # 读取文件的前32个字节，这是文件头部信息
        header = target_file.read(32)
        # 将头部信息中的'000000000'替换为空字节
        new_header = header.replace(b"000000000", b"")
        # 将头部信息中的'$'替换为空格
        new_header = new_header.replace(b"$", b" ")
        # 将头部信息中的'avc1'替换为空字节
        new_header = new_header.replace(b"avc1", b"")

        # 以二进制模式（'wb'）打开输出文件，即修改后的文件
        with open(output_path, "wb") as OUTPUT_FILE:
            # 将新的头部信息写入输出文件
            OUTPUT_FILE.write(new_header)
            # 初始化一个变量i为target_file读取的字节数据，首次读取时，bufsize大小的字节数据被读取进来
            i = target_file.read(bufsize)
            # 当i不为空时，循环继续，即继续从输入文件读取数据，并将其写入输出文件
            while i:
                # 将i（已读取的字节数据）写入输出文件
                OUTPUT_FILE.write(i)
                # 从输入文件继续读取bufsize大小的字节数据，并将其赋值给i
                i = target_file.read(bufsize)
