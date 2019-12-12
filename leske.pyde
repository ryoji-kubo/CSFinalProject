import random, time
add_library('minim')
audioPlayer = Minim(this)
dis=600/20
buf=100/2
main_dir = os.getcwd()  # return the current directory
print(main_dir)
cover_dir = main_dir+'/images/'
image_list2 = os.listdir(cover_dir)
file=main_dir+"/score.txt"

class Student:
    def __init__(self,start):
        self.pos=start
        #Controls the direction of the student
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
    def move(self):
        #controls the movement of the student
        if self.keyHandler[LEFT]==True and self.pos[0]!=0 and board.current[self.pos[1]][self.pos[0]-1]!="#" and board.current[self.pos[1]][self.pos[0]-1]!="/" and board.current[self.pos[1]][self.pos[0]-1]!="!" and board.current[self.pos[1]][self.pos[0]-1]!="*":
            self.pos=(self.pos[0]-1,self.pos[1])
        elif self.keyHandler[RIGHT]==True and self.pos[0]!=19 and board.current[self.pos[1]][self.pos[0]+1]!="#" and board.current[self.pos[1]][self.pos[0]+1]!="/" and board.current[self.pos[1]][self.pos[0]+1]!="!" and board.current[self.pos[1]][self.pos[0]+1]!="*":
            self.pos=(self.pos[0]+1,self.pos[1])
        elif self.keyHandler[UP]==True and self.pos[1]!=0 and board.current[self.pos[1]-1][self.pos[0]]!="#" and board.current[self.pos[1]-1][self.pos[0]]!="*" and board.current[self.pos[1]-1][self.pos[0]]!="!" and board.current[self.pos[1]-1][self.pos[0]]!="/":
            self.pos=(self.pos[0],self.pos[1]-1)
        elif self.keyHandler[DOWN]==True and self.pos[1]!=19 and board.current[self.pos[1]+1][self.pos[0]]!="#" and board.current[self.pos[1]+1][self.pos[0]]!="/" and board.current[self.pos[1]+1][self.pos[0]]!="!" and board.current[self.pos[1]+1][self.pos[0]]!="*":
            self.pos=(self.pos[0],self.pos[1]+1)
    def drawStudent(self):
        #Display the student
        x=self.pos[0]
        y=self.pos[1]
        if student.keyHandler[LEFT]==True: 
            image(board.ryoji_left,x*dis,y*dis+buf,dis,dis)        
        elif student.keyHandler[UP]==True:
            image(board.ryoji_up,x*dis,y*dis+buf,dis,dis)
        elif student.keyHandler[DOWN]==True:
            image(board.ryoji_down,x*dis,y*dis+buf,dis,dis)
        else:
            image(board.ryoji_right,x*dis,y*dis+buf,dis,dis)

