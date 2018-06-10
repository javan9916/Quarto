class Match:
    def __init__(self, matchNumber, gamersName, totalPlays):
        self.__matchNumber = matchNumber
        self.__gamersName = gamersName
        self.__totalPlays = totalPlays


    def setMatchNumber(self, matchNumber):
        self.__matchNumber = matchNumber

    def getMatchNumber(self):
        return self.__matchNumber

    def setGamersName(self, gamersName):
        self.__gamersName = gamersName

    def getGamersName(self):
        return self.__gamersName

    def setTotalPlays(self, totalPlays):
        self.__totalPlays = totalPlays

    def getTotalPlays(self):
        return self.__totalPlays

