class MediaInfo:
    def __init__(self, type, path, title):
        self.type = type
        self.path = path
        self.title = title

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return f"Type：{self.type}，Path：{self.path}，Title：{self.title}"
