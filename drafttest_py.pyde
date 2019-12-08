import random
dis=600/20
buf=100/2
class Student:
    def __init__(self,start):
        self.pos=start
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
    def move(self):
        if self.keyHandler[LEFT]==True and self.pos[0]!=0 and board.current[self.pos[1]][self.pos[0]-1]!="#":
            self.pos=(self.pos[0]-1,self.pos[1])
        elif self.keyHandler[RIGHT]==True and self.pos[0]!=19 and board.current[self.pos[1]][self.pos[0]+1]!="#":
            self.pos=(self.pos[0]+1,self.pos[1])
        elif self.keyHandler[UP]==True and self.pos[1]!=0 and board.current[self.pos[1]-1][self.pos[0]]!="#":
            self.pos=(self.pos[0],self.pos[1]-1)
        elif self.keyHandler[DOWN]==True and self.pos[1]!=19 and board.current[self.pos[1]+1][self.pos[0]]!="#":
            self.pos=(self.pos[0],self.pos[1]+1)
    def drawStudent(self):
        x=self.pos[0]
        y=self.pos[1]
        fill(255)
        circle(x*dis+dis/2,y*dis+dis/2+buf,dis)
class Board:
    def __init__(self):
        self.board1=[["","","","","","","","","","","","","","","","","","","","E"],
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
                    ["S","#","","","#","","","#","","","#","","","#","","","#","","",""]]

        self.board2=[["","","","","","","","","","","","","","","","","","","","E"],
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
                    ["S","","","","","","","","","","","","","","","","","","",""]]
        
        self.current=self.board1
        self.list=[self.board1,self.board2]
        
    def printBoard(self):
        for row in range(len(self.current)):
            for col in range(len(self.current[0])):
                if self.current[row][col]=="#":
                    fill(255)
                    rect(col*dis,row*dis+buf,dis,dis)
                elif self.current[row][col]=="S":
                    fill(100)
                    rect(col*dis,row*dis+buf,dis,dis)
                elif self.current[row][col]=="E":
                    fill(200)
                    rect(col*dis,row*dis+buf,dis,dis)
    
    def changeStage(self):
        if self.current[student.pos[1]][student.pos[0]]=="E":
            self.current=self.list[self.list.index(self.board1)+1]
            student.pos=(self.current[len(self.current)-1].index("S"),len(self.current)-1)
        
                    
