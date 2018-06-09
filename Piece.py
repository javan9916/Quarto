import pygame

class Piece:
    def __init__(self, name, position_x, position_y, image, morph, shape, color, size, used, selected):
        self.__name = name
        self.__position_x = position_x
        self.__position_y = position_y
        self.__image = pygame.image.load(image)
        self.__morph = morph
        self.__shape = shape
        self.__color = color
        self.__size = size
        self.__used = used
        self.__selected = selected

    def getName(self):
        return self.__name

    def getPositionX(self):
        return self.__position_x

    def setPositionX(self,position_x):
        self.__position_x = position_x

    def getPositionY(self):
        return self.__position_y

    def setPositionY(self, position_y):
        self.__position_y = position_y

    def getImage(self):
        return self.__image

    def getMorph(self):
        return self.__morph

    def setMorph(self, morph):
        self.__morph = morph

    def getShape(self):
        return self.__shape

    def setShape(self, shape):
        self.__shape = shape

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

    def getUsed(self):
        return self.__used

    def setUsed(self, used):
        self.__used = used

    def getSelected(self):
        return self.__selected

    def setSelected(self, selected):
        self.__selected = selected

    def movePiece(self,x,y):
        self.setPositionX(x)
        self.setPositionY(y)