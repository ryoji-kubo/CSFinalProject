import random
dis=600/20
buf=100/2
class Student:
    def __init__(self,start=(0,19)):
        self.pos=start
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
    def move(self):
        if self.keyHandler[LEFT]==True and self.pos[0]!=0 and board.board[self.pos[1]][self.pos[0]-1]=="":
            self.pos=(self.pos[0]-1,self.pos[1])
        elif self.keyHandler[RIGHT]==True and self.pos[0]!=19 and board.board[self.pos[1]][self.pos[0]+1]=="":
            self.pos=(self.pos[0]+1,self.pos[1])
        elif self.keyHandler[UP]==True and self.pos[1]!=0 and board.board[self.pos[1]-1][self.pos[0]]=="":
            self.pos=(self.pos[0],self.pos[1]-1)
        elif self.keyHandler[DOWN]==True and self.pos[1]!=19 and board.board[self.pos[1]+1][self.pos[0]]=="":
            self.pos=(self.pos[0],self.pos[1]+1)
    def drawStudent(self):
        x=self.pos[0]
        y=self.pos[1]
        fill(255)
        circle(x*dis+dis/2,y*dis+dis/2+buf,dis)
class Board:
    def __init__(self):
        self.board=[["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","#","","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","#","","","#","","","#","","","#","","","#","","","#","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","#","","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","#","","","#","","","#","","","#","","","#","","","#","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","#","","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","#","","","#","","","#","","","#","","","#","","","#","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","#","","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","#","","","#","","","#","","","#","","","#","","","#","","",""]]
    def printBoard(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]=="#":
                    fill(255)
                    rect(col*dis,row*dis+buf,dis,dis)
                    
class Coffee:
    def __init__(self):
        self.pos=(random.randint(0,19),random.randint(0,19))
        while board.board[self.pos[1]][self.pos[0]]=="#" or self.pos==student.pos or self.pos in stage.coffeePosList:
            self.pos=(random.randint(0,19),random.randint(0,19))
        

class Stage:
    def __init__(self):
        self.coffeeList=[]
        self.coffeePosList=[]
    def spawnCoffee(self):
        self.coffeeList.append(Coffee())
    def update(self):
        for coffee in self.coffeeList:
            self.coffeePosList.append(coffee.pos)

class Point:
    def __init__(self):
        self.score=0
        
class Game:
    def __init__(self):
        self.gameEnd=False
        self.frame=0
    def main(self):
        self.display()
        board.printBoard()
        student.drawStudent()
        student.move()
        game.drinkCoffee()
    def display(self):
        #Setting the timer
        self.frame+=1
        fill(255)
        textSize(30)
        timer=30-self.frame//5
        text("Time Remaining: "+str(timer),4,34)
        
        #Display the point
        fill(0)
        rect(348,4,204,30)
        fill(0,60,255)
        rect(350,6,p.score*2,26)
        
        #Display the coffee cups
        for coffee in stage.coffeeList:
            x=coffee.pos[0]
            y=coffee.pos[1]
            fill(255,0,0)
            circle(x*dis+dis/2,y*dis+dis/2+buf,dis)
    def drinkCoffee(self):
        for coffee in stage.coffeeList:
            if coffee.pos==student.pos:
                stage.coffeeList.remove(coffee)
                p.score+=2
        
student=Student()
game=Game()
board=Board()
p=Point()
stage=Stage()
for i in range(7):
    stage.spawnCoffee()
    stage.update()

def setup():
    size(600,700)
    background(205)

def draw():
    if frameCount%12==0:
        background(205)
        game.main()

def keyPressed():
    if keyCode == LEFT:
        student.keyHandler[LEFT]=True
    elif keyCode == RIGHT:
        student.keyHandler[RIGHT]=True
    elif keyCode == UP:
        student.keyHandler[UP]=True
    elif keyCode==DOWN:
      student.keyHandler[DOWN]=True


def keyReleased():
    if keyCode == LEFT:
        student.keyHandler[LEFT]=False
    elif keyCode == RIGHT:
        student.keyHandler[RIGHT]=False
    elif keyCode == UP:
      student.keyHandler[UP]=False
    elif keyCode == DOWN:
      student.keyHandler[DOWN]=False
