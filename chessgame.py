import sys, pygame
from pygame.locals import *



pygame.init()

black = 0,0,0
white = 255,255,255

size = width, height = 1500, 1000

screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 100)
reply_font = pygame.font.SysFont(None, 60)
stalemate_font =  pygame.font.SysFont(None, 80)
white_won = font.render('White won!',True,white)
black_won = font.render('Black won!',True,(130,130,130))
white_turn = font.render('White turn',True,white)
black_turn = font.render('Black turn',True,(130,130,130))

stalemate_message = stalemate_font.render('Draw by stalemate',True,white)

replay_message = reply_font.render('Press Enter to replay!',True,white)

darkSquare = pygame.image.load("dark.png")
whiteSquare = pygame.image.load("white.png")

whitepawn = pygame.image.load("whitepawn.png")
whitebishop = pygame.image.load("whitebishop.png")
whiterook = pygame.image.load("whiterook.png")
whiteknight = pygame.image.load("whiteknight.png")
whitequeen = pygame.image.load("whitequeen.png")
whiteking = pygame.image.load("whiteking.png")

darkpawn = pygame.image.load("darkpawn.png")
darkbishop = pygame.image.load("darkbishop.png")
darkrook = pygame.image.load("darkrook.png")
darkknight = pygame.image.load("darkknight.png")
darkqueen = pygame.image.load("darkqueen.png")
darkking = pygame.image.load("darkking.png")


dark_pieces = []
white_pieces = []
last_square = "free"
moving_piece = "free"
playerColor = "white"
game_finished = False

class Piece:
    def __init__(self,square,color,type):
        self.square = square
        # square.piece = self
        self.color = color
        self.type = type

    def piece_moves(self):
        return self.type.piece_moves(self.square,self.color,matrix)

class Square:
    def __init__(self,center,color):
        self.center = center
        self.color = color
        self.piece = "free"
        self.line = 0
        self.collum = 0
        self.visibility = True

class Mouse:
    def __init__(self,mouse_position):
        self.mouse_position = mouse_position
        self.piece = "free"

class Knight:
    points = 3
    name = "knight"
    moves = []

    def piece_moves(self,square,color,matrix):
        self.moves =[]
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum

        line = orig_line + 2
        if line < 8:
            collum = orig_collum+1
            if collum < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])



            collum = orig_collum-1
            if collum > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])

        line = orig_line - 2
        if line > -1:
            collum = orig_collum+1
            if collum < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])


            collum = orig_collum-1
            if collum > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])


        collum = orig_collum + 2
        if collum < 8:
            line = orig_line+1
            if line < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])

            line = orig_line-1
            if line > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])

        collum = orig_collum - 2
        if collum > -1:
            line = orig_line+1
            if line < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])
            line = orig_line-1
            if line > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])
        return self.moves


class Queen:
    points = 9
    name = "queen"
    moves = []


    def piece_moves(self,square,color,matrix):
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum
        for line in range(orig_line+1,8):
            if matrix[line][orig_collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif not(matrix[line][orig_collum].piece.color == color):
                self.moves.append(matrix[line][orig_collum])
                break
            else:
                break
        for line in range(orig_line-1,-1,-1):
            if matrix[line][orig_collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif not(matrix[line][orig_collum].piece.color == color):
                self.moves.append(matrix[line][orig_collum])
                break
            else:
                break
        for collum in range(orig_collum+1,8):
            if matrix[orig_line][collum].piece == "free":
                self.moves.append(matrix[orig_line][collum])
            elif not(matrix[orig_line][collum].piece.color == color):
                self.moves.append(matrix[orig_line][collum])
                break
            else:
                break

        for collum in range(orig_collum-1,-1,-1):
            if matrix[orig_line][collum].piece == "free":
                self.moves.append(matrix[orig_line][collum])
            elif not(matrix[orig_line][collum].piece.color == color):
                self.moves.append(matrix[orig_line][collum])
                break
            else:
                break

        for line,collum in zip(range(orig_line+1,8),range(orig_collum+1,8)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])
                break
            else:
                break

        for line,collum in zip(range(orig_line+1,8),range(orig_collum-1,-1,-1)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])
                break
            else:
                break

        for line,collum in zip(range(orig_line-1,-1,-1),range(orig_collum+1,8)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])
                break
            else:
                break

        for line,collum in zip(range(orig_line-1,-1,-1),range(orig_collum-1,-1,-1)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])
                break
            else:
                break
        return self.moves