class Friend1:
    def __init__(self,start=(1,8)):
        self.pos=start
        self.dir=random.randint(0,1)
        self.obstruction={"LEFT":False, "RIGHT":False, "UP":False, "DOWN":False}
        self.i = student.pos[0]
        self.j = student.pos[1]
        self.x = self.pos[0]
        self.y = self.pos[1]
    
    def setting(self):
        self.i = student.pos[0]
        self.j = student.pos[1]
        self.x = self.pos[0]
        self.y = self.pos[1]
        #if the friend is already on the same x or y axis as the student
        if self.dir == 0 and self.i == self.x:
            self.dir = 1
        elif self.dir == 1 and self.j == self.y:
            self.dir = 0
    
    def checkObstruction(self):
        if self.pos[0]+1 > 19 or board.current[self.pos[1]][self.pos[0]+1] =="#":
            self.obstruction["RIGHT"]=True
        else:
            self.obstruction["RIGHT"]=False
        if self.pos[0]-1 < 0 or board.current[self.pos[1]][self.pos[0]-1] =="#":
            self.obstruction["LEFT"]=True
        else:
            self.obstruction["LEFT"]=False
        if self.pos[1]+1 > 19 or board.current[self.pos[1]+1][self.pos[0]] =="#":
            self.obstruction["DOWN"]=True
        else:
            self.obstruction["DOWN"]=False
        if self.pos[0]-1 <0 or board.current[self.pos[1]-1][self.pos[0]] =="#":
            self.obstruction["UP"]=True
        else:
            self.obstruction["UP"]=False
    
    def move(self):
        ####NO OBSTRUCTION###
        if self.dir == 0 and self.i > self.x and self.obstruction["RIGHT"]==False: #if student is on the right side and no obstruction
            self.pos = (self.pos[0]+1, self.pos[1])
        elif self.dir == 0 and self.i < self.x and self.obstruction["LEFT"]==False: #if student is on the left side and no obstruction
            self.pos = (self.pos[0]-1, self.pos[1])
        elif self.dir == 1 and self.j > self.y and self.obstruction["DOWN"]==False: #if student is below and no obstruction
            self.pos = (self.pos[0], self.pos[1]+1)
        elif self.dir == 1 and self.j < self.y and self.obstruction["UP"]==False: #if student is above and no obstruction
            self.pos = (self.pos[0], self.pos[1]-1)
        ####OBSTRUCTION####
        elif self.dir == 0 and self.i > self.x and self.obstruction["RIGHT"]==True: #if student on the right and obstruction
            copyObstruction=self.obstruction.copy()
            copyObstruction.pop("RIGHT")
            dList=copyObstruction.keys()
            d = random.randint(0,2)
            while copyObstruction[dList[d]]==True:
                d = random.randint(0,2)
            if dList[d]=="LEFT":
                self.pos = (self.pos[0]-1, self.pos[1])
            elif dList[d]=="DOWN":
                self.pos = (self.pos[0], self.pos[1]+1)
            elif dList[d]=="UP":
                self.pos = (self.pos[0], self.pos[1]-1)
        
        elif self.dir == 0 and self.i < self.x and self.obstruction["LEFT"]==True: #if student on the left and obstruction
            copyObstruction=self.obstruction.copy()
            copyObstruction.pop("LEFT")
            dList=copyObstruction.keys()
            d = random.randint(0,2)
            while copyObstruction[dList[d]]==True:
                d = random.randint(0,2)
            if dList[d]=="RIGHT":
                self.pos = (self.pos[0]+1, self.pos[1])
            elif dList[d]=="DOWN":
                self.pos = (self.pos[0], self.pos[1]+1)
            elif dList[d]=="UP":
                self.pos = (self.pos[0], self.pos[1]-1)
        
        elif self.dir == 1 and self.j > self.y and self.obstruction["DOWN"]==True: #if student is below and obstruction
            copyObstruction=self.obstruction.copy()
            copyObstruction.pop("DOWN")
            dList=copyObstruction.keys()
            d = random.randint(0,2)
            while copyObstruction[dList[d]]==True:
                d = random.randint(0,2)
            if dList[d]=="LEFT":
                self.pos = (self.pos[0]-1, self.pos[1])
            elif dList[d]=="RIGHT":
                self.pos = (self.pos[0]+1, self.pos[1])
            elif dList[d]=="UP":
                self.pos = (self.pos[0], self.pos[1]-1)
        
        elif self.dir == 1 and self.j < self.y and self.obstruction["UP"]==True: #if student is above and obstruction
            copyObstruction=self.obstruction.copy()
            copyObstruction.pop("UP")
            dList=copyObstruction.keys()
            d = random.randint(0,2)
            while copyObstruction[dList[d]]==True:
                d = random.randint(0,2)
            if dList[d]=="LEFT":
                self.pos = (self.pos[0]-1, self.pos[1])
            elif dList[d]=="RIGHT":
                self.pos = (self.pos[0]+1, self.pos[1])
            elif dList[d]=="DOWN":
                self.pos = (self.pos[0], self.pos[1]+1)
                
                
    def drawFriend1(self):
        x = self.pos[0]
        y = self.pos[1]
        fill(255, 255, 51)
        circle(x*dis+dis/2,y*dis+dis/2+buf,dis)
        
class Coffee:
    def __init__(self):
        self.pos=(random.randint(0,19),random.randint(0,19))
        while board.current[self.pos[1]][self.pos[0]]=="#" or self.pos==student.pos or self.pos in stage.coffeePosList:
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
        
class Game:
    def __init__(self):
        self.gameEnd=False
        self.frame=0
        self.count=0
        self.score=0
    def main(self):
        self.drinkCoffee()
        self.meetFriend()
        self.display()
        board.printBoard()
        student.drawStudent()
        student.move()
        friend1.drawFriend1()
        friend1.checkObstruction()
        friend1.setting()
        board.changeStage()
        
        if (friend1.dir == 0 and friend1.i > friend1.x and friend1.obstruction["RIGHT"]==True) or (friend1.dir == 0 and friend1.i < friend1.x and friend1.obstruction["LEFT"]==True)\
        or (friend1.dir == 1 and friend1.j > friend1.y and friend1.obstruction["DOWN"]==True) or (friend1.dir == 1 and friend1.j < friend1.y and friend1.obstruction["UP"]==True):
            self.count+=1
            if self.count%2==0:
                friend1.move()
        else:
            friend1.move()
            
    def display(self):
        #Setting the timer
        self.frame+=1
        fill(255)
        textSize(30)
        timer=60-self.frame//3
        text("Time Remaining: "+str(timer),4,34)
        
        #Display the point
        fill(0)
        rect(348,4,204,30)
        fill(0,60,255)
        rect(350,6,self.score*2,26)
        
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
                self.score+=5
    
    def meetFriend(self):
        if student.pos==friend1.pos:
            self.score-=10
            friend1.pos=(1,8)
    
        
game=Game()
board=Board()
student=Student((board.current[len(board.current)-1].index("S"),len(board.current)-1))
stage=Stage()
friend1=Friend1()

for i in range(7):
    stage.spawnCoffee()
    stage.update()

def setup():
    size(600,700)
    background(205)

def draw():
    if frameCount%20==0:
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
