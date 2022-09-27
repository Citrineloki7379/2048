#Test Comment

import random
from tkinter import *
from tkinter import messagebox

class GameGrid:
    bg_color={
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#edc53f',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    }
    color={
         '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }
    def __init__(self):
        #self.n=4
        self.window=Tk()
        self.window.title('2048 Python')
        self.gameArea=Frame(self.window,bg= 'azure3')
        self.GameGrid=[]
        self.boxes=[[0,0,0,0], 
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        #self.boxes=[[2,4,0,4], 
         #           [4,2,4,0],
         #           [2,0,2,4],
          #          [4,2,4,2]]
        self.moved=False
        #self.movable=False
        self.score=0
        self.points=None####
        for i in range(4):
            rows=[]
            for x in range(4):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('helvetica',25,'bold'),width=5,height=3)
                l.grid(row=i,column=x,padx=10,pady=10,sticky="NSEW")
                rows.append(l)
            self.GameGrid.append(rows)
        self.gameArea.grid(sticky="NSEW")
        self.points=Label(text=str(self.score))###
        self.points.grid(sticky="NSEW")###

    def moveupArray(self):
        array=self.boxes
        combineCheck=[[False, False, False, False],
                  [False, False, False, False],
                  [False, False, False, False],
                  [False, False, False, False]]
        done=False
        iterations=0
        while done==False:
            movements=0
            for x in range(1,len(array)):
                for v,y in enumerate(range(0,len(array[x]))):
                    if array[x][v]==0:
                        continue
                    else:
                        if array[x-1][v]==0:
                            movements=movements+1
                            array[x-1][v], array[x][v]=array[x][v], array[x-1][v]
                            combineCheck[x-1][v], combineCheck[x][v]=combineCheck[x][v], combineCheck[x-1][v]
                            continue
                        elif array[x-1][v]==array[x][v] and combineCheck[x][v]==False and combineCheck[x-1][v]==False:
                            if x>=2:
                                if array[x-2][v]==array[x][v]:
                                    continue
                            movements=movements+1
                            array[x-1][v]=array[x-1][v]+array[x][v]
                            array[x][v]=0
                            combineCheck[x-1][v]=True
                            self.score += array[x-1][v]
                            continue
                        else:
                            continue
            if movements==0:
                done=True
            else:
                iterations=iterations+1
                #self.moved=True
                #self.movable=True
                continue
        self.boxes=array
        if iterations>0:
            self.moved=True
        #return array, iterations
   # def Vcorrect(self):
    #    correction=[]
    #    for i,x in enumerate(range(len(self.boxes))):
     #       correction.insert(0,self.boxes[i])
    #    self.boxes=correction

    def rotateClockwise(self):
        correction=[]
        for i,x in enumerate(range(len(self.boxes[0]))):
            instance=[]
            for v,y in enumerate(range(len(self.boxes))):
                instance.append(self.boxes[v][i])
            instance.reverse()
            correction.append(instance)
        self.boxes=correction

    #def HCorrect(self):
     #   correction=[]
     #   for i,x in enumerate(range(len(self.boxes))):
      #      correction.append(self.boxes[i][-1:(-len(self.boxes[i])-1):-1])
     #   self.boxes=correction

    def addNumber(self):
        count=0
        for i,x in enumerate(range(len(self.boxes))):
            for v,y in enumerate(range(len(self.boxes[i]))):
                if self.boxes[i][v]==0:
                    count=count+1
        place=random.randint(0,count-1)
        number=random.randint(1,10)
        insertion=0
        if number==1:
            insertion=4
        else:
            insertion=2
        iterations=0
        for q,c in enumerate(range(len(self.boxes))):
            if iterations>place:
                break
            for f,k in enumerate(range(len(self.boxes[i]))):
                if self.boxes[q][f]==0:
                    if iterations==place:
                        self.boxes[q][f]=insertion
                    iterations=iterations+1
                else:
                    continue

    def check(self):
        for i in range(3): 
            for j in range(3): 
                if(self.boxes[i][j]== self.boxes[i + 1][j] or self.boxes[i][j]== self.boxes[i][j + 1]): 
                    return True
        for j in range(3): 
            if(self.boxes[3][j]== self.boxes[3][j + 1]): 
                return True
  
        for i in range(3): 
            if(self.boxes[i][3]== self.boxes[i + 1][3]):
                return True
        #print("Game Over")
        return False

    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.boxes[i][j]==0:
                    self.GameGrid[i][j].config(text='',bg='azure4')
                else:
                    self.GameGrid[i][j].config(text=str(self.boxes[i][j]),
                    bg=self.bg_color.get(str(self.boxes[i][j])),
                    fg=self.color.get(str(self.boxes[i][j])))
        self.points.config(text="Score: "+str(self.score))###

class GamePlay:
    def __init__(self,GameGrid):
        self.GameGrid=GameGrid
        self.lose=False
        self.won=False
    def Validate(self):
        flag=False
        for x in range(len(self.GameGrid.boxes)):
            for i in range(len(self.GameGrid.boxes[x])):
                if self.GameGrid.boxes[x][i]==2048:
                    self.won=True
                    messagebox.showinfo('2048', message='You Wonnn!!')
                    print("won")
                    return 0
        
        for i in range(4):
            if flag==True:
                break
            for j in range(4): 
                if(self.GameGrid.boxes[i][j]== 0): 
                    flag=True
                    break
                    
        if flag==False and self.GameGrid.check()==False:
            self.lose=True
            messagebox.showinfo('2048','Game Over!!!')
            print("Game Over")
            return 0
        return 0
    def initialise(self):
        self.GameGrid.addNumber()
        self.GameGrid.addNumber()
        self.GameGrid.paintGrid()
        self.GameGrid.window.bind('<Key>', self.Input)
        self.GameGrid.window.mainloop()
        return 0
    def Input(self, event):
        if self.lose==True or self.won==True:
            messagebox.showinfo('2048', 'No more moves left Close the 2048 Tab')
            return 0
        self.GameGrid.moved=False

        input=event.keysym
        if input=="Up":
            self.GameGrid.moveupArray()
           # if self.GameGrid.moved==False:
              #  self.GameGrid.movable=self.GameGrid.check()#
        elif input=="Down":
            #self.GameGrid.Vcorrect()
            for x in range(2):
                self.GameGrid.rotateClockwise()
            self.GameGrid.moveupArray()
            for x in range(2):
                self.GameGrid.rotateClockwise()
            #self.GameGrid.Vcorrect()
            #if self.GameGrid.moved==False: 
               # self.GameGrid.movable=self.GameGrid.check()
        elif input=="Left":
            self.GameGrid.rotateClockwise()
            self.GameGrid.moveupArray()
            for x in range(3):
                self.GameGrid.rotateClockwise()
            #if self.GameGrid.moved==False:
               # self.GameGrid.movable=self.GameGrid.check()
        elif input=="Right":
            #self.GameGrid.HCorrect()
            #self.GameGrid.rotateClockwise()
            for x in range(3):
                self.GameGrid.rotateClockwise()
            self.GameGrid.moveupArray()
            self.GameGrid.rotateClockwise()
            #for x in range(3):
               # self.GameGrid.rotateClockwise()
            #self.GameGrid.HCorrect()
           # if self.GameGrid.moved==False:
                #self.GameGrid.movable=self.GameGrid.check()
        else:
            pass
        #self.GameGrid.paintGrid()
        #print(str(self.GameGrid.score))
        
        if self.GameGrid.moved==True:
            self.GameGrid.addNumber()
        self.GameGrid.paintGrid()
        self.Validate()
        



