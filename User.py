class User:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def getScore(self):
        return self.__score
