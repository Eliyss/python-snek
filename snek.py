from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor 
import sys, random

class Snek(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

    
class Grid(QFrame):
    snekSpeed
    snekDirection
    gridSize
    gridLength = 11

    def __init__(self):
        super().__init__(parent)
        self.initGrid()
    
    def initGrid(self):
        self.grid = []
        self.timer = QBasicTimer()
        self.resetGrid()
        self.leSnekHasArrived()
        self.ateApple = False
        self.snekHeadX = 5
        self.snekHeadY = 4
        self.appleX = 0
        self.appleY = 0
        self.xVelocity = 0
        self.yVelocity = 0
        self.snekLength = 2
        self.snekTailX = 4
        self.snekTailY = 4
        self.snekTrailX = []
        self.snekTrailY = []

    
    def resetGrid(self):
        for i in range(gridLength):
            self.grid.append(0)
    
    def leSnekHasArrived(self):
        grid[gridLength*gridLength//2] = 1
        leSnek = Snek()
    
    def timerEvent(self, event):
        if event.timerId() = self.timer.timerId():
            self.headX += self.xVelocity
            self.headT += self.yVelocity
            

            if snekHeadX in snekTrail[]

            if self.ateApple:
                self.ateApple = False
                self.spawnApple()
        else:
            super(Grid, self).timerEvent(event)

    def paintEvent(self, event):
        
    
    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.key_Up:
            self.xVelocity = 0
            self.yVelocity = 1
        elif key == Qt.key_Right:
            self.xVelocity = 1
            self.yVelocity = 0
        elif key == Qt.key_Down:
            self.xVelocity = 0
            self.yVelocity = -1
        elif key == Qt.key_Left:
            self.xVelocity = -1
            self.yVelocity = 0
        else:
            super(Board, self).keyPressEvent(event)
    
    def paintEvent(self, event):
    
    def spawnApple(self):



class Snek(object):
    slitherSpeed = 200
    def __init__(self):
        length = 1
        body = []
        body.append([0, 0])
    
    def getLength(self):
        return self.length
    
    def setLength(self, newLength):
        self.Length = newLength
    
    def getBodyLocationX(self, i):
        return self.body[i]

    def setBodyLocation(self, i, newLocation):
        self.body[i] = 

    def grow(self, growth):
        setLength(self, self.getLength+growth)
        self.body.append