class Pawn:
    points = 1
    name = "pawn"
    first_move = True
    moves = []

    def piece_moves(self,square,color,matrix):
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum

        if orig_line == 7 or orig_line == 0:
            return self.moves

        if self.first_move:
            if color == "white":
                for line in range(orig_line-1,orig_line-3,-1):
                    if (orig_collum-1 > -1):
                        if not (matrix[line][orig_collum-1].piece == "free"):
                            if not(matrix[line][orig_collum-1].piece.color == color):
                                self.moves.append(matrix[line][orig_collum-1])
                    if (orig_collum+1 < 8):
                        if not (matrix[line][orig_collum+1].piece == "free"):
                            if not(matrix[line][orig_collum+1].piece.color == color):
                                self.moves.append(matrix[line][orig_collum+1])


                    if not(matrix[line][orig_collum].piece == "free"):
                        break
                    self.moves.append(matrix[line][orig_collum])
            else:
                for line in range(orig_line+1,orig_line+3,):
                    if (orig_collum-1 > -1):
                        if not (matrix[line][orig_collum-1].piece == "free"):
                            if not(matrix[line][orig_collum-1].piece.color == color):
                                self.moves.append(matrix[line][orig_collum-1])
                    if (orig_collum+1 < 8):
                        if not (matrix[line][orig_collum+1].piece == "free"):
                            if not(matrix[line][orig_collum+1].piece.color == color):
                                self.moves.append(matrix[line][orig_collum+1])


                    if not(matrix[line][orig_collum].piece == "free"):
                        break
                    self.moves.append(matrix[line][orig_collum])
        else:
            if color == "white":
                for line in range(orig_line-1,orig_line-2,-1):
                    if (orig_collum-1 > -1):
                        if (orig_collum-1 > -1):
                            if not (matrix[line][orig_collum-1].piece == "free"):
                                if not(matrix[line][orig_collum-1].piece.color == color):
                                    self.moves.append(matrix[line][orig_collum-1])
                        if (orig_collum+1 < 8):
                            if not (matrix[line][orig_collum+1].piece == "free"):
                                if not(matrix[line][orig_collum+1].piece.color == color):
                                    self.moves.append(matrix[line][orig_collum+1])

                    if not(matrix[line][orig_collum].piece == "free"):
                        break
                    self.moves.append(matrix[line][orig_collum])
            else:
                for line in range(orig_line+1,orig_line+2):
                    if (orig_collum-1 > -1):
                        if not (matrix[line][orig_collum-1].piece == "free"):
                            if not(matrix[line][orig_collum-1].piece.color == color):
                                self.moves.append(matrix[line][orig_collum-1])
                    if (orig_collum+1 < 8):
                        if not (matrix[line][orig_collum+1].piece == "free"):
                            if not(matrix[line][orig_collum+1].piece.color == color):
                                self.moves.append(matrix[line][orig_collum+1])

                    if not(matrix[line][orig_collum].piece == "free"):
                        break
                    self.moves.append(matrix[line][orig_collum])

        return self.moves

class Bishop:
    points = 3
    name = "bishop"
    moves = []

    def piece_moves(self,square,color,matrix):
        self.moves =[]
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum

        for line,collum in zip(range(orig_line+1,8),range(orig_collum+1,8)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])
                break
            else:
                break

        for line,collum in zip(range(orig_line+1,8),range(orig_collum-1,-1,-1)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])
                break
            else:
                break

        for line,collum in zip(range(orig_line-1,-1,-1),range(orig_collum+1,8)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])
                break
            else:
                break

        for line,collum in zip(range(orig_line-1,-1,-1),range(orig_collum-1,-1,-1)):
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])
                break
            else:
                break
        return self.moves

