import pygame,sys
from Piece import *
from pygame import *
from Position import *

global seconds
seconds = 0
pieceList=[]
positionList=[]
win = False

def main(usr1,usr2):
    pygame.init()
    root = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Quarto")
    rectangulo = pygame.Rect(0, 0, 230, 800)
    mouse = pygame.Rect(0,0,0,0)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 30)
    user1 = font.render(usr1.getName()+": "+str(usr1.getScore()), 1, (255, 255, 255))
    user2 = font.render(usr2.getName()+": "+str(usr2.getScore()), 1, (255, 255, 255))
    turn = False
    usr = usr1

    global flag
    flag = False
    selected = 0
    global win
    win = False

    #positions
    p1 = Piece("p1",30,20,"images/big_nonvoided_blue_circle.png","nonvoid","circle","blue","big",False,False)
    pieceList.append(p1)
    p2 = Piece("p2",140,30,"images/small_nonvoided_blue_circle.png","nonvoid","circle","blue","small",False,False)
    pieceList.append(p2)
    p3 = Piece("p3",130,90,"images/big_nonvoided_blue_square.png","nonvoid","square","blue","big",False,False)
    pieceList.append(p3)
    p4 = Piece("p4",40,100,"images/small_nonvoided_blue_square.png","nonvoid","square","blue","small",False,False)
    pieceList.append(p4)
    p5 = Piece("p5",30,160,"images/big_voided_blue_circle.png","void","circle","blue","big",False,False)
    pieceList.append(p5)
    p6 = Piece("p6",140,170,"images/small_voided_blue_circle.png","void","circle","blue","small",False,False)
    pieceList.append(p6)
    p7 = Piece("p7",130,230,"images/big_voided_blue_square.png","void","square","blue","big",False,False)
    pieceList.append(p7)
    p8 = Piece("p8",40,240,"images/small_voided_blue_square.png","void","square","blue","small",False,False)
    pieceList.append(p8)
    p9 = Piece("p9",30,300,"images/big_nonvoided_red_circle.png","nonvoid","circle","red","big",False,False)
    pieceList.append(p9)
    p10 = Piece("p10",140,310,"images/small_nonvoided_red_circle.png","nonvoid","circle","red","small",False,False)
    pieceList.append(p10)
    p11 = Piece("p11",130,370,"images/big_nonvoided_red_square.png","nonvoid","square","red","big",False,False)
    pieceList.append(p11)
    p12 = Piece("p12",40,380,"images/small_nonvoided_red_square.png","nonvoid","square","red","small",False,False)
    pieceList.append(p12)
    p13 = Piece("p13",30,440,"images/big_voided_red_circle.png","void","circle","red","big",False,False)
    pieceList.append(p13)
    p14 = Piece("p14",140,450,"images/small_voided_red_circle.png","void","circle","red","small",False,False)
    pieceList.append(p14)
    p15 = Piece("p15",130,510,"images/big_voided_red_square.png","void","square","red","big",False,False)
    pieceList.append(p15)
    p16 = Piece("p16",40,520,"images/small_voided_red_square.png","void","square","red","small",False,False)
    pieceList.append(p16)

    table = pygame.image.load("images/table.png")

    pygame.draw.rect(root, (255, 255, 255), rectangulo)

    piece1 = pygame.draw.rect(root, (255, 255, 255), (30,20,60,60))
    piece2 = pygame.draw.rect(root, (255, 255, 255), (140,30,40,40))
    piece3 = pygame.draw.rect(root, (255, 255, 255), (130,90,60,60))
    piece4 = pygame.draw.rect(root, (255, 255, 255), (40,100,40,40))
    piece5 = pygame.draw.rect(root, (255, 255, 255), (30,160,60,60))
    piece6 = pygame.draw.rect(root, (255, 255, 255), (140,170,40,40))
    piece7 = pygame.draw.rect(root, (255, 255, 255), (130,230,60,60))
    piece8 = pygame.draw.rect(root, (255, 255, 255), (40,240,40,40))
    piece9 = pygame.draw.rect(root, (255, 255, 255), (30,300,60,60))
    piece10 = pygame.draw.rect(root, (255, 255, 255), (140,310,40,40))
    piece11 = pygame.draw.rect(root, (255, 255, 255), (130,370,60,60))
    piece12 = pygame.draw.rect(root, (255, 255, 255), (40,380,40,40))
    piece13 = pygame.draw.rect(root, (255, 255, 255), (30,440,60,60))
    piece14 = pygame.draw.rect(root, (255, 255, 255), (140,450,40,40))
    piece15 = pygame.draw.rect(root, (255, 255, 255), (130,510,60,60))
    piece16 = pygame.draw.rect(root, (255, 255, 255), (40,520,40,40))

    i0j0 = Position("i0j0",(407, 37, 70, 70),False,root,(255,255,255),0)
    i0j0.setRect()
    positionList.append(i0j0)
    i0j1 = Position("i0j1",(483, 37, 70, 70),False,root,(255,255,255),0)
    i0j1.setRect()
    positionList.append(i0j1)
    i0j2 = Position("i0j2", (568, 37, 70, 70), False, root, (255, 255, 255),0)
    i0j2.setRect()
    positionList.append(i0j2)
    i0j3 = Position("i0j3", (654, 37, 70, 70), False, root, (255, 255, 255),0)
    i0j3.setRect()
    positionList.append(i0j3)
    i1j0 = Position("i1j0", (407, 114, 70, 70), False, root, (255, 255, 255),0)
    i1j0.setRect()
    positionList.append(i1j0)
    i1j1 = Position("i1j1", (483, 114, 70, 70), False, root, (255, 255, 255),0)
    i1j1.setRect()
    positionList.append(i1j1)
    i1j2 = Position("i1j2", (568, 114, 70, 70), False, root, (255, 255, 255),0)
    i1j2.setRect()
    positionList.append(i1j2)
    i1j3 = Position("i1j3", (654, 114, 70, 70), False, root, (255, 255, 255),0)
    i1j3.setRect()
    positionList.append(i1j3)
    i2j0 = Position("i2j0", (407, 195, 70, 70), False, root, (255, 255, 255),0)
    i2j0.setRect()
    positionList.append(i2j0)
    i2j1 = Position("i2j1", (483, 195, 70, 70), False, root, (255, 255, 255),0)
    i2j1.setRect()
    positionList.append(i2j1)
    i2j2 = Position("i2j2", (568, 195, 70, 70), False, root, (255, 255, 255),0)
    i2j2.setRect()
    positionList.append(i2j2)
    i2j3 = Position("i2j3", (654, 195, 70, 70), False, root, (255, 255, 255),0)
    i2j3.setRect()
    positionList.append(i2j3)
    i3j0 = Position("i3j0", (407, 279, 70, 70), False, root, (255, 255, 255),0)
    i3j0.setRect()
    positionList.append(i3j0)
    i3j1 = Position("i3j1", (483, 279, 70, 70), False, root, (255, 255, 255),0)
    i3j1.setRect()
    positionList.append(i3j1)
    i3j2 = Position("i3j2", (568, 279, 70, 70), False, root, (255, 255, 255),0)
    i3j2.setRect()
    positionList.append(i3j2)
    i3j3 = Position("i3j3", (654, 279, 70, 70), False, root, (255, 255, 255),0)
    i3j3.setRect()
    positionList.append(i3j3)

    matrix = [i0j0, i0j1, i0j2, i0j3], \
            [i1j0, i1j1, i1j2, i1j3], \
            [i2j0, i2j1, i2j2, i2j3], \
            [i3j0, i3j1, i3j2, i3j3]

    def setWin():
        # void/nonvoid
        # i
        if matrix[0][0].getPiece() != 0 and matrix[0][1].getPiece() != 0 and matrix[0][2].getPiece() != 0 and matrix[0][3].getPiece() != 0:
            if matrix[0][0].getPiece().getMorph() == "void" and matrix[0][1].getPiece().getMorph() == "void" and \
            matrix[0][2].getPiece().getMorph() == "void" and matrix[0][3].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[0][0].getPiece().getMorph() == "nonvoid" and matrix[0][1].getPiece().getMorph() == "nonvoid" and \
            matrix[0][2].getPiece().getMorph() == "nonvoid" and matrix[0][3].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        if matrix[1][0].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[1][3].getPiece() != 0:
            if matrix[1][0].getPiece().getMorph() == "void" and matrix[1][1].getPiece().getMorph() == "void" and \
            matrix[1][2].getPiece().getMorph() == "void" and matrix[1][3].getPiece().getMorphv == "void" and win == False:
                return True
            elif matrix[1][0].getPiece().getMorph() == "nonvoid" and matrix[1][1].getPiece().getMorph() == "nonvoid" and \
            matrix[1][2].getPiece().getMorph == "nonvoid" and matrix[1][3].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        if matrix[2][0].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[2][3].getPiece() != 0:
            if matrix[2][0].getPiece().getMorph() == "void" and matrix[2][1].getPiece().getMorph() == "void" and \
            matrix[2][2].getPiece().getMorph() == "void" and matrix[2][3].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[2][0].getPiece().getMorph() == "nonvoid" and matrix[2][1].getPiece().getMorph() == "nonvoid" and \
            matrix[2][2].getPiece().getMorph() == "nonvoid" and matrix[2][3].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        if matrix[3][0].getPiece() != 0 and matrix[3][1].getPiece() != 0 and matrix[3][2].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[3][0].getPiece().getMorph() == "void" and matrix[3][1].getPiece().getMorph() == "void" and \
            matrix[3][2].getPiece().getMorph() == "void" and matrix[3][3].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[3][0].getPiece().getMorph() == "nonvoid" and matrix[3][1].getPiece().getMorph() == "nonvoid" and \
            matrix[3][2].getPiece().getMorph() == "nonvoid" and matrix[3][3].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        # j
        if matrix[0][0].getPiece() != 0 and matrix[1][0].getPiece() != 0 and matrix[2][0].getPiece() != 0 and matrix[3][0].getPiece() != 0:
            if matrix[0][0].getPiece().getMorph() == "void" and matrix[1][0].getPiece().getMorph() == "void" and \
            matrix[2][0].getPiece().getMorph() == "void" and matrix[3][0].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[0][0].getPiece().getMorph() == "nonvoid" and matrix[1][0].getPiece().getMorph() == "nonvoid" and \
            matrix[2][0].getPiece().getMorph() == "nonvoid" and matrix[3][0].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        if matrix[0][1].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[3][1].getPiece() != 0:
            if matrix[0][1].getPiece().getMorph() == "void" and matrix[1][1].getPiece().getMorph() == "void" and \
            matrix[2][1].getPiece().getMorph() == "void" and matrix[3][1].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[0][1].getPiece().getMorph() == "nonvoid" and matrix[1][1].getPiece().getMorph() == "nonvoid" and \
            matrix[2][1].getPiece().getMorph() == "nonvoid" and matrix[3][1].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        if matrix[0][2].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[3][2].getPiece() != 0:
            if matrix[0][2].getPiece().getMorph() == "void" and matrix[1][2].getPiece().getMorph() == "void" and \
            matrix[2][2].getPiece().getMorph() == "void" and matrix[3][2].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[0][2].getPiece().getMorph() == "nonvoid" and matrix[1][2].getPiece().getMorph() == "nonvoid" and \
            matrix[2][2].getPiece().getMorph() == "nonvoid" and matrix[3][2].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        if matrix[0][3].getPiece() != 0 and matrix[1][3].getPiece() != 0 and matrix[2][3].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[0][3].getPiece().getMorph() == "void" and matrix[1][3].getPiece().getMorph() == "void" and \
            matrix[2][3].getPiece().getMorph() == "void" and matrix[3][3].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[0][3].getPiece().getMorph() == "nonvoid" and matrix[1][3].getPiece().getMorph() == "nonvoid" and \
            matrix[2][3].getPiece().getMorph() == "nonvoid" and matrix[3][3].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        # diagonal
        if matrix[0][0].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[0][0].getPiece().getMorph() == "void" and matrix[1][1].getPiece().getMorph() == "void" and \
            matrix[2][2].getPiece().getMorph() == "void" and matrix[3][3].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[0][0].getPiece().getMorph() == "nonvoid" and matrix[1][1].getPiece().getMorph() == "nonvoid" and \
            matrix[2][2].getPiece().getMorph() == "nonvoid" and matrix[3][3].getPiece().getMorph() == "nonvoid" and win == False:
                return True
        if matrix[0][3].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[3][0].getPiece() != 0:
            if matrix[0][3].getPiece().getMorph() == "void" and matrix[1][2].getPiece().getMorph() == "void" and \
            matrix[2][1].getPiece().getMorph() == "void" and matrix[3][0].getPiece().getMorph() == "void" and win == False:
                return True
            elif matrix[0][3].getPiece().getMorph() == "nonvoid" and matrix[1][2].getPiece().getMorph() == "nonvoid" and \
            matrix[2][1].getPiece().getMorph() == "nonvoid" and matrix[3][0].getPiece().getMorph() == "nonvoid" and win == False:
                return True

        # shape
        # i
        if matrix[0][0].getPiece() != 0 and matrix[0][1].getPiece() != 0 and matrix[0][2].getPiece() != 0 and matrix[0][3].getPiece() != 0:
            if matrix[0][0].getPiece().getShape() == "circle" and matrix[0][1].getPiece().getShape() == "circle" and \
            matrix[0][2].getPiece().getShape() == "circle" and matrix[0][3].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[0][0].getPiece().getShape() == "square" and matrix[0][1].getPiece().getShape() == "square" and \
            matrix[0][2].getPiece().getShape() == "square" and matrix[0][3].getPiece().getShape() == "square" and win == False:
                return True
        if matrix[1][0].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[1][3].getPiece() != 0:
            if matrix[1][0].getPiece().getShape() == "circle" and matrix[1][1].getPiece().getShape() == "circle" and \
            matrix[1][2].getPiece().getShape() == "circle" and matrix[1][3].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[1][0].getPiece().getShape() == "square" and matrix[1][1].getPiece().getShape() == "square" and \
            matrix[1][2].getPiece().getShape() == "square" and matrix[1][3].getPiece().getShape() == "square" and win == False:
                return True
        if matrix[2][0].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[2][3].getPiece() != 0:
            if matrix[2][0].getPiece().getShape() == "circle" and matrix[2][1].getPiece().getShape() == "circle" and \
            matrix[2][2].getPiece().getShape() == "circle" and matrix[2][3].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[2][0].getPiece().getShape() == "square" and matrix[2][1].getPiece().getShape() == "square" and \
            matrix[2][2].getPiece().getShape() == "square" and matrix[2][3].getPiece().getShape() == "square" and win == False:
                return True
        if matrix[3][0].getPiece() != 0 and matrix[3][1].getPiece() != 0 and matrix[3][2].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[3][0].getPiece().getShape() == "circle" and matrix[3][1].getPiece().getShape() == "circle" and \
            matrix[3][2].getPiece().getShape() == "circle" and matrix[3][3].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[3][0].getPiece().getShape() == "square" and matrix[3][1].getPiece().getShape() == "square" and \
            matrix[3][2].getPiece().getShape() == "square" and matrix[3][3].getPiece().getShape() == "square" and win == False:
                return True
        # j
        if matrix[0][0].getPiece() != 0 and matrix[1][0].getPiece() != 0 and matrix[2][0].getPiece() != 0 and matrix[3][0].getPiece() != 0:
            if matrix[0][0].getPiece().getShape() == "circle" and matrix[1][0].getPiece().getShape() == "circle" and \
            matrix[2][0].getPiece().getShape() == "circle" and matrix[3][0].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[0][0].getPiece().getShape() == "square" and matrix[1][0].getPiece().getShape() == "square" and \
            matrix[2][0].getPiece().getShape() == "square" and matrix[3][0].getPiece().getShape() == "square" and win == False:
                return True
        if matrix[0][1].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[3][1].getPiece() != 0:
            if matrix[0][1].getPiece().getShape() == "circle" and matrix[1][1].getPiece().getShape() == "circle" and \
            matrix[2][1].getPiece().getShape() == "circle" and matrix[3][1].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[0][1].getPiece().getShape() == "square" and matrix[1][1].getPiece().getShape() == "square" and \
            matrix[2][1].getPiece().getShape() == "square" and matrix[3][1].getPiece().getShape() == "square" and win == False:
                return True
        if matrix[0][2].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[3][2].getPiece() != 0:
            if matrix[0][2].getPiece().getShape() == "circle" and matrix[1][2].getPiece().getShape() == "circle" and \
            matrix[2][2].getPiece().getShape() == "circle" and matrix[3][2].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[0][2].getPiece().getShape() == "square" and matrix[1][2].getPiece().getShape() == "square" and \
            matrix[2][2].getPiece().getShape() == "square" and matrix[3][2].getPiece().getShape() == "square" and win == False:
                return True
        if matrix[0][3].getPiece() != 0 and matrix[1][3].getPiece() != 0 and matrix[2][3].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[0][3].getPiece().getShape() == "circle" and matrix[1][3].getPiece().getShape() == "circle" and \
            matrix[2][3].getPiece().getShape() == "circle" and matrix[3][3].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[0][3].getPiece().getShape() == "square" and matrix[1][3].getPiece().getShape() == "square" and \
            matrix[2][3].getPiece().getShape() == "square" and matrix[3][3].getPiece().getShape() == "square" and win == False:
                return True
        # diagonal
        if matrix[0][0].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[0][0].getPiece().getShape() == "circle" and matrix[1][1].getPiece().getShape() == "circle" and \
            matrix[2][2].getPiece().getShape() == "circle" and matrix[3][3].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[0][0].getPiece().getShape() == "square" and matrix[1][1].getPiece().getShape() == "square" and \
            matrix[2][2].getPiece().getShape() == "square" and matrix[3][3].getPiece().getShape() == "square" and win == False:
                return True
        if matrix[0][3].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix [3][0].getPiece() != 0:
            if matrix[0][3].getPiece().getShape() == "circle" and matrix[1][2].getPiece().getShape() == "circle" and \
            matrix[2][1].getPiece().getShape() == "circle" and matrix[3][0].getPiece().getShape() == "circle" and win == False:
                return True
            elif matrix[0][3].getPiece().getShape() == "square" and matrix[1][2].getPiece().getShape() == "square" and \
            matrix[2][1].getPiece().getShape() == "square" and matrix[3][0].getPiece().getShape() == "square" and win == False:
                return True

        # color
        # i
        if matrix[0][0].getPiece() != 0 and matrix[0][1].getPiece() != 0 and matrix[0][2].getPiece() != 0 and matrix[0][3].getPiece() != 0:
            if matrix[0][0].getPiece().getColor() == "red" and matrix[0][1].getPiece().getColor() == "red" and \
            matrix[0][2].getPiece().getColor() == "red" and matrix[0][3].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[0][0].getPiece().getColor() == "blue" and matrix[0][1].getPiece().getColor() == "blue" and \
            matrix[0][2].getPiece().getColor() == "blue" and matrix[0][3].getPiece().getColor() == "blue" and win == False:
                return True
        if matrix[1][0].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[1][3].getPiece() != 0:
            if matrix[1][0].getPiece().getColor() == "red" and matrix[1][1].getPiece().getColor() == "red" and \
            matrix[1][2].getPiece().getColor() == "red" and matrix[1][3].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[1][0].getPiece().getColor() == "blue" and matrix[1][1].getPiece().getColor() == "blue" and \
            matrix[1][2].getPiece().getColor() == "blue" and matrix[1][3].getPiece().getColor() == "blue" and win == False:
                return True
        if matrix[2][0].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[2][3].getPiece() != 0:
            if matrix[2][0].getPiece().getColor() == "red" and matrix[2][1].getPiece().getColor() == "red" and \
            matrix[2][2].getPiece().getColor() == "red" and matrix[2][3].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[2][0].getPiece().getColor() == "blue" and matrix[2][1].getPiece().getColor() == "blue" and \
            matrix[2][2].getPiece().getColor() == "blue" and matrix[2][3].getPiece().getColor() == "blue" and win == False:
                return True
        if matrix[3][0].getPiece() != 0 and matrix[3][1].getPiece() != 0 and matrix[3][2].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[3][0].getPiece().getColor() == "red" and matrix[3][1].getPiece().getColor() == "red" and \
            matrix[3][2].getPiece().getColor() == "red" and matrix[3][3].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[3][0].getPiece().getColor() == "blue" and matrix[3][1].getPiece().getColor() == "blue" and \
            matrix[3][2].getPiece().getColor() == "blue" and matrix[3][3].getPiece().getColor() == "blue" and win == False:
                return True
        # j
        if matrix[0][0].getPiece() != 0 and matrix[1][0].getPiece() != 0 and matrix[2][0].getPiece() != 0 and matrix[3][0].getPiece() != 0:
            if matrix[0][0].getPiece().getColor() == "red" and matrix[1][0].getPiece().getColor() == "red" and \
            matrix[2][0].getPiece().getColor() == "red" and matrix[3][0].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[0][0].getPiece().getColor() == "blue" and matrix[1][0].getPiece().getColor() == "blue" and \
            matrix[2][0].getPiece().getColor() == "blue" and matrix[3][0].getPiece().getColor() == "blue" and win == False:
                return True
        if matrix[0][1].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[3][1].getPiece() != 0:
            if matrix[0][1].getPiece().getColor() == "red" and matrix[1][1].getPiece().getColor() == "red" and \
            matrix[2][1].getPiece().getColor() == "red" and matrix[3][1].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[0][1].getPiece().getColor() == "blue" and matrix[1][1].getPiece().getColor() == "blue" and \
            matrix[2][1].getPiece().getColor() == "blue" and matrix[3][1].getPiece().getColor() == "blue" and win == False:
                return True
        if matrix[0][2].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[3][2].getPiece() != 0:
            if matrix[0][2].getPiece().getColor() == "red" and matrix[1][2].getPiece().getColor() == "red" and \
            matrix[2][2].getPiece().getColor() == "red" and matrix[3][2].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[0][2].getPiece().getColor() == "blue" and matrix[1][2].getPiece().getColor() == "blue" and \
            matrix[2][2].getPiece().getColor() == "blue" and matrix[3][2].getPiece().getColor() == "blue" and win == False:
                return True
        if matrix[0][3].getPiece() != 0 and matrix[1][3].getPiece() != 0 and matrix[2][3].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[0][3].getPiece().getColor() == "red" and matrix[1][3].getPiece().getColor() == "red" and \
            matrix[2][3].getPiece().getColor() == "red" and matrix[3][3].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[0][3].getPiece().getColor() == "blue" and matrix[1][3].getPiece().getColor() == "blue" and \
            matrix[2][3].getPiece().getColor() == "blue" and matrix[3][3].getPiece().getColor() == "blue" and win == False:
                return True
        # diagonal
        if matrix[0][0].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[0][0].getPiece().getColor() == "red" and matrix[1][1].getPiece().getColor() == "red" and \
            matrix[2][2].getPiece().getColor() == "red" and matrix[3][3].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[0][0].getPiece().getColor() == "blue" and matrix[1][1].getPiece().getColor() == "blue" and \
            matrix[2][2].getPiece().getColor() == "blue" and matrix[3][3].getPiece().getColor() == "blue" and win == False:
                return True
        if matrix[0][3].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[3][0].getPiece() != 0:
            if matrix[0][3].getPiece().getColor() == "red" and matrix[1][2].getPiece().getColor() == "red" and \
            matrix[2][1].getPiece().getColor() == "red" and matrix[3][0].getPiece().getColor() == "red" and win == False:
                return True
            elif matrix[0][3].getPiece().getColor() == "blue" and matrix[1][2].getPiece().getColor() == "blue" and \
            matrix[2][1].getPiece().getColor() == "blue" and matrix[3][0].getPiece().getColor() == "blue" and win == False:
                return True


        # size
        # i
        if matrix[0][0].getPiece() != 0 and matrix[0][1].getPiece() != 0 and matrix[0][2].getPiece() != 0 and matrix[0][3].getPiece() != 0:
            if matrix[0][0].getPiece().getSize() == "big" and matrix[0][1].getPiece().getSize() == "big" and \
            matrix[0][2].getPiece().getSize() == "big" and matrix[0][3].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[0][0].getPiece().getSize() == "small" and matrix[0][1].getPiece().getSize() == "small" and \
            matrix[0][2].getPiece().getSize() == "small" and matrix[0][3].getPiece().getSize() == "small" and win == False:
                return True
        if matrix[1][0].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[1][3].getPiece() != 0:
            if matrix[1][0].getPiece().getSize() == "big" and matrix[1][1].getPiece().getSize() == "big" and \
            matrix[1][2].getPiece().getSize() == "big" and matrix[1][3].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[1][0].getPiece().getSize() == "small" and matrix[1][1].getPiece().getSize() == "small" and \
            matrix[1][2].getPiece().getSize() == "small" and matrix[1][3].getPiece().getSize() == "small" and win == False:
                return True
        if matrix[2][0].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[2][3].getPiece() != 0:
            if matrix[2][0].getPiece().getSize() == "big" and matrix[2][1].getPiece().getSize() == "big" and \
            matrix[2][2].getPiece().getSize() == "big" and matrix[2][3].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[2][0].getPiece().getSize() == "small" and matrix[2][1].getPiece().getSize() == "small" and \
            matrix[2][2].getPiece().getSize() == "small" and matrix[2][3].getPiece().getSize() == "small" and win == False:
                return True
        if matrix[3][0].getPiece() != 0 and matrix[3][1].getPiece() != 0 and matrix[3][2].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[3][0].getPiece().getSize() == "big" and matrix[3][1].getPiece().getSize() == "big" and \
            matrix[3][2].getPiece().getSize() == "big" and matrix[3][3].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[3][0].getPiece().getSize() == "small" and matrix[3][1].getPiece().getSize() == "small" and \
            matrix[3][2].getPiece().getSize() == "small" and matrix[3][3].getPiece().getSize() == "small" and win == False:
                return True
        # j
        if matrix[0][0].getPiece() != 0 and matrix[1][0].getPiece() != 0 and matrix[2][0].getPiece() != 0 and matrix[3][0].getPiece() != 0:
            if matrix[0][0].getPiece().getSize() == "big" and matrix[1][0].getPiece().getSize() == "big" and \
            matrix[2][0].getPiece().getSize() == "big" and matrix[3][0].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[0][0].getPiece().getSize() == "small" and matrix[1][0].getPiece().getSize() == "small" and \
            matrix[2][0].getPiece().getSize() == "small" and matrix[3][0].getPiece().getSize() == "small" and win == False:
                return True
        if matrix[0][1].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[3][1].getPiece() != 0:
            if matrix[0][1].getPiece().getSize() == "big" and matrix[1][1].getPiece().getSize() == "big" and \
            matrix[2][1].getPiece().getSize() == "big" and matrix[3][1].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[0][1].getPiece().getSize() == "small" and matrix[1][1].getPiece().getSize() == "small" and \
            matrix[2][1].getPiece().getSize() == "small" and matrix[3][1].getPiece().getSize() == "small" and win == False:
                return True
        if matrix[0][2].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[3][2].getPiece() != 0:
            if matrix[0][2].getPiece().getSize() == "big" and matrix[1][2].getPiece().getSize() == "big" and \
            matrix[2][2].getPiece().getSize() == "big" and matrix[3][2].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[0][2].getPiece().getSize() == "small" and matrix[1][2].getPiece().getSize() == "small" and \
            matrix[2][2].getPiece().getSize() == "small" and matrix[3][2].getPiece().getSize() == "small" and win == False:
                return True
        if matrix[0][3].getPiece() != 0 and matrix[1][3].getPiece() != 0 and matrix[2][3].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[0][3].getPiece().getSize() == "big" and matrix[1][3].getPiece().getSize() == "big" and \
            matrix[2][3].getPiece().getSize() == "big" and matrix[3][3].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[0][3].getPiece().getSize() == "small" and matrix[1][3].getPiece().getSize() == "small" and \
            matrix[2][3].getPiece().getSize() == "small" and matrix[3][3].getPiece().getSize() == "small" and win == False:
                return True
        # diagonal
        if matrix[0][0].getPiece() != 0 and matrix[1][1].getPiece() != 0 and matrix[2][2].getPiece() != 0 and matrix[3][3].getPiece() != 0:
            if matrix[0][0].getPiece().getSize() == "big" and matrix[1][1].getPiece().getSize() == "big" and \
            matrix[2][2].getPiece().getSize() == "big" and matrix[3][3].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[0][0].getPiece().getSize() == "small" and matrix[1][1].getPiece().getSize() == "small" and \
            matrix[2][2].getPiece().getSize() == "small" and matrix[3][3].getPiece().getSize() == "small" and win == False:
                return True
        if matrix[0][3].getPiece() != 0 and matrix[1][2].getPiece() != 0 and matrix[2][1].getPiece() != 0 and matrix[3][0].getPiece() != 0:
            if matrix[0][3].getPiece().getSize() == "big" and matrix[1][2].getPiece().getSize() == "big" and \
            matrix[2][1].getPiece().getSize() == "big" and matrix[3][0].getPiece().getSize() == "big" and win == False:
                return True
            elif matrix[0][3].getPiece().getSize() == "small" and matrix[1][2].getPiece().getSize() == "small" and \
            matrix[2][1].getPiece().getSize() == "small" and matrix[3][0].getPiece().getSize() == "small" and win == False:
                return True

    def deactivate():
        i = 0
        while i < len(pieceList):
            if pieceList[i].getSelected() == True:
                pieceList[i].setSelected(False)
            i+=1

    while True:
        mouse.left,mouse.top = pygame.mouse.get_pos()
        if turn == False:
            usr = usr1
        elif turn == True:
            usr = usr2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if mouse.colliderect(piece1):
                    deactivate()
                    p1.setSelected(True)
                    selected = p1
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece2):
                    deactivate()
                    p2.setSelected(True)
                    selected = p2
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece3):
                    deactivate()
                    p3.setSelected(True)
                    selected = p3
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece4):
                    deactivate()
                    p4.setSelected(True)
                    selected = p4
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece5):
                    deactivate()
                    p5.setSelected(True)
                    selected = p5
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece6):
                    deactivate()
                    p6.setSelected(True)
                    selected = p6
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece7):
                    deactivate()
                    p7.setSelected(True)
                    selected = p7
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece8):
                    deactivate()
                    p8.setSelected(True)
                    selected = p8
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece9):
                    deactivate()
                    p9.setSelected(True)
                    selected = p9
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece10):
                    deactivate()
                    p10.setSelected(True)
                    selected = p10
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece11):
                    deactivate()
                    p11.setSelected(True)
                    selected = p11
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece12):
                    deactivate()
                    p12.setSelected(True)
                    selected = p12
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece13):
                    deactivate()
                    p13.setSelected(True)
                    selected = p13
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece14):
                    deactivate()
                    p14.setSelected(True)
                    selected = p14
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece15):
                    deactivate()
                    p15.setSelected(True)
                    selected = p15
                    flag = True
                    print(selected.getName())
                if mouse.colliderect(piece16):
                    deactivate()
                    p16.setSelected(True)
                    selected = p16
                    flag = True
                    print(selected.getName())

                print("(" + str(mx) + ", " + str(my) + ")")
                if mouse.colliderect(i0j0.getRect()) and selected!=0 and selected.getUsed() == False and i0j0.getUsed() == False:
                    selected.setPositionX(440-28)
                    selected.setPositionY(69-28)
                    i0j0.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i0j0.setPiece(pieceList[i])
                            print(i0j0.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i0j1.getRect()) and selected!=0 and selected.getUsed() == False and i0j1.getUsed() == False:

                    selected.setPositionX(521-28)
                    selected.setPositionY(69-28)
                    i0j1.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i0j1.setPiece(pieceList[i])
                            print(i0j1.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i0j2.getRect()) and selected!=0 and selected.getUsed() == False and i0j2.getUsed() == False:
                    selected.setPositionX(607-28)
                    selected.setPositionY(69-28)
                    i0j2.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i0j2.setPiece(pieceList[i])
                            print(i0j2.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i0j3.getRect()) and selected!=0 and selected.getUsed() == False and i0j3.getUsed() == False:
                    selected.setPositionX(694-28)
                    selected.setPositionY(69-28)
                    i0j3.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i0j3.setPiece(pieceList[i])
                            print(i0j3.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i1j0.getRect()) and selected!=0 and selected.getUsed() == False and i1j0.getUsed() == False:
                    selected.setPositionX(440-28)
                    selected.setPositionY(151-28)
                    i1j0.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i1j0.setPiece(pieceList[i])
                            print(i1j0.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i1j1.getRect()) and selected!=0 and selected.getUsed() == False and i1j1.getUsed() == False:
                    selected.setPositionX(521-28)
                    selected.setPositionY(151-28)
                    i1j1.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i1j1.setPiece(pieceList[i])
                            print(i1j1.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i1j2.getRect()) and selected!=0 and selected.getUsed() == False and i1j2.getUsed() == False:
                    selected.setPositionX(607-28)
                    selected.setPositionY(151-28)
                    i1j2.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i1j2.setPiece(pieceList[i])
                            print(i1j2.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i1j3.getRect()) and selected!=0 and selected.getUsed() == False and i1j3.getUsed() == False:
                    selected.setPositionX(694-28)
                    selected.setPositionY(151-28)
                    i1j3.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i1j3.setPiece(pieceList[i])
                            print(i1j3.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i2j0.getRect()) and selected!=0 and selected.getUsed() == False and i2j0.getUsed() == False:
                    selected.setPositionX(440-28)
                    selected.setPositionY(234-28)
                    i2j0.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i2j0.setPiece(pieceList[i])
                            print(i2j0.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i2j1.getRect()) and selected!=0 and selected.getUsed() == False and i2j1.getUsed() == False:
                    selected.setPositionX(521-28)
                    selected.setPositionY(234-28)
                    i2j1.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i2j1.setPiece(pieceList[i])
                            print(i2j1.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i2j2.getRect()) and selected!=0 and selected.getUsed() == False and i2j2.getUsed() == False:
                    selected.setPositionX(607-28)
                    selected.setPositionY(234-28)
                    i2j2.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i2j2.setPiece(pieceList[i])
                            print(i2j2.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i2j3.getRect()) and selected!=0 and selected.getUsed() == False and i2j3.getUsed() == False:
                    selected.setPositionX(694-28)
                    selected.setPositionY(234-28)
                    i2j3.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i2j3.setPiece(pieceList[i])
                            print(i2j3.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i3j0.getRect()) and selected!=0 and selected.getUsed() == False and i3j0.getUsed() == False:
                    selected.setPositionX(440-28)
                    selected.setPositionY(315-28)
                    i3j0.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i3j0.setPiece(pieceList[i])
                            print(i3j0.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i3j1.getRect()) and selected!=0 and selected.getUsed() == False and i3j1.getUsed() == False:
                    selected.setPositionX(521-28)
                    selected.setPositionY(315-28)
                    i3j1.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i3j1.setPiece(pieceList[i])
                            print(i3j1.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i3j2.getRect()) and selected!=0 and selected.getUsed() == False and i3j2.getUsed() == False:
                    selected.setPositionX(607-28)
                    selected.setPositionY(315-28)
                    i3j2.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i3j2.setPiece(pieceList[i])
                            print(i3j2.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")
                if mouse.colliderect(i3j3.getRect()) and selected!=0 and selected.getUsed() == False and i3j3.getUsed() == False:
                    selected.setPositionX(694-28)
                    selected.setPositionY(315-28)
                    i3j3.setUsed(True)
                    for piece in pieceList:
                        if piece.getSelected() == True:
                            piece.setUsed(True)
                    i = 0
                    while i < len(pieceList):
                        if pieceList[i].getName() == selected.getName():
                            i3j3.setPiece(pieceList[i])
                            print(i3j3.getPiece().getName())
                            break
                        i += 1

                    if turn == False:
                        turn = True
                    else:
                        turn = False

                    if setWin() == True:
                        win = True
                        print("ALGUIEN GANÓ!")

        root.blit(table, (400, 30))
        for piece in pieceList:
            root.blit(piece.getImage(), (piece.getPositionX(), piece.getPositionY()))
        root.blit(user1, (407, 380))
        root.blit(user2, (407, 440))
        inning = font.render("Turn: " + usr.getName(), 1, (255, 255, 255))
        root.blit(inning, (407, 510))
        clock.tick(25)
        pygame.display.update()