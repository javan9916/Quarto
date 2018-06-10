class Match:
    def __init__(self, matchNumber, gamersName, totalPlays, reason):
        self.__matchNumber = matchNumber
        self.__gamersName = gamersName
        self.__totalPlays = totalPlays
        self.__reason = reason

    def setReason(self, reason):
        self.__reason = reason

    def getReason(self):
        return self.__reason

