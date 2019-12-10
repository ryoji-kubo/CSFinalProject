import random, time
dis=600/20
buf=100/2

class Student:
    def __init__(self,start):
        self.pos=start
        #Controls the direction of the student
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
    def move(self):
        #controls the movement of the student
        if self.keyHandler[LEFT]==True and self.pos[0]!=0 and board.current[self.pos[1]][self.pos[0]-1]!="#": #Checks if it is valid move (if there is an obstruction then the student won't be able to movve)
            self.pos=(self.pos[0]-1,self.pos[1]) #Move the position of the student
        elif self.keyHandler[RIGHT]==True and self.pos[0]!=19 and board.current[self.pos[1]][self.pos[0]+1]!="#":
            self.pos=(self.pos[0]+1,self.pos[1])
        elif self.keyHandler[UP]==True and self.pos[1]!=0 and board.current[self.pos[1]-1][self.pos[0]]!="#":
            self.pos=(self.pos[0],self.pos[1]-1)
        elif self.keyHandler[DOWN]==True and self.pos[1]!=19 and board.current[self.pos[1]+1][self.pos[0]]!="#":
            self.pos=(self.pos[0],self.pos[1]+1)
    def drawStudent(self):
        #Display the student
        x=self.pos[0]
        y=self.pos[1]
        fill(255)
        circle(x*dis+dis/2,y*dis+dis/2+buf,dis)

