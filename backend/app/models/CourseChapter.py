class CourseChapter():
    def __init__(self,progress , name , video):
        self.__progress = progress
        self.__name  = name
        self.__video = video
    @property
    def progress(self):
        return self.__progress


    
