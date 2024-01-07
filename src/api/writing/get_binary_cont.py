# 读取二进制文件的前32个字节内容
def get_bin_content(file_path):  
    with open(file_path, 'rb') as file:  
        content = file.read(32)  
        
        print('\n-type read_bin_content: ', type(content))
        print('\n-read_binary_content: ', content)
        return content