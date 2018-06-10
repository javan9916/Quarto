from Match import *
class Stat:
    def __init__(self):
        self.__matchStats = "matchStats.txt"

    def writeMatch(self, matchList):
            file = open(self.__matchStats,"a")
            info = ""

            for match in matchList:
                i=1
                while i < len(match.getGamersName()):
                    name1 = match.getGamersName()[0]
                    name2 = match.getGamersName()[1]
                    i+=1
                i=1
                while i < len(match.getTotalPlays()):
                    play1 = match.getTotalPlays()[0]
                    play2 = match.getTotalPlays()[1]
                    i+=1

                info += str(match.getMatchNumber())+"$"+name1+","+name2+"$"+str(play1)+","+str(play2)

            file.write(info)
            file.close()


    def readMatchs(self, matchList):
        try:
            file = open(self.__matchStats, "r")

            for linea in file.readlines():
                matchNumber, gamerNames, totalPlays = linea.split("$")
                match = Match(matchNumber,[gamerNames],[totalPlays])
                matchList.append(match)

            file.close()

        except:
            print("Archivo no disponible")