class Board:
    def __init__(self):
        #Each board contains how each stage will be mapped
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
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["S","","","","","","","","","","","","","","","","","","",""]]
        
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
                    ["","#","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["S","","","","","","","","","","","","","","","","","","",""]]

        self.board3=[["","","","","","","","","","","","","","","","","","","","E"],
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
                    ["","#","","#","","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","#","","","#","","","#","","","#","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["S","","","","","","","","","","","","","","","","","","",""]]
        
        self.board4=[["","","","","","","","","","","","","","","","","","","","E"],
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
                    ["","#","","#","","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["#","#","#","","","","","#","","","#","","","#","","","#","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["S","","","","","","","","","","","","","","","","","","",""]]
        
        self.board5=[["","","","","","","","","","","","","","","","","","","","E"],
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
                    ["","#","","#","","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","#","","","#","","","#","","","#","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["S","","","","","","","","","","","","","","","","","","",""]]
        
        self.board6=[["","","","","","","","","","","","","","","","","","","","E"],
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
                    ["","#","","#","","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","#","","","#","","","#","","","#","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["S","","","","","","","","","","","","","","","","","","",""]]
        
        
        self.current=self.board1 #This tells which board to map (initially we are at board1)
        self.list=[self.board1,self.board2,self.board3,self.board4,self.board5,self.board6] #contains all the boards
        self.stageList=["BEDROOM","PALM TREE AREA","D2","BARAHA","LIBRARY","UNIX LAB"] #this will be used to determine at which stage we are at
        self.stage="BEDROOM" #initially we are at the palm tree area
        self.newStage = False 
        
    def printBoard(self):
        #prints out the board
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
        #controls the changing of the stage
        #moving from one stage to the next
        if self.current[student.pos[1]][student.pos[0]]=="E" and student.keyHandler[RIGHT]==True:
            self.current=self.list[self.list.index(self.board1)+1]
            self.stage=self.stageList[self.stageList.index(self.stage)+1]
            student.pos=(self.current[len(self.current)-1].index("S"),len(self.current)-1)
            self.newStage=True
        
        #moving back to the stage before
        if self.current[student.pos[1]][student.pos[0]]=="S" and student.keyHandler[LEFT]==True and self.list.index(self.current)!=0:
            self.current=self.list[self.list.index(self.board1)-1]
            self.stage=self.stageList[self.stageList.index(self.stage)-1]
            student.pos=(self.current[0].index("E"),0)
            self.newStage=True
        
                    
class Friend1: #class enemy
    def __init__(self,start=(0,0)):
        self.pos=start #position of the enemy
        self.dir=random.randint(0,1) #determines whether to approach from the x axis or the y axis (0 -> x, 1 -> y)
        self.obstruction={"LEFT":False, "RIGHT":False, "UP":False, "DOWN":False} #checks whether there is an obstruction in each direction
        self.i = student.pos[0] #the x coordinate of the objective
        self.j = student.pos[1] #the y coordinate of the objective
        self.x = self.pos[0] #x coordinate of yourself
        self.y = self.pos[1] #y coordinate of yourself
    
    def setting(self):
        #basic setting
        if board.newStage==True:
            self.pos=(0,0)
        if food.dropped == True: #if there is food 
            self.i = food.pos[0] #change the x,y coordinate of the objective to that of the food
            self.j = food.pos[1]
        else: #if there is no food
            self.i = student.pos[0] #change the x,y coordinate of the objective to that of the student
            self.j = student.pos[1]
        self.x = self.pos[0] #update your x,y coordinate
        self.y = self.pos[1]
        #if the friend is already on the same x or y coordinate as the student
        if self.dir == 0 and self.i == self.x: #if same x, approach by changing y
            self.dir = 1
        elif self.dir == 1 and self.j == self.y: #if same y, approach by changing x
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
        while board.current[self.pos[1]][self.pos[0]]=="#" or self.pos==student.pos or self.pos in stage.coffeePos[board.stage]:
            self.pos=(random.randint(0,19),random.randint(0,19))
        

class Stage:
    def __init__(self):
        self.coffeeData={"BEDROOM":[],"PALM TREE AREA":[],"D2":[],"BARAHA":[],"LIBRARY":[],"UNIX LAB":[]}
        self.coffeePos={"BEDROOM":[],"PALM TREE AREA":[],"D2":[],"BARAHA":[],"LIBRARY":[],"UNIX LAB":[]}
    def spawnCoffee(self,stage):
        self.coffeeData[stage].append(Coffee())
    def update(self,stage):
        for coffee in self.coffeeData[stage]:
            self.coffeePos[stage].append(coffee.pos)
    def display(self):#Display the coffee cups
        for coffee in self.coffeeData[board.stage]:
            x=coffee.pos[0]
            y=coffee.pos[1]
            fill(255,0,0)
            circle(x*dis+dis/2,y*dis+dis/2+buf,dis)
    
        
class Game:
    def __init__(self):
        self.starting=True
        self.gameEnd=False
        self.frame=0
        self.count=0
        self.score=0
        self.met=False
        self.n=0
        self.metpos=(None,None)
        self.ate=False
        self.stallcount=0
        self.atepos=(None,None)
    def main(self):
        if self.starting:
            background(0)
            fill(255)
            textSize(30)
            textAlign(CENTER)
            text("I just want to Graduate!",300,300)
            text("Press Enter to Play", 300, 400)
        elif not self.starting:
            board.changeStage()
            board.printBoard()
            student.move()
            self.display()
            student.drawStudent()
            if board.stage=="PALM TREE AREA" or board.stage=="D2" or board.stage=="BARAHA" or board.stage =="LIBRARY":
                self.drinkCoffee()
                self.meetFriend()
                friend1.drawFriend1()
                stage.display()
                self.eatFood() #this has to come after board.changeStage() and before friend1.setting()
                friend1.checkObstruction()
                friend1.setting()
                food.dropFood()
                friend1.move()
                ###THIS CONTROLLS HOW "DUMB" THE ENEMY IS
                # if (friend1.dir == 0 and friend1.i > friend1.x and friend1.obstruction["RIGHT"]==True) or (friend1.dir == 0 and friend1.i < friend1.x and friend1.obstruction["LEFT"]==True)\
                # or (friend1.dir == 1 and friend1.j > friend1.y and friend1.obstruction["DOWN"]==True) or (friend1.dir == 1 and friend1.j < friend1.y and friend1.obstruction["UP"]==True):
                #     self.count+=1
                #     if self.count%2==0:
                #         friend1.move()
                # else:
                #     friend1.move()
            if board.newStage:
                background(0)
                fill(255)
                textSize(30)
                textAlign(CENTER)
                text(board.stage,300,300)
                text("Press Enter to Continue",300,400)
                board.newStage=False
                noLoop()
            
    def display(self):
        #Setting the timer
        self.frame+=1
        fill(255)
        textAlign(LEFT)
        textSize(30)
        timer=60-self.frame//3
        text("Time Remaining: "+str(timer),4,34)
        
        #Display the point
        fill(0)
        rect(348,4,204,30)
        fill(0,60,255)
        rect(350,6,self.score*2,26)
            
        #Display the remaining food item
        for n in range(food.remaining):
            x = 400+n*40
            y = 660
            fill(255)
            rect(x,y,dis,dis)
            
        #Display the name of the area
        fill(255)
        textSize(30)
        text(board.stage,5,680)
            
    def drinkCoffee(self):
        for coffee in stage.coffeeData[board.stage]:
            if coffee.pos==student.pos:
                stage.coffeeData[board.stage].remove(coffee)
                self.score+=5
    
    def meetFriend(self):
        if not self.met and student.pos==friend1.pos:
            self.metpos=friend1.pos
            if self.score>=10:
                self.score-=10
            elif self.score<10:
                self.score=0
            self.met=True
        elif self.met==True:
            friend1.pos=self.metpos
            self.n+=1
        if self.n==15:
            self.met=False
            self.n=0
    
    def eatFood(self):
        if not self.ate and food.pos==friend1.pos:
            self.atepos=friend1.pos
            self.ate = True
            food.dropped=False
        elif self.ate==True:
            friend1.pos=self.atepos
            self.stallcount+=1
            print(self.stallcount)
        if self.stallcount==30 or board.newStage:
            self.ate=False
            self.stallcount=0
        
        
class Food:
    def __init__(self):
        self.remaining=4
        self.pos=(None,None)
        self.dropped=False    
    def dropFood(self):
        if board.newStage:
            self.pos=(None,None)
            food.dropped=False
        if food.dropped:
            if self.pos!=(None,None):
                x=self.pos[0]
                y=self.pos[1]
                fill(100,100,100)
                circle(x*dis+dis/2,y*dis+dis/2+buf,dis)
        elif food.dropped==False:
            self.pos=(None,None)
        
game=Game()
board=Board()
student=Student((board.current[len(board.current)-1].index("S"),len(board.current)-1))
stage=Stage()
friend1=Friend1()
food=Food()

for n in board.stageList:
    for i in range(7):
        stage.spawnCoffee(n)
        stage.update(n)

def setup():
    size(600,700)
    background(205)

def draw():
    if frameCount%10==0:
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
      
    if key == " " and food.remaining!=0 and not food.dropped:
        food.pos=student.pos
        food.dropped=True
        food.remaining-=1
    
    if key == ENTER and game.starting:
        game.starting = False
    
    elif key == ENTER:
        loop()

def keyReleased():
    if keyCode == LEFT:
        student.keyHandler[LEFT]=False
    elif keyCode == RIGHT:
        student.keyHandler[RIGHT]=False
    elif keyCode == UP:
      student.keyHandler[UP]=False
    elif keyCode == DOWN:
      student.keyHandler[DOWN]=False
