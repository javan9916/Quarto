from Piece import *
import pygame

class Position:
    def __init__(self,name,position,used,root,color,piece):
        self.__name = name
        self.__position = position
        self.__used = used
        self.__rect = pygame.draw.rect(root,(color),(position))
        self.__color = color
        self.__root = root
        self.__piece = piece

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def setPosition(self,position):
        self.__position = position

    def getUsed(self):
        return self.__used

    def setUsed(self,used):
        self.__used = used

    def setRect(self):
        self.__rect = pygame.draw.rect(self.__root, (self.__color), (self.__position))

    def getRect(self):
        return self.__rect

    def setPiece(self,piece):
        self.__piece = piece

    def getPiece(self):
        return self.__piece