class King:
    points = "kekw"
    name = "king"
    moved = False
    shortcastle = False
    longcastle = False
    moves = []

    def piece_moves(self,square,color,matrix):
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum

        if not(self.moved):
            self.shortcastle = check_shortcastle(square,color,matrix)
            self.longcastle = check_longcastle(square,color,matrix)
        else:
            self.longcastle = False
            self.shortcastle = False

        line = orig_line
        collum = orig_collum +1
        if collum < 8:
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])

        collum = orig_collum -1
        if collum > -1:
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])


        line = orig_line +1
        if line < 8:
            collum = orig_collum
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])

            collum = orig_collum +1
            if collum < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])

            collum = orig_collum -1
            if collum > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])

        line = orig_line -1
        if line > -1:
            collum = orig_collum
            if matrix[line][collum].piece == "free":
                self.moves.append(matrix[line][collum])
            elif not(matrix[line][collum].piece.color == color):
                self.moves.append(matrix[line][collum])

            collum = orig_collum +1
            if collum < 8:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])

            collum = orig_collum -1
            if collum > -1:
                if matrix[line][collum].piece == "free":
                    self.moves.append(matrix[line][collum])
                elif not(matrix[line][collum].piece.color == color):
                    self.moves.append(matrix[line][collum])




        return self.moves