class Board:
    def __init__(self):
        #Each board contains how each stage will be mapped
        self.board1=[["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["#","#","#","#","#","#","#","#","#","E","#","#","#","#","#","#","#","#","#","#"],
                    ["#","","","","","","","Z","","","","","","","","","","","","#"],
                    ["#","O","/","","","#","","","","","","","","","#","O","/","","","#"],
                    ["#","/","/","","","#","","","","","","","","","#","/","/","","","#"],
                    ["#","","","","","#","","","","","","","","","#","","","","","#"],
                    ["#","","*","","","#","!","/","","","","","!","/","#","","*","","","#"],
                    ["#","","","","","#","/","/","","","","","/","/","#","","","","","#"],
                    ["#","","S","","","#","","","","","","","","","#","","","","","#"],
                    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""]]

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
                    ["S","#","","","#","","","#","","","#","","","#","","","#","","",""]]

        self.board3=[["","","","","","","","","","","","","","","","","","","","E"],
                    ["#","","","*","/","","*","/","","*","/","","*","/","","*","/","","*","/"],
                    ["","","","/","/","","/","/","","/","/","","/","/","","/","/","","/","/"],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","#","","","#","","","#","","","#","","","#","","","#","","#",""],
                    ["#","","","#","","","#","","","#","","","#","","","#","","#","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["#","","","*","/","","*","/","","*","/","","*","/","","*","/","","*","/"],
                    ["","","","/","/","","/","/","","/","/","","/","/","","/","/","","/","/"],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["*","/","","","#","","","#","","","#","","","#","","","#","","*","/"],
                    ["/","/","","","","","","","","","","","","","","","","","/","/"],
                    ["","","","","","","","#","","","#","","","#","","","#","","",""],
                    ["!","!","!","!","!","","#","","","#","","","#","","","#","","","#",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","!","!","!","!","","","#","","","#","","","#","","","#","","","#"],
                    ["","!","","","#","","","#","","","#","","","#","","","#","","",""],
                    ["","!","","","","","","","","","","","","","","","","","",""],
                    ["","!","","*","/","","*","/","","*","/","","*","/","","*","/","","*","/"],
                    ["S","!","","/","/","","/","/","","/","/","","/","/","","/","/","","/","/"]]
        
        self.board4=[["","","*","*","*","","*","*","*","","","*","","*","","*","","*","",""],
                    ["S","","","","O","/","","","*","","","*","","*","","*","","*","",""],
                    ["","","","","/","/","","","*","","","","","","","*","","*","",""],
                    ["","!","/","","","","","","","","","","","","","*","","*","",""],
                    ["","/","/","","#","/","/","/","","","#","/","/","/","","","","","",""],
                    ["","","","","/","/","/","/","","","/","/","/","/","","","","","",""],
                    ["*","*","*","","/","/","/","/","","","/","/","/","/","","","","*","",""],
                    ["","","","","","","","","","","","","","","","","","*","",""],
                    ["","O","/","","#","/","/","/","","?","/","/","","?","/","/","","*","",""],
                    ["","/","/","","/","/","/","/","","/","/","/","","/","/","/","","*","","E"],
                    ["","","","","/","/","/","/","","/","/","/","","/","/","/","","","",""],
                    ["","","","","","","","","","","","","","","","","","*","",""],
                    ["","!","/","","*","","?","/","/","","?","/","/","","!","/","","*","",""],
                    ["","/","/","","*","","/","/","/","","/","/","/","","/","/","","*","",""],
                    ["","","","","","","/","/","/","","/","/","/","","","","","*","",""],
                    ["","!","/","","*","","","","","","","","","","*","","","","",""],
                    ["","/","/","","*","","#","/","/","/","","?","/","/","","*","","!","/",""],
                    ["","","","","*","","/","/","/","/","","/","/","/","","*","","/","/",""],
                    ["","O","/","","*","","/","/","/","/","","/","/","/","","*","","","",""],
                    ["","/","/","","*","","","","","","","","","","","","","","",""]]
        
        self.board5=[["","!","!","!","!","!","!","!","!","!","!","!","!","!","!","!","!","!","","E"],
                    ["","","","","","","","","","","","","","","","","","","","!"],
                    ["","","!","","!","!","!","!","","!","","!","","!","!","!","!","!","!","!"],
                    ["","","!","","","","","","","","","!","","","","","","","","!"],
                    ["","","","","!","!","!","!","","!","","!","","!","!","!","!","!","!","!"],
                    ["","","!","","","","","","","","","!","","","","","","","","!"],
                    ["","","!","","!","!","!","!","","!","","!","","!","!","!","!","!","!","!"],
                    ["","","","","","","","","","","","!","","","","","","","","!"],
                    ["","","!","","!","!","!","!","","!","","!","","!","!","!","!","!","!","!"],
                    ["","","!","","","","","","","","","!","","","","","","","","!"],
                    ["","","","","!","!","!","!","","!","","","","!","!","!","!","!","!","!"],
                    ["","","!","","","","","","","","","!","","","","","","","","!"],
                    ["","","!","","!","!","!","!","","!","","!","","!","!","!","!","!","!","!"],
                    ["","","","","","","","","","","","","","","","","","","","!"],
                    ["","","!","","!","!","!","!","","!","","!","","!","!","!","!","!","!","!"],
                    ["","","!","","","","","","","","","!","","","","","","","","!"],
                    ["","","","","!","!","!","!","","!","","","","","","","","","","!"],
                    ["","","!","","","","","","","","","!","","!","!","!","!","!","!","!"],
                    ["","","","","","","","","","","","","","","","","","","","!"],
                    ["S","","!","","!","!","!","!","","!","","!","!","!","!","!","!","!","!","!"]]
        
        self.board6=[["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                    ["","","","","","","","","","","","","","","","","","","","#"],
                    ["","","","","","","","","","","","","","","","","","","","#"],
                    ["","","","","","","","","","","","","","","","","","","","#"],
                    ["S","","","","","","","","","E","#","#","","","","","","","","#"],
                    ["","","","","","","","","","","","","","","","","","","","#"],
                    ["","","","","","","","","","","","","","","","","","","","#"],
                    ["","","","","","","","","","","","","","","","","","","","#"],
                    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""],
                    ["","","","","","","","","","","","","","","","","","","",""]]
        
        
        self.current=self.board1 #This tells which board to map (initially we are at board1)
        self.list=[self.board1,self.board2,self.board3,self.board4,self.board5,self.board6] #contains all the boards
        self.stageList=["BEDROOM","PALM TREE AREA","D2","BARAHA","LIBRARY","UNIX LAB"] #this will be used to determine at which stage we are at
        self.stage="BEDROOM" #initially we are at the Bedroom
        self.startpos=[(2,15),(0,19),(0,19),(0,19),(0,19),(0,9)] #logs where to start for each stage
        self.endpos=[(9,8),(19,0),(19,0),(19,0),(19,0),(9,9)] #logs where the exit is for each stage
        self.newStage = False #turns true when changing a stage
        self.currentIndex=0 #used for changing self.current and self.stage and referring to the start and end points
        
        ###IMAGES###
        self.ryoji_up=loadImage(cover_dir+"Testing_up.jpg")
        self.ryoji_down=loadImage(cover_dir+"Testing_down.jpg")
        self.ryoji_right=loadImage(cover_dir+"Testing_right.jpg")
        self.ryoji_left=loadImage(cover_dir+"Testing_left.jpg")
        self.coffee_cup=loadImage(cover_dir+"Starbucks.jpg")
        self.free_food=loadImage(cover_dir+"free_food.jpg")
        self.friend_enemy=loadImage(cover_dir+"Testing 3.jpg")
        self.palm_tree=loadImage(cover_dir+"palm_tree.jpg")
        self.table_one=loadImage(cover_dir+"D2 table 1.jpg")
        self.table_two=loadImage(cover_dir+"round lunch table.jpg")
        self.bed=loadImage(cover_dir+"bed.png")
        self.couch1=loadImage(cover_dir+"couches1.png")
        self.couch2=loadImage(cover_dir+"couches2.png")
        self.pooltable=loadImage(cover_dir+"pool table.png")
        self.carpet=loadImage(cover_dir+"carpet.png")
        self.desk=loadImage(cover_dir+"desk.png")
        self.airhockey=loadImage(cover_dir+"Aior hockey table.png")
        self.drink= audioPlayer.loadFile(main_dir+"/music/drink.mp3")
        self.meh= audioPlayer.loadFile(main_dir+"/music/meh.mp3")
        self.winner= audioPlayer.loadFile(main_dir+"/music/winner.mp3")
        self.dun= audioPlayer.loadFile(main_dir+"/music/dun dun dun.mp3")  
        self.food= audioPlayer.loadFile(main_dir+"/music/food.mp3")        
        
    def printBoard(self):
        #prints out the board
        if self.current==self.board1:    
            for row in range(len(self.current)):
                for col in range(len(self.current[0])):
                    if self.current[row][col]=="!":
                        image(self.couch1,col*dis,row*dis+buf,dis*2,dis*2)
                    elif self.current[row][col]=="S":
                        fill(0,255,0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="E":
                        fill(255,0,0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="*":
                        image(self.bed,col*dis,row*dis+buf,dis*2,dis*2)
                    elif self.current[row][col]=="#":
                        fill(200)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="O":
                        image(self.desk,col*dis,row*dis+buf,dis*2,dis*2)
                    elif self.current[row][col]=="Z":
                        image(self.carpet,col*dis,row*dis+buf)

        elif self.current==self.board2:                                                           
            for row in range(len(self.current)):
                for col in range(len(self.current[0])):
                    if self.current[row][col]=="#":
                        fill(255)
                        image(self.palm_tree,col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="S":
                        fill(0,255,0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="E":
                        fill(255,0,0)
        elif self.current==self.board3:
            for row in range(len(self.current)):
                for col in range(len(self.current[0])):
                    if self.current[row][col]=="!":
                        fill(233)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="S":
                        fill(0,255,0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="E":
                        fill(255,0,0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="*":
                        image(self.table_one,col*dis,row*dis+buf,dis*2,dis*2)
                    elif self.current[row][col]=="#":
                        image(self.table_two,col*dis,row*dis+buf,dis,dis)

        elif self.current==self.board4:
            for row in range(len(self.current)):
                for col in range(len(self.current[0])):
                    if self.current[row][col]=="#":
                        image(self.pooltable,col*dis,row*dis+buf,dis*4,dis*3)
                    elif self.current[row][col]=="O":
                        image(self.couch2,col*dis,row*dis+buf,dis*2,dis*2)
                    elif self.current[row][col]=="?":
                        image(self.airhockey,col*dis,row*dis+buf,dis*3,dis*3)
                    elif self.current[row][col]=="!":
                        image(self.couch1,col*dis,row*dis+buf,dis*2,dis*2)
                    elif self.current[row][col]=="*":
                        fill(100)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="S":
                        fill(0,255,0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="E":
                        fill(255,0,0)
                        rect(col*dis,row*dis+buf,dis,dis)
        elif self.current==self.board5:
            for row in range(len(self.current)):
                for col in range(len(self.current[0])):
                    if self.current[row][col]=="!":
                        fill(0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="S":
                        fill(0,255,0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="E":
                        fill(255,0,0)
                        rect(col*dis,row*dis+buf,dis,dis)
        elif self.current==self.board6:
            for row in range(len(self.current)):
                for col in range(len(self.current[0])):
                    if self.current[row][col]=="#":
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="S":
                        fill(0,255,0)
                        rect(col*dis,row*dis+buf,dis,dis)
                    elif self.current[row][col]=="E":
                        fill(255,0,0)
                        rect(col*dis,row*dis+buf,dis,dis)
            
    
    def changeStage(self):
        #controls the changing of the stage
        #moving from one stage to the next
        if self.current[student.pos[1]][student.pos[0]]=="E" and (student.keyHandler[RIGHT]==True or student.keyHandler[UP]==True) and self.stage!="UNIX LAB":
            self.currentIndex+=1
            self.current=self.list[self.currentIndex]
            self.stage=self.stageList[self.currentIndex]
            student.pos=self.startpos[self.currentIndex]
            self.newStage=True
        
        #moving back to the stage before
        if self.current[student.pos[1]][student.pos[0]]=="S" and student.keyHandler[LEFT]==True and self.list.index(self.current)!=0:
            self.currentIndex-=1
            self.current=self.list[self.currentIndex]
            self.stage=self.stageList[self.currentIndex]
            student.pos=self.endpos[self.currentIndex]
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
        if self.pos[0]+1 > 19 or board.current[self.pos[1]][self.pos[0]+1] =="#" or board.current[self.pos[1]][self.pos[0]+1] =="O" or board.current[self.pos[1]][self.pos[0]+1] =="/" or board.current[self.pos[1]][self.pos[0]+1] =="!" or board.current[self.pos[1]][self.pos[0]+1] =="*":
            self.obstruction["RIGHT"]=True
        else:
            self.obstruction["RIGHT"]=False
        if self.pos[0]-1 < 0 or board.current[self.pos[1]][self.pos[0]-1] =="#" or board.current[self.pos[1]][self.pos[0]-1] =="O" or board.current[self.pos[1]][self.pos[0]-1] =="/" or board.current[self.pos[1]][self.pos[0]-1] =="!" or board.current[self.pos[1]][self.pos[0]-1] =="*":
            self.obstruction["LEFT"]=True
        else:
            self.obstruction["LEFT"]=False
        if self.pos[1]+1 > 19 or board.current[self.pos[1]+1][self.pos[0]] =="#" or board.current[self.pos[1]+1][self.pos[0]] =="O" or board.current[self.pos[1]+1][self.pos[0]] =="/" or board.current[self.pos[1]+1][self.pos[0]] =="!" or board.current[self.pos[1]+1][self.pos[0]] =="*":
            self.obstruction["DOWN"]=True
        else:
            self.obstruction["DOWN"]=False
        if self.pos[0]-1 <0 or board.current[self.pos[1]-1][self.pos[0]] =="#" or board.current[self.pos[1]-1][self.pos[0]] =="/" or board.current[self.pos[1]-1][self.pos[0]] =="!" or board.current[self.pos[1]-1][self.pos[0]] =="*":
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
        image(board.friend_enemy,x*dis,y*dis+buf,dis,dis)
    
                
class Coffee:
    def __init__(self,stageName):
        self.pos=(random.randint(0,19),random.randint(0,19))
        self.index=board.stageList.index(stageName)
        self.board=board.list[self.index]
        # while self.board[self.pos[1]][self.pos[0]]=="#" or self.pos==student.pos or self.pos in stage.coffeePos[stageName]:
        #     self.pos=(random.randint(0,19),random.randint(0,19))
        while self.board[self.pos[1]][self.pos[0]]=="#" or self.board[self.pos[1]][self.pos[0]]=="O"  or self.board[self.pos[1]][self.pos[0]]=="!" or self.board[self.pos[1]][self.pos[0]]=="*" or self.board[self.pos[1]][self.pos[0]]=="/" or self.pos==student.pos or self.pos in stage.coffeePos[stageName]:
            self.pos=(random.randint(0,19),random.randint(0,19))

class Stage:
    def __init__(self):
        self.coffeeData={"BEDROOM":[],"PALM TREE AREA":[],"D2":[],"BARAHA":[],"LIBRARY":[],"UNIX LAB":[]}
        self.coffeePos={"BEDROOM":[],"PALM TREE AREA":[],"D2":[],"BARAHA":[],"LIBRARY":[],"UNIX LAB":[]}
    def spawnCoffee(self,stage):
        self.coffeeData[stage].append(Coffee(stage))
    def update(self,stage):
        for coffee in self.coffeeData[stage]:
            self.coffeePos[stage].append(coffee.pos)
    def display(self):#Display the coffee cups
        for coffee in self.coffeeData[board.stage]:
            x=coffee.pos[0]
            y=coffee.pos[1]
            image(board.coffee_cup,x*dis,y*dis+buf,dis,dis)
    
        
class Game:
    def __init__(self):
        self.starting=True
        self.instructions=False
        self.timeOver=False
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
        self.timer=200-self.frame//3
        self.finalScore=0
    def main(self):
        if self.starting:
            inputFile=open(file,"r")
            data=inputFile.readlines()
            scores=[]
            for n in data:
                scores.append(int(n.strip()))    
            best=max(scores)
            inputFile.close()
            background(0)
            fill(255,255,51)
            textFont(font,30)
            textAlign(CENTER)
            text("HIGHSCORE: "+str(best),300,30)
            text("I just want to Graduate!",300,300)
            textSize(20)
            fill(255)
            text("By Abdi Ambari and Ryoji Kubo", 300, 600)
            text("Press Enter to Play", 300, 350)
            text("Press Space for Instruction", 300,375)
            if self.instructions:
                background(0)
                fill(255,255,51)
                textFont(font,30)
                textAlign(CENTER)
                text("This is the instruction page",300,300)
                text("Press shift to go back",300,350)
                noLoop()
        elif not self.starting:
            board.changeStage()
            board.printBoard()
            student.move()
            self.display()
            student.drawStudent()
            self.checkEnd()
            if board.stage=="PALM TREE AREA" or board.stage=="D2" or board.stage=="BARAHA" or board.stage =="LIBRARY":
                self.drinkCoffee()
                self.meetFriend()
                friend1.drawFriend1()
                stage.display()
                self.eatFood() #this has to come after board.changeStage() and before friend1.setting()
                friend1.checkObstruction()
                friend1.setting()
                food.dropFood()
                if not self.ate:
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
                friend1.pos=(0,0)
                self.ate=False
                self.stallcount=0
                self.met=False
                self.n=0
                background(0)
                fill(255)
                textSize(30)
                textAlign(CENTER)
                text(board.stage,300,300)
                text("Press Enter to Continue",300,400)
                noLoop()
            if self.timeOver==True:
                background(0)
                fill(255)
                textSize(30)
                textAlign(CENTER)
                text("TIMEOVER",300,300)
                noLoop()
            if self.gameEnd==True:
                self.finalScore=self.timer+self.score*2+food.remaining*10
                outputFile=open(file,"a")
                outputFile.write(str(self.finalScore)+"\n")
                outputFile.close()
                inputFile=open(file,"r")
                data=inputFile.readlines()
                scores=[]
                for n in data:
                    scores.append(int(n.strip()))    
                best=max(scores)
                scores.remove(max(scores))
                secondBest=max(scores)
                scores.remove(max(scores))
                thirdBest=max(scores)
                scores.remove(max(scores))
                inputFile.close()
                highscore=False
                second=False
                third=False
                if self.finalScore==best:
                    highscore=True
                elif self.finalScore==secondBest:
                    second=True
                elif self.finalScore==thirdBest:
                    third=True
                if self.score<=40:
                    background(0)
                    fill(255)
                    textSize(30)
                    textAlign(CENTER)
                    board.dun.rewind()
                    board.dun.play()
                    text("YOU FAILED",300,300)
                    text("YOU SCORE IS: "+str(self.finalScore),300,350)
                    if highscore:
                        text("!NEW HIGHSCORE!",300,375)
                    text("RANKING",300,400)
                    if highscore:
                        fill(255,255,51)
                        text(best,300,440)
                    else:
                        fill(255)
                        text(best,300,440)
                    if second:
                        fill(255,255,51)
                        text(secondBest,300,470)
                    else:
                        fill(255)
                        text(secondBest,300,470)
                    if third:
                        fill(255,255,51)
                        text(thirdBest,300,500)
                    else:
                        fill(255)
                        text(thirdBest,300,500)
                    noLoop()
                elif self.score>40 and self.score<=70:
                    background(0)
                    fill(255)
                    textSize(30)
                    textAlign(CENTER)
                    board.meh.rewind()
                    board.meh.play()
                    text("YOU MEDIUM",300,300)
                    text("YOU SCORE IS: "+str(self.finalScore),300,350)
                    if highscore:
                        text("!NEW HIGHSCORE!",300,375)
                    text("RANKING",300,400)
                    if highscore:
                        fill(255,255,51)
                        text(best,300,440)
                    else:
                        fill(255)
                        text(best,300,440)
                    if second:
                        fill(255,255,51)
                        text(secondBest,300,470)
                    else:
                        fill(255)
                        text(secondBest,300,470)
                    if third:
                        fill(255,255,51)
                        text(thirdBest,300,500)
                    else:
                        fill(255)
                        text(thirdBest,300,500)
                    noLoop()
                elif self.score>70:
                    background(0)
                    fill(255)
                    textSize(30)
                    textAlign(CENTER)
                    board.winner.rewind()
                    board.winner.play()
                    text("YOU BEST",300,300)
                    text("YOU SCORE IS: "+str(self.finalScore),300,350)
                    if highscore:
                        text("!NEW HIGHSCORE!",300,375)
                    text("RANKING",300,400)
                    if highscore:
                        fill(255,255,51)
                        text(best,300,440)
                    else:
                        fill(255)
                        text(best,300,440)
                    if second:
                        fill(255,255,51)
                        text(secondBest,300,470)
                    else:
                        fill(255)
                        text(secondBest,300,470)
                    if third:
                        fill(255,255,51)
                        text(thirdBest,300,500)
                    else:
                        fill(255)
                        text(thirdBest,300,500)
                    noLoop()
                    
    def display(self):
        #display rectange on the buffers
        fill(0)
        rect(0,0,600,50)
        rect(0,650,600,50)
        #Setting the timer
        self.frame+=1
        self.timer=200-self.frame//3
        fill(255)
        textAlign(LEFT)
        textSize(30)
        text("Time Remaining: "+str(self.timer),4,34)
        
        #Display the point
        fill(0)
        rect(348,4,204,30)
        fill(0,60,255)
        rect(350,6,self.score*2,26)
            
        #Display the remaining food item
        for n in range(food.remaining):
            x = 400+n*40
            y = 660
            image(board.free_food,x,y,dis,dis)
            
        #Display the name of the area
        fill(255)
        textSize(30)
        text(board.stage,5,680)
            
    def drinkCoffee(self):
        for coffee in stage.coffeeData[board.stage]:
            if coffee.pos==student.pos:
                stage.coffeeData[board.stage].remove(coffee)
                board.drink.rewind()
                board.drink.play()
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
            board.food.rewind()
            board.food.play()
            food.dropped=False
        elif self.ate==True:
            friend1.pos=self.atepos
            self.stallcount+=1
            print(self.stallcount)
        if self.stallcount==30:
            self.ate=False
            self.stallcount=0
    def checkEnd(self):
        if self.timer==0:
            self.timeOver=True
        elif board.current[student.pos[1]][student.pos[0]]=="E" and board.stage=="UNIX LAB":
            self.gameEnd=True
            
        
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
                image(board.free_food,x*dis,y*dis+buf,dis,dis)
        elif food.dropped==False:
            self.pos=(None,None)

def reset():
    global game,board,student,stage,friend1,food        
    game=Game()
    board=Board()
    student=Student(board.startpos[board.currentIndex])
    stage=Stage()
    friend1=Friend1()
    food=Food()
    for n in board.stageList:
        for i in range(7):
            stage.spawnCoffee(n)
            stage.update(n)

reset()


def setup():
    global font
    size(600,700)
    background(255)
    font=loadFont("Phosphate-Solid-48.vlw")
             

def draw():
    if frameCount%20==0:
        background(255)
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
      
    if key == " " and food.remaining!=0 and not food.dropped and board.stage!="BEDROOM" and board.stage!="UNIX LAB" :
        food.pos=student.pos
        food.dropped=True
        food.remaining-=1
    
    if key == " " and game.starting:
        game.instructions = True
    
    elif keyCode == SHIFT and game.instructions:
        game.instructions = False
        loop()
    if key == ENTER and game.starting:
        game.starting = False
    elif key == ENTER and board.newStage:
        board.newStage=False
        loop()
    
    elif key == ENTER and game.timeOver:
        game.timeOver=False
        reset()
        loop()
    
    elif key == ENTER and game.gameEnd:
        game.gameEnd=False
        reset()
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
