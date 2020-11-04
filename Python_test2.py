from bangtal import *

scene1 = Scene("테스트용","Images/배경.png")
BOARD_ANIMATION_FRAME = 10

class Block(Object):
    def __init__(self, num, x, y):
        super().__init__("Images/block"+str(num)+".png") 
        self.setScale(4.0)        
        self.locate_on_board(x, y)
        self.show()
    def locate_on_board(self, bx, by):
        self.x = bx
        self.y = by
        tx = int(300 + 96 * bx)
        ty = int(100 + 96 * by)
        self.locate(scene1, tx, ty)
    def moveAnimation(self, direction, frame):        
        #if direction == RIGHT
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        self.x -= 1/BOARD_ANIMATION_FRAME
        if frame == BOARD_ANIMATION_FRAME:
            self.x = round(self.x)
        self.locate_on_board(self.x, self.y)       

blocks = []


for i in range(30):    
    blocks.append(Block(i//5, i%5, i//5))
    if i > 24:
        blocks[i].hide()

class BlockBoard():
    def __init__(self):
        self.board = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        self.spareBoard = [25, 26, 27, 28, 29]
        self.frame = 1

    def locate_spare(self, direction):
        # if direction == RIGHT
        for i in range(5):
            tblock = blocks[self.spareBoard[i]]
            tblock.locate_on_board(5, i)
            tblock.show()

    def update_board(self, direction):
        #if direction == RIGHT
        tempSpare = []
        for i in range(5):
            tempSpare.append(self.board[i][0])
        for i in range(5):
            for j in range(5):
                if i==4:
                    self.board[j][i] = self.spareBoard[j]
                else:
                    self.board[j][i] = self.board[j][i+1]
        for i in range(5):
            self.spareBoard[i] = tempSpare[i]
            blocks[tempSpare[i]].hide()

    def boardAnimation(self, direction):        
        boardTimer.set(0.1)
        boardTimer.start()
        print("HERE")
        for i in range(30):
            blocks[i].moveAnimation(1, self.frame)
        self.frame = self.frame % 10 + 1
        if self.frame == 1:
            boardTimer.stop()
            self.update_board(direction)
            #TODO hide, board update, spareBoard update
            return
        pass

    def move(self,direction):
        self.locate_spare(direction)
        self.boardAnimation(direction)

blockBoard = BlockBoard()

def boardTimeOut():
    blockBoard.boardAnimation(1)    
    pass

def keyBoard(key, pressed):
    if pressed:
        blockBoard.move(1)
        pass

scene1.onKeyboard = keyBoard
boardTimer = Timer(0.1)
boardTimer.onTimeout = boardTimeOut

startGame(scene1)