class Rook:
    points = 5
    name = "rook"
    moved = False
    moves = []

    def piece_moves(self,square,color,matrix):   #square is where the piece is currently at
        self.moves = []
        orig_line = square.line
        orig_collum = square.collum
        for line in range(orig_line+1,8):
            if matrix[line][orig_collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif not(matrix[line][orig_collum].piece.color == color):
                self.moves.append(matrix[line][orig_collum])
                break
            else:
                break
        for line in range(orig_line-1,-1,-1):
            if matrix[line][orig_collum].piece == "free":
                self.moves.append(matrix[line][orig_collum])
            elif not(matrix[line][orig_collum].piece.color == color):
                self.moves.append(matrix[line][orig_collum])
                break
            else:
                break
        for collum in range(orig_collum+1,8):
            if matrix[orig_line][collum].piece == "free":
                self.moves.append(matrix[orig_line][collum])
            elif not(matrix[orig_line][collum].piece.color == color):
                self.moves.append(matrix[orig_line][collum])
                break
            else:
                break
        for collum in range(orig_collum-1,-1,-1):
            if matrix[orig_line][collum].piece == "free":
                self.moves.append(matrix[orig_line][collum])
            elif not(matrix[orig_line][collum].piece.color == color):
                self.moves.append(matrix[orig_line][orig_collum])
                break
            else:
                break
        return self.moves

matrix = [[Square((100,100),"white"),Square((200,100),"dark"),Square((300,100),"white"),Square((400,100),"dark")
        ,Square((500,100),"white"),Square((600,100),"dark"),Square((700,100),"white"),Square((800,100),"dark")]

        ,[Square((100,200),"dark"),Square((200,200),"white"),Square((300,200),"dark"),Square((400,200),"white")
        ,Square((500,200),"dark"),Square((600,200),"white"),Square((700,200),"dark"),Square((800,200),"white")]

        ,[Square((100,300),"white"),Square((200,300),"dark"),Square((300,300),"white"),Square((400,300),"dark")
        ,Square((500,300),"white"),Square((600,300),"dark"),Square((700,300),"white"),Square((800,300),"dark")]

        ,[Square((100,400),"dark"),Square((200,400),"white"),Square((300,400),"dark"),Square((400,400),"white")
        ,Square((500,400),"dark"),Square((600,400),"white"),Square((700,400),"dark"),Square((800,400),"white")]

        ,[Square((100,500),"white"),Square((200,500),"dark"),Square((300,500),"white"),Square((400,500),"dark")
        ,Square((500,500),"white"),Square((600,500),"dark"),Square((700,500),"white"),Square((800,500),"dark")]

        ,[Square((100,600),"dark"),Square((200,600),"white"),Square((300,600),"dark"),Square((400,600),"white")
        ,Square((500,600),"dark"),Square((600,600),"white"),Square((700,600),"dark"),Square((800,600),"white")]

        ,[Square((100,700),"white"),Square((200,700),"dark"),Square((300,700),"white"),Square((400,700),"dark")
        ,Square((500,700),"white"),Square((600,700),"dark"),Square((700,700),"white"),Square((800,700),"dark")]

        ,[Square((100,800),"dark"),Square((200,800),"white"),Square((300,800),"dark"),Square((400,800),"white")
        ,Square((500,800),"dark"),Square((600,800),"white"),Square((700,800),"dark"),Square((800,800),"white")]
        ]

def check_shortcastle(square,color,matrix):
    global white_pieces
    global dark_pieces

    if color == "white":
        if not(white_king.type.moved):
            if not(matrix[7][7].piece == "free") and matrix[7][7].piece.type.name == "rook" and not(matrix[7][7].piece.type.moved):
                print(matrix[7][7].piece.type.moved)
                for piece in dark_pieces:
                    for collum in range(white_king.square.collum,8):
                        if not(piece.type.name == "king") and legal_move(matrix[7][collum],piece.piece_moves()):
                            return False
                    for collum in range(dark_king.square.collum+1,7):
                        if not(matrix[7][collum].piece == "free"):
                            return False
            else:
                return False
            return True
        return False

    else:
        if not(dark_king.type.moved):
            if not(matrix[0][7].piece == "free") and matrix[0][7].piece.type.name == "rook" and not(matrix[0][7].piece.type.moved):
                for piece in white_pieces:
                    for collum in range(dark_king.square.collum,8):
                        if not(piece.type.name == "king") and legal_move(matrix[0][collum],piece.piece_moves()):
                            return False
                    for collum in range(dark_king.square.collum+1,7):
                        if not(matrix[0][collum].piece == "free"):
                            return False
            else:
                return False
            return True
        return False

def check_longcastle(square,color,matrix):
    global white_pieces
    global dark_pieces

    if color == "white":
        if not(white_king.type.moved):
            if not(matrix[7][7].piece == "free") and matrix[7][0].piece.type.name == "rook" and not(matrix[7][0].piece.type.moved):
                for piece in dark_pieces:
                    for collum in range(white_king.square.collum,-1,-1):
                        if not(piece.type.name == "king") and legal_move(matrix[7][collum],piece.piece_moves()):
                            return False
                    for collum in range(white_king.square.collum-1,0,-1):
                        if not(matrix[7][collum].piece == "free"):
                            # print("NOT ENOUF MANAAAA")
                            return False
            else:
                return False
            return True
        return False

    else:
        if not(dark_king.type.moved):
            if not(matrix[0][7].piece == "free") and matrix[0][0].piece.type.name == "rook" and not(matrix[0][0].piece.type.moved):
                for piece in white_pieces:
                    for collum in range(dark_king.square.collum,-1,-1):
                        if not(piece.type.name == "king") and legal_move(matrix[0][collum],piece.piece_moves()):
                            return False
                    for collum in range(dark_king.square.collum-1,0,-1):
                        if not(matrix[0][collum].piece == "free"):
                            return False
            else:
                return False
            return True
        return False



dark_king, white_king = "",""

def init_pieces():
    global matrix
    global dark_king
    global white_king
    global white_pieces
    global dark_pieces

    white_pieces = []
    dark_pieces = []

    matrix = [[Square((100,100),"white"),Square((200,100),"dark"),Square((300,100),"white"),Square((400,100),"dark")
            ,Square((500,100),"white"),Square((600,100),"dark"),Square((700,100),"white"),Square((800,100),"dark")]

            ,[Square((100,200),"dark"),Square((200,200),"white"),Square((300,200),"dark"),Square((400,200),"white")
            ,Square((500,200),"dark"),Square((600,200),"white"),Square((700,200),"dark"),Square((800,200),"white")]

            ,[Square((100,300),"white"),Square((200,300),"dark"),Square((300,300),"white"),Square((400,300),"dark")
            ,Square((500,300),"white"),Square((600,300),"dark"),Square((700,300),"white"),Square((800,300),"dark")]

            ,[Square((100,400),"dark"),Square((200,400),"white"),Square((300,400),"dark"),Square((400,400),"white")
            ,Square((500,400),"dark"),Square((600,400),"white"),Square((700,400),"dark"),Square((800,400),"white")]

            ,[Square((100,500),"white"),Square((200,500),"dark"),Square((300,500),"white"),Square((400,500),"dark")
            ,Square((500,500),"white"),Square((600,500),"dark"),Square((700,500),"white"),Square((800,500),"dark")]

            ,[Square((100,600),"dark"),Square((200,600),"white"),Square((300,600),"dark"),Square((400,600),"white")
            ,Square((500,600),"dark"),Square((600,600),"white"),Square((700,600),"dark"),Square((800,600),"white")]

            ,[Square((100,700),"white"),Square((200,700),"dark"),Square((300,700),"white"),Square((400,700),"dark")
            ,Square((500,700),"white"),Square((600,700),"dark"),Square((700,700),"white"),Square((800,700),"dark")]

            ,[Square((100,800),"dark"),Square((200,800),"white"),Square((300,800),"dark"),Square((400,800),"white")
            ,Square((500,800),"dark"),Square((600,800),"white"),Square((700,800),"dark"),Square((800,800),"white")]
            ]

    for line in range(0,8):
        for collum in range(0,8):
            if(line == 1):
                matrix[line][collum].piece = Piece(matrix[line][collum],"dark",Pawn())
                dark_pieces.append(matrix[line][collum].piece)
            elif(line == 6):
                matrix[line][collum].piece = Piece(matrix[line][collum],"white",Pawn())
                white_pieces.append(matrix[line][collum].piece)
            elif(line == 0):
                if(collum == 0):
                    matrix[line][collum].piece = Piece(matrix[line][collum],"dark",Rook())
                    dark_pieces.append(matrix[line][collum].piece)
                elif collum == 1:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"dark",Knight())
                    dark_pieces.append(matrix[line][collum].piece)
                elif collum == 2:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"dark",Bishop())
                    dark_pieces.append(matrix[line][collum].piece)
                elif collum == 3:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"dark",Queen())
                    dark_pieces.append(matrix[line][collum].piece)
                elif collum == 4:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"dark",King())
                    dark_king = matrix[line][collum].piece
                    dark_pieces.append(matrix[line][collum].piece)
                elif collum == 5:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"dark",Bishop())
                    dark_pieces.append(matrix[line][collum].piece)
                elif collum == 6:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"dark",Knight())
                    dark_pieces.append(matrix[line][collum].piece)
                elif collum == 7:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"dark",Rook())
                    dark_pieces.append(matrix[line][collum].piece)

            elif(line == 7):
                if(collum == 0):
                    matrix[line][collum].piece = Piece(matrix[line][collum],"white",Rook())
                    white_pieces.append(matrix[line][collum].piece)
                elif collum == 1:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"white",Knight())
                    white_pieces.append(matrix[line][collum].piece)
                elif collum == 2:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"white",Bishop())
                    white_pieces.append(matrix[line][collum].piece)
                elif collum == 3:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"white",Queen())
                    white_pieces.append(matrix[line][collum].piece)
                elif collum == 4:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"white",King())
                    white_king = matrix[line][collum].piece
                    white_pieces.append(matrix[line][collum].piece)
                elif collum == 5:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"white",Bishop())
                    white_pieces.append(matrix[line][collum].piece)
                elif collum == 6:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"white",Knight())
                    white_pieces.append(matrix[line][collum].piece)
                elif collum == 7:
                    matrix[line][collum].piece = Piece(matrix[line][collum],"white",Rook())
                    white_pieces.append(matrix[line][collum].piece)

            matrix[line][collum].line = line
            matrix[line][collum].collum = collum


def showpiece(piece,center):
    name = piece.type.name
    piece_rect = 0
    if piece.color == "white":
        if name == "pawn":
            piece_rect = whitepawn.get_rect(center=center)
            screen.blit(whitepawn,piece_rect)
        elif name == "rook":
            piece_rect = whiterook.get_rect(center=center)
            screen.blit(whiterook,piece_rect)
        elif name == "bishop":
            piece_rect = whitebishop.get_rect(center=center)
            screen.blit(whitebishop,piece_rect)
        elif name == "knight":
            piece_rect = whiteknight.get_rect(center=center)
            screen.blit(whiteknight,piece_rect)
        elif name == "queen":
            piece_rect = whitequeen.get_rect(center=center)
            screen.blit(whitequeen,piece_rect)
        elif name == "king":
            piece_rect = whiteking.get_rect(center=center)
            screen.blit(whiteking,piece_rect)
    elif piece.color == "dark":
        if name == "pawn":
            piece_rect = darkpawn.get_rect(center=center)
            screen.blit(darkpawn,piece_rect)
        elif name == "rook":
            piece_rect = darkrook.get_rect(center=center)
            screen.blit(darkrook,piece_rect)
        elif name == "bishop":
            piece_rect = darkbishop.get_rect(center=center)
            screen.blit(darkbishop,piece_rect)
        elif name == "knight":
            piece_rect = darkknight.get_rect(center=center)
            screen.blit(darkknight,piece_rect)
        elif name == "queen":
            piece_rect = darkqueen.get_rect(center=center)
            screen.blit(darkqueen,piece_rect)
        elif name == "king":
            piece_rect = darkking.get_rect(center=center)
            screen.blit(darkking,piece_rect)

def legal_move(square,legal_sq):
    # count = 0
    # for sq in legal_sq:
    #     print(count,"-",sq.line,sq.collum)
    #     count+=1
    for sq in legal_sq:
        if square == sq:
            return True
    return False

def capture(piece):
    if piece.color == "white":
        white_pieces.remove(piece)
    else:
        dark_pieces.remove(piece)

def promoted_pawn(piece):
    if piece.square.line == 7 or piece.square.line == 0:
        if piece.color == "white":
            piece.square.piece = Piece(piece.square,"white",Queen())
            white_pieces.append(piece.square.piece)
            piece.square = "free"
            white_pieces.remove(piece)
        else:
            piece.square.piece = Piece(piece.square,"dark",Queen())
            dark_pieces.append(piece.square.piece)
            piece.square = "free"
            dark_pieces.remove(piece)

def move_played(mouse,matrix):
    cpt = False
    global moves_count
    global playerColor
    global game_finished
    if playerColor == mouse.piece.color:
        for line in matrix:
            for square in line:
                if whiteSquare.get_rect(center=square.center).collidepoint(mouse.mouse_position):
                    last_position = mouse.piece.square
                    if mouse.piece.type.name =="king":
                        if mouse.piece.type.shortcastle:
                            if mouse.piece.color == "white":
                                for collum in range(5,8):
                                    if square == matrix[7][collum]:
                                        white_king.square.visibility = True
                                        white_king.square.piece = "free"
                                        white_king.square = matrix[7][6]
                                        white_king.square.piece = white_king
                                        white_king.type.moved = True

                                        matrix[7][7].piece.square = matrix[7][5]
                                        matrix[7][5].piece = matrix[7][7].piece
                                        matrix[7][5].piece.type.moved = True
                                        matrix[7][7].piece = "free"
                                        mouse.piece = "free"
                                        move_routine("dark")
                                        playerColor = "dark"
                                        moves_count+=1
                                        return
                            if mouse.piece.color == "dark":
                                for collum in range(5,8):
                                    if square == matrix[0][collum]:
                                        dark_king.square.visibility = True
                                        dark_king.square.piece = "free"
                                        dark_king.square = matrix[0][6]
                                        dark_king.square.piece = dark_king
                                        dark_king.type.moved = True

                                        matrix[0][7].piece.square = matrix[0][5]
                                        matrix[0][5].piece = matrix[0][7].piece
                                        matrix[0][5].piece.type.moved = True
                                        matrix[0][7].piece = "free"
                                        mouse.piece = "free"
                                        move_routine("white")
                                        playerColor = "white"
                                        moves_count+=1
                                        return
                        if mouse.piece.type.longcastle:
                            if mouse.piece.color == "white":
                                for collum in range(2,-1,-1):
                                    if square == matrix[7][collum]:
                                        white_king.square.visibility = True
                                        white_king.square.piece = "free"
                                        white_king.square = matrix[7][2]
                                        white_king.square.piece = white_king
                                        white_king.type.moved = True

                                        matrix[7][0].piece.square = matrix[7][3]
                                        matrix[7][3].piece = matrix[7][0].piece
                                        matrix[7][3].piece.type.moved = True
                                        matrix[7][0].piece = "free"
                                        mouse.piece = "free"
                                        move_routine("dark")
                                        playerColor = "dark"
                                        moves_count+=1
                                        return
                            if mouse.piece.color == "dark":
                                for collum in range(2,-1,-1):
                                    if square == matrix[0][collum]:
                                        dark_king.square.visibility = True
                                        dark_king.square.piece = "free"
                                        dark_king.square = matrix[0][2]
                                        dark_king.square.piece = dark_king
                                        dark_king.type.moved = True

                                        matrix[0][0].piece.square = matrix[0][3]
                                        matrix[0][3].piece = matrix[0][0].piece
                                        matrix[0][3].piece.type.moved = True
                                        matrix[0][0].piece = "free"
                                        mouse.piece = "free"
                                        move_routine("white")
                                        playerColor = "white"
                                        moves_count+=1
                                        return

                    if legal_move(square,mouse.piece.piece_moves()):
                        if not(square.piece == "free"):
                            last_piece = square.piece
                            capture(square.piece)
                            last_piece.square = "free"
                            cpt = True

                        mouse.piece.square.visibility = True
                        mouse.piece.square.piece = "free"
                        mouse.piece.square = square
                        square.piece = mouse.piece
                        mouse.piece = "free"
                        if player_king_incheck(square.piece.color):

                            last_position.piece = square.piece
                            square.piece.square = last_position
                            square.piece = "free"
                            if cpt:
                                if last_piece.color =="white":
                                    white_pieces.append(last_piece)
                                else:
                                    dark_pieces.append(last_piece)
                                square.piece = last_piece
                                last_piece.square = square

                            # print(last_position.piece.type.name," from ",last_position.line,last_position.collum , " denied move to ",square.line,square.collum)
                            return

                        if( square.piece.type.name == "pawn"):
                            square.piece.type.first_move = False
                            promoted_pawn(square.piece)
                        if square.piece.type.name =="king" or square.piece.type.name =="rook":
                            square.piece.type.moved = True

                        if(square.piece.color == "white"):
                            move_routine("dark")

                            playerColor = "dark"
                        else:
                            move_routine("white")

                            playerColor = "white"

                        moves_count+=1
                        # print(square.piece.type.name," from ",last_position.line,last_position.collum , " to ",square.line,square.collum)

                        return
                    else:
                        mouse.piece.square.visibility = True
                        mouse.piece = "free"
                        # print(last_position.piece.type.name," from ",last_position.line,last_position.collum, " denied move to ",square.line,square.collum)
                        return
    else:
        mouse.piece.square.visibility = True
        mouse.piece = "free"

def dark_mated():
    cpt = False
    last_piece = "free"
    for piece in dark_pieces:
        last_position = piece.square
        for square in piece.piece_moves():
            cpt = False
            if not(square.piece == "free"):
                last_piece = square.piece
                last_piece.square = "free"
                cpt = True
                capture(square.piece)

            last_position = piece.square
            last_position.piece = "free"
            piece.square = square
            square.piece = piece

            if not(player_king_incheck(square.piece.color)):

                last_position.piece = square.piece
                square.piece.square = last_position
                square.piece = "free"

                if cpt:
                    white_pieces.append(last_piece)
                    square.piece = last_piece
                    last_piece.square = square
                    last_piece = "free"
                return False

            last_position.piece = square.piece
            square.piece.square = last_position
            square.piece = "free"
            if cpt:
                white_pieces.append(last_piece)
                square.piece = last_piece
                last_piece.square = square
                last_piece = "free"

    return True

def white_mated():
    cpt = False
    last_piece = "free"
    for piece in white_pieces:
        for square in piece.piece_moves():
            cpt = False
            if not(square.piece == "free"):
                last_piece = square.piece
                last_piece.square = "free"
                cpt = True
                capture(square.piece)

            last_position = piece.square
            last_position.piece = "free"
            piece.square = square
            square.piece = piece

            if not(player_king_incheck("white")):
                last_position.piece = square.piece
                square.piece.square = last_position
                square.piece = "free"

                if cpt:
                    dark_pieces.append(last_piece)
                    square.piece = last_piece
                    last_piece.square = square
                    last_piece = "free"
                return False

            last_position.piece = square.piece
            square.piece.square = last_position
            square.piece = "free"
            if cpt:
                dark_pieces.append(last_piece)
                square.piece = last_piece
                last_piece.square = square
                last_piece = "free"

    return True



def move_routine(playerColor):
    global game_finished
    global stalemate
    if(player_king_incheck(playerColor)):
        if playerColor =="white" and white_mated():
            game_finished = True

        elif playerColor =="dark" and dark_mated():
            game_finished = True
        return
    if playerColor =="white" and white_mated():
        stalemate = True

    elif playerColor =="dark" and dark_mated():
        stalemate = True



def player_king_incheck(color):
    if color == "white":
        if len(whiteking_checks()) > 0:
            return True
        else:
            return False
    else:
        if len(darkking_checks()) > 0:
            return True
        else:
            return False

def darkking_checks():
    global white_pieces
    global dark_king
    global matrix
    global dark_checkers
    dark_checkers = []

    for piece in white_pieces:
        if legal_move(dark_king.square,piece.piece_moves()):
            dark_checkers.append(piece)
    return dark_checkers

def whiteking_checks():
    global white_pieces
    global white_king
    global matrix
    global white_checkers

    white_checkers = []

    for piece in dark_pieces:
        if legal_move(white_king.square,piece.piece_moves()):
            white_checkers.append(piece)
    return white_checkers


mouse = Mouse(pygame.mouse.get_pos())
white_checkers =[]
dark_checkers = []
stalemate = False
moves_count = 0


def init_game():
    global playerColor
    global game_finished
    global stalemate

    playerColor = "white"
    game_finished = False
    stalemate = False
    init_pieces()

init_game()

while 1:
    screen.fill(black)
    mouse.mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if(game_finished == False and stalemate == False):
            if event.type == MOUSEBUTTONDOWN:
                for button in pygame.mouse.get_pressed(num_buttons=3):
                    if button == True:
                        for line in matrix:
                            for square in line:
                                if whiteSquare.get_rect(center=square.center).collidepoint(mouse.mouse_position) and not(square.piece=="free"):
                                    moving_piece = mouse.piece
                                    mouse.piece = square.piece
                                    square.visibility = False
            if event.type == MOUSEBUTTONUP:
                if not(mouse.piece == "free"):
                    move_played(mouse,matrix)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    init_game()

        for line in matrix:
            for square in line:
                if square.color == "white":
                    whiteS_rect = whiteSquare.get_rect(center=square.center)
                    screen.blit(whiteSquare, whiteS_rect)
                else:
                    darkS_rect = darkSquare.get_rect(center=square.center)
                    screen.blit(darkSquare, darkS_rect)
                if not(square.piece == "free") and square.visibility == True:
                    showpiece(square.piece,square.center)



        if not(mouse.piece=="free"):
            if mouse.mouse_position[0] < 850 and mouse.mouse_position[0] > 50:
                if mouse.mouse_position[1] > 50 and mouse.mouse_position[1] < 850:
                    showpiece(mouse.piece,mouse.mouse_position)

        if game_finished == True:
            if playerColor == "white":
                screen.blit(black_won,(1000,250))
                screen.blit(replay_message,(950,400))
            else:
                screen.blit(white_won,(950,250))
                screen.blit(replay_message,(950,400))
        elif(stalemate ==True):
            screen.blit(stalemate_message,(950,220))
            screen.blit(replay_message,(950,400))
        else:
            if playerColor == "white":
                screen.blit(white_turn,(1000,250))
            else:
                screen.blit(black_turn,(1000,250))

        pygame.display.flip()
