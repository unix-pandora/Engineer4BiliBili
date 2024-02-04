
class DirectoryInfo:  
    def __init__(self, video_path, audio_path, json_path, new_video_path, new_audio_path):  
        self._video_path = video_path  
        self._audio_path = audio_path  
        self._json_path = json_path  
        self._new_video_path = new_video_path  
        self._new_audio_path = new_audio_path  
  
    @property  
    def video_path(self):  
        return self._video_path  
  
    @video_path.setter  
    def video_path(self, new_video_path):  
        self._video_path = new_video_path  
  
    @property  
    def audio_path(self):  
        return self._audio_path  
  
    @audio_path.setter  
    def audio_path(self, new_audio_path):  
        self._audio_path = new_audio_path  
  
    @property  
    def json_path(self):  
        return self._json_path  
  
    @json_path.setter  
    def json_path(self, new_json_path):  
        self._json_path = new_json_path  
  
    @property  
    def new_video_path(self):  
        return self._new_video_path  
  
    @new_video_path.setter  
    def new_video_path(self, new_new_video_path):  
        self._new_video_path = new_new_video_path  
  
    @property  
    def new_audio_path(self):  
        return self._new_audio_path  
  
    @new_audio_path.setter  
    def new_audio_path(self, new_new_audio_path):  
        self._new_audio_path = new_new_audio_path

    def __str__(self):  
        return f"Video Path: {self.video_path}, Audio Path: {self.audio_path}, JSON Path: {self.json_path}, New Video Path: {self.new_video_path}, New Audio Path: {self.new_audio_path}"        