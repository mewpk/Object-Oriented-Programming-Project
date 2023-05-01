class CourseChapter():
    def __init__(self,progress , name , video):
        self.__progress = progress
        self.__name  = name
        self.__video = video
    @property
    def progress(self):
        return self.__progress
    @property
    def name(self):
        return self.__name
    @property
    def video(self):
        return self.__video
    @progress.setter
    def progress(self,progress):
        self.__progress = progress
        return self.__progress
    @name.setter
    def name(self,name):
        self.__name = name
        return self.__name
    @video.setter
    def video(self,video):
        self.__video = video
        return self.__video


    
