class User:
    def __init__(self, name, score, plays):
        self.__name = name
        self.__score = score
        self.__plays = plays

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def getScore(self):
        return self.__score

    def setScore(self, score):
        self.__score = score

    def getPlays(self):
        return self.__plays

    def setPlays(self, plays):
        self.__plays = plays

    def sumScore(self):
        self.__score += 3

    def sumPlays(self):
        self.__plays += 1