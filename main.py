import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import random
import time
import enum
from queue import PriorityQueue

class Stack:


    def __init__(self):
        self._stackArray = [];
        self._top = -1;
        self.Full=0

    def Size(self):
        return len(self._stackArray)

    def Push(self,element):
            self._top=self._top+1
            self._stackArray.append(element)
            self.Full=self.Full+1

    def Pop(self):
        if self._top==-1:
            return "Stack is Empty"
        else:
            self._top=self._top-1
            self.Full = self.Full - 1
            return self._stackArray.pop()
    def Display(self):
        return  self._stackArray

class Queue:
    def __init__(self):
        # self.Size=Size
        self.QueueArray = [];

    def Enqueue(self, Element,Mode):

        if isinstance(Element, list) and Mode=="List":
            for item in Element:
                self.Enqueue(item,"No List")
        else:
            self.QueueArray.append(Element)

    def Dequeue(self):
        if self.size() == 0:
            return "Queue Underflow"
        else:
            deletedElement = self.QueueArray[0]
            self.QueueArray.remove(deletedElement)
            return deletedElement




    def DisplayQueue(self):
        return self.QueueArray

    def size(self):
        return len(self.QueueArray)

    def Clear(self):
        self.QueueArray.clear()


class From(enum.Enum):
    start = 0
    up = 1
    right = 2
    bottom = 3
    left = 4
    nonvisited=5


class PushButton(QPushButton):
    def __init__(self, text, style,row,column, color, parent=None):
        super(PushButton, self).__init__(text, parent)
        self.setStyleSheet(style)
        self.setText(text)
        self.setMinimumSize(QSize(35, 35))
        self.setMaximumSize(QSize(35, 35))
        self.color=color
        self.status=""
        self.InfoArray=[row, column, From.nonvisited]


class OptionButton(QPushButton):
    def __init__(self, text,width, parent=None):
        super(QPushButton, self).__init__(text, parent)
        self.setFont(QFont('Century Gothic',10))
        self.setMaximumWidth(width)

class Lables(QLabel):
    def __init__(self,text,width,parent=None):
        super(QLabel,self).__init__(text,parent)
        self.setFont(QFont('Century Gothic',10))
        self.setText(text)
        self.setMaximumWidth(width)


class ComboBox(QComboBox):
    def __init__(self,Items):
        super(ComboBox, self).__init__()
        self.addItems(Items)
        self.setMaximumWidth(200)

        self.setFont(QFont('Century Gothic',10))

class Search():



    def __init__(self,Buttons):
        self.Buttons=Buttons
        self.queue=Queue()
        self.stack=Stack()


    def DFS(self,Current,Goal):
        Neighbors=FindNeighbor(Current,"Without From")


        current=FindButton(Current)
        current.status="visited"
        up = FindButton(Neighbors[0])
        right = FindButton(Neighbors[1])
        bottom = FindButton(Neighbors[2])
        left = FindButton(Neighbors[3])
        w.NodeCount+=1
        if Goal==Current:
            return 1
        if current.color!="red":
            ColorizeButton(current,"Pink")
            sleep_program()
        if up!=0 :
            if up.color!= "black" and up.status!= "visited":
                NextNode=[Current[0]-1,Current[1]]

                if self.DFS(NextNode,Goal) :
                    if current.color != "red":
                        self.stack.Push(current)
                    return 1

        if right!=0 :
            if right.color!= "black" and right.status!= "visited":
                NextNode=[Current[0],Current[1]+1]

                if self.DFS(NextNode,Goal) :
                    if current.color != "red":
                        self.stack.Push(current)
                    return 1

        if bottom!=0 :
            if bottom.color!= "black" and bottom.status!= "visited":
                NextNode=[Current[0]+1,Current[1]]

                if self.DFS(NextNode,Goal) :
                    if current.color != "red":
                        self.stack.Push(current)
                    return 1
        if left!=0 :
            if left.color!= "black" and left.status!= "visited":
                NextNode=[Current[0],Current[1]-1]

                if self.DFS(NextNode,Goal) :
                    if current.color!="red":
                        self.stack.Push(current)
                    return 1
        if current.color!="red":
            ColorizeButton(current,"Pink")
            sleep_program()

    def BFS(self,Current,Goal):

        CurrentNode=Current.copy()
        CurrentNode.append(From.start)
        self.queue.Enqueue(CurrentNode, "No List")

        Result=None

        while Result!=True:

            Node=self.queue.Dequeue()
            if Node=="Queue Underflow":
                return False

            Result = self.CheckGoal(Node,Goal)

        self.queue.Clear()
        return True

    def AStar(self,Origin,Goal):
        Current=Origin.copy()
        PQueue = PriorityQueue()
        g=0

        FindButton(Current).status = "visited"
        FindButton(Current).InfoArray[2] =From.start
        w.NodeCount+=1
        while True:

            List = FindNeighbor(Current,"With From")


            if g!=0:
                g=get[1]+1
            else:
                g=1
            List=self.CheckUnacceptableButtons(List)

            for i in List:
                FindButton(i).status="added"
                FindButton(i).InfoArray[2]=i[2]
                h = self.Calculate_H(i,Goal)
                f = g+h
                PQueue.put((f, g, h, i))

            if PQueue.empty() :
                return False
            get = PQueue.get()
            Current=get[3]
            w.NodeCount+=1
            current = FindButton(Current)
            current.status="visited"
            if current.color != "green":
                ColorizeButton(current,"Pink")
                sleep_program()
            Current.append(get[1])




            if current.color == "green":
                node=Current.copy()
                while node[2] != From.start:
                    if FindButton(node[:2]).color != "green":
                        self.stack.Push(node)

                    if node[2] == From.up:
                        node = self.Buttons[node[0] - 1][node[1]].InfoArray
                    elif node[2] == From.right:
                        node = self.Buttons[node[0]][node[1] + 1].InfoArray
                    elif node[2] == From.bottom:
                        node = self.Buttons[node[0] + 1][node[1]].InfoArray
                    elif node[2] == From.left:
                        node = self.Buttons[node[0]][node[1] - 1].InfoArray
                return True






    def Calculate_H(self,Current,Goal):
        Currentrow = Current[0]
        Currentcolumn = Current[1]
        Goalrow = Goal[0]
        Goalcolumn = Goal[1]

        Diffrence_of_rows = pow(Currentrow - Goalrow, exp=2)
        Diffrence_of_columns = pow(Currentcolumn - Goalcolumn, exp=2)

        eclidus = Diffrence_of_rows + Diffrence_of_columns
        return eclidus



    def CheckGoal(self,Current,Goal):

        Currentrow = Current[0]
        Currentcolumn = Current[1]
        CurrentFrom=Current[2]
        current = FindButton(Current[:2])
        current.status = "visited"
        if CurrentFrom==From.start:
            w.NodeCount += 1
            self.Buttons[Currentrow][Currentcolumn].InfoArray=[Currentrow, Currentcolumn, CurrentFrom]


        List=FindNeighbor(Current,"With From")


        List=self.CheckUnacceptableButtons(List)

        for i in List:
            self.Buttons[i[0]][i[1]].InfoArray = i


        for i in List:
            if i[0:2] == Goal:
                node=i
                while node[2]!=From.start:
                    if FindButton(node[:2]).color!="green":
                        self.stack.Push(node)

                    if node[2]==From.up:
                        node=self.Buttons[node[0]-1][node[1]].InfoArray
                    elif node[2]==From.right:
                        node = self.Buttons[node[0]][node[1]+1].InfoArray
                    elif node[2]==From.bottom:
                        node = self.Buttons[node[0] + 1][node[1]].InfoArray
                    elif node[2]==From.left:
                        node = self.Buttons[node[0]][node[1]-1].InfoArray

                w.NodeCount += 1
                return True
            w.NodeCount+=1
            ColorizeButton(i[:2],"Pink")
            sleep_program()

        self.queue.Enqueue(List, "List")







    def CheckUnacceptableButtons(self,List):
        RemovedList=[]
        for i in List:
            button=self.Buttons[i[0]][i[1]]
            if button==0:
                RemovedList.append(i)
            elif button.status=="visited"or button.status=="added" or button.color=="black" or self.Buttons[i[0]][i[1]].InfoArray[2]!=From.nonvisited:
                RemovedList.append(i)

        for i in RemovedList:
            List.remove(i)

        return List


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        width=1100
        height=900
        self.setFixedSize(width,height)


        self.rows = 20
        self.columns = 30
        self.Buttons = [[0 for x in range(self.columns)] for y in range(self.rows)]
        self.NodeCount=0
        self.Styles = {
            "White": """
                background-color:white;
                max-height:35px;
                max-width:35px;
                border :1px solid gray;
                """,
            "Black": """
                background-color:black;
                max-height:35px;
                max-width:35px;
                border :1px solid gray;
                """,
            "Red": """
                background-color:red;
                max-height:35px;
                max-width:35px;
                border :1px solid gray;
                """,
            "Green": """
                background-color:lime;
                max-height:35px;
                max-width:35px;
                border :1px solid gray;
                """,
            "Light Green": """
                background-color:#cbe8d6;
                max-height:35px;
                max-width:35px;
                border :1px solid gray;
                color:black;
                """,
            "Pink": """
                background-color:#f9cdeb;
                max-height:35px;
                max-width:35px;
                border :1px solid gray;
                """}
        self.Red=None
        self.Green=None
        self.redpositions=[0,0]
        self.greenpositions=[0,0]



        Widget= QWidget()
        self.vertical = QVBoxLayout()
        self.inWidget = QWidget()
        self.layout = QGridLayout(self.inWidget)
        self.MessageBox()
        self.CreateButtons()
        self.Researcher = Search(self.Buttons)
        self.CreateOptionBox()
        Widget.setLayout(self.vertical)
        self.setCentralWidget(Widget)


    def MessageBox(self):
        self.MB = QMessageBox()
        self.MB.setStandardButtons(QMessageBox.Ok)

    def CreateOptionBox(self):
        self.layout.setVerticalSpacing(0)
        self.layout.setHorizontalSpacing(0)
        self.vertical.addWidget(self.inWidget)
        self.OptionBox = QGridLayout()


        #ComboBoxs
        self.ColorCombobox = ComboBox(["Green", "Red", "Black", "White"])
        self.ColorCombobox.setEnabled(False)
        self.SearchMethodComboBox = ComboBox(["DFS", "BFS", "A*"])
        self.DensityComboBox = ComboBox(["1", "2", "3", "4", "5"])
        self.HandyComboBox = ComboBox(["UnHandy", "Handy"])
        self.AnimationRateComboBox=ComboBox(["Without Animation","20","40","60","80","100","150","300","500","1000"])

        self.HandyComboBox.currentTextChanged.connect(self.HandyHandeling)

        #Option Buttons
        self.GenerateButton = OptionButton(text="Generate Random Pattern", width=250)
        self.ClearButton = OptionButton(text="Clear", width=200)
        self.UndoButton = OptionButton(text="Undo", width=200)
        self.SearchButton = OptionButton(text="Search", width=200)
        self.GenerateButton.clicked.connect(self.GenerateButtonClicked)
        self.ClearButton.clicked.connect(self.ClearButtonClicked)
        self.UndoButton.clicked.connect(self.UndoButtonClicked)
        self.SearchButton.clicked.connect(self.SearchButtonClicked)

        #Lables

        self.Density = Lables(text="Density:", width=90)
        self.AlgorithmLable = Lables(text="Algorithm:", width=90)
        self.ColorLabel = Lables(text="Color:", width=90)
        self.AnimationRateLabel = Lables(text="Animation Rate:", width=150)
        self.TimeText = Lables(text="Time Of Execution:", width=150)
        self.HandyStatusLable = Lables(text="Handy Status:", width=150)
        self.NodesText = Lables(text="Opened Node:", width=150)
        self.Time = Lables(text="", width=90)
        self.Nodes = Lables(text="", width=90)

        #Add Widgets
        self.OptionBox.addWidget(self.ColorLabel,0,0)
        self.OptionBox.addWidget(self.ColorCombobox,0,1)
        self.OptionBox.addWidget(self.Density,0,2)
        self.OptionBox.addWidget(self.DensityComboBox,0,3)
        self.OptionBox.addWidget(self.ClearButton, 0, 4)
        self.OptionBox.addWidget(self.AlgorithmLable, 1, 0)
        self.OptionBox.addWidget(self.SearchMethodComboBox, 1,1 )
        self.OptionBox.addWidget(self.AnimationRateLabel, 1,2 )
        self.OptionBox.addWidget(self.AnimationRateComboBox, 1,3 )
        self.OptionBox.addWidget(self.UndoButton,1,4)
        self.OptionBox.addWidget(self.HandyStatusLable, 2, 0)
        self.OptionBox.addWidget(self.HandyComboBox, 2, 1)
        self.OptionBox.addWidget(self.GenerateButton,2,3)
        self.OptionBox.addWidget(self.SearchButton,2,4)
        self.OptionBox.addWidget(self.TimeText,3,1)
        self.OptionBox.addWidget(self.Time, 3, 2)
        self.OptionBox.addWidget(self.NodesText,3,3)
        self.OptionBox.addWidget(self.Nodes,3,4)

        self.vertical.addLayout(self.OptionBox)


    def CreateButtons(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if (row==0 or row==19) or(column==0 or column==29):
                    button = PushButton('', style=self.Styles["Black"],row=row,column=column, color="black")
                    self.layout.addWidget(button,row + 1, column)
                else:
                    button = PushButton('', style=self.Styles["White"],row=row,column=column, color="white")
                    self.Buttons[row][column]=button
                    button.clicked.connect(self.PatternsButtonClicked)
                    button.setEnabled(False)
                    self.layout.addWidget(button,row+1,column)

    def PatternsButtonClicked(self):
        sender=self.sender()
        if self.ColorCombobox.currentText()=="Green":
            if self.Green!=None:
                ColorizeButton(self.Green,"White")
                self.Green.color="white"
            if sender==self.Red:
                self.Red=None
                self.redpositions = [0, 0]
            self.greenpositions = sender.InfoArray[:2]
            sender.color = "green"
            self.Green=sender

        elif self.ColorCombobox.currentText()=="Red":
            if self.Red!=None:
                ColorizeButton(self.Red, "White")
                self.Red.color="white"
            if sender==self.Green:
                self.Green=None
                self.greenpositions = [0, 0]
            self.redpositions = sender.InfoArray[:2]
            sender.color = "red"
            self.Red = sender


        elif self.ColorCombobox.currentText()=="Black":
            sender.color = "black"
            if sender==self.Red:
                self.Red=None
                self.redpositions = [0, 0]

            if sender==self.Green:
                self.Red=None
                self.greenpositions = [0, 0]
        elif self.ColorCombobox.currentText()=="White":
            sender.color = "white"
            if sender==self.Red:
                self.Red=None
                self.redpositions = [0, 0]

            if sender==self.Green:
                self.Green=None
                self.greenpositions = [0, 0]

        ColorizeButton(sender,self.ColorCombobox.currentText())

    def GenerateButtonClicked(self):
        self.ClearButtonClicked()
        for i in self.Buttons:
            for j in i:
                if j!=0:
                    Num=GetRandNumber(int(self.DensityComboBox.currentText()))
                    if Num==0:
                        j.color="white"
                        ColorizeButton(j, "White")
                    elif Num==1:
                        j.color="black"
                        ColorizeButton(j, "Black")
                    j.setEnabled(False)

        #Goal Position
        self.greenpositions[0]=random.randint(1,18)
        self.greenpositions[1]=random.randint(1,28)

        #Primary Location
        self.redpositions[0]=random.randint(1,18)
        self.redpositions[1]=random.randint(1,28)
        while (self.redpositions[0]==self.greenpositions[0]) and (self.redpositions[1]==self.greenpositions[1]):
            self.redpositions[0]=random.randint(1,18)
            self.redpositions[1]=random.randint(1,28)


        if self.Red!=None:
            self.Red.color= "white"
            ColorizeButton(self.Red,"White")
        if self.Green != None:
            self.Green.color="white"
            ColorizeButton(self.Green,"White")

        self.Red=self.Buttons[self.redpositions[0]][self.redpositions[1]]
        self.Green=self.Buttons[self.greenpositions[0]][self.greenpositions[1]]
        ColorizeButton(self.Green,"Green")
        self.Green.color="green"
        ColorizeButton(self.Red,"Red")
        self.Red.color="red"


    def HandyHandeling(self):
        if self.HandyComboBox.currentText()=="Handy":
            self.ColorCombobox.setEnabled(True)
            for i in self.Buttons:
                for j in i:
                    if j != 0:
                        j.setEnabled(True)
        elif self.HandyComboBox.currentText()=="UnHandy":
            self.ColorCombobox.setEnabled(False)
            for i in self.Buttons:
                for j in i:
                    if j != 0:
                        j.setEnabled(False)

    def ClearButtonClicked(self):
        self.HandyComboBox.setCurrentText("UnHandy")
        self.SearchButton.setEnabled(True)
        for i in self.Buttons:
            for j in i:
                if j!=0:
                    ColorizeButton(j,"White")
                    j.status=""
                    j.color=""
                    j.setText("")
                    j.InfoArray[2]=From.nonvisited
        w.Nodes.setText("")
        w.Time.setText("")
        self.NodeCount = 0
        self.Red = None
        self.Green = None

    def UndoButtonClicked(self):
        self.HandyComboBox.setCurrentText("UnHandy")
        self.ColorCombobox.setEnabled(False)
        self.SearchButton.setEnabled(True)
        for i in self.Buttons:
            for j in i:
                if j!=0:
                    if j.styleSheet()==self.Styles["Pink"] or j.styleSheet()==self.Styles["Light Green"]:
                        ColorizeButton(j,"White")
                        j.setText("")
                    j.status = ""
                    j.InfoArray[2]=From.nonvisited


        w.Nodes.setText("")
        w.Time.setText("")
        self.NodeCount = 0

    def SearchButtonClicked(self):
        if self.Red==None or self.Green==None:
            self.MB.setText("You forgot to specify the origin or the destination.")
            self.MB.show()
        else:
            self.UndoButtonClicked()
            self.UndoButton.setEnabled(False)
            self.ClearButton.setEnabled(False)
            self.SearchButton.setEnabled(False)
            self.GenerateButton.setEnabled(False)
            if self.SearchMethodComboBox.currentText()=="DFS":
                t1=time.time()
                result=self.Researcher.DFS(self.redpositions,self.greenpositions)
                self.HandyComboBox.setCurrentText("UnHandy")

                t2 = time.time()
                TimeResult = int((t2 - t1) * 1000)
                self.Time.setText(str(TimeResult) + " ms")
                self.Nodes.setText(str(self.NodeCount))
                if result==None:
                    self.MB.setText("Couldn't Find Path.")
                    self.MB.show()

                ShowPath()





            elif self.SearchMethodComboBox.currentText()=="BFS":
                t1 = time.time()
                result=self.Researcher.BFS(self.redpositions,self.greenpositions)
                self.HandyComboBox.setCurrentText("UnHandy")
                t2 = time.time()
                TimeResult = int((t2 - t1) * 1000)
                self.Time.setText(str(TimeResult) + " ms")
                self.Nodes.setText(str(self.NodeCount))

                ShowPath()

                if result==False:
                    self.MB.setText("Couldn't Find Path.")
                    self.MB.show()

            else:
                t1 = time.time()

                result=self.Researcher.AStar(self.redpositions,self.greenpositions)

                self.HandyComboBox.setCurrentText("UnHandy")


                t2 = time.time()
                TimeResult = int((t2 - t1) * 1000)
                self.Time.setText(str(TimeResult) + " ms")
                self.Nodes.setText(str(self.NodeCount))

                #Show Message Box
                if result==False:
                    self.MB.setText("Couldn't Find Path.")
                    self.MB.show()


                #Colorize Path
                else:
                    ShowPath()
        self.UndoButton.setEnabled(True)
        self.ClearButton.setEnabled(True)
        self.SearchButton.setEnabled(True)
        self.GenerateButton.setEnabled(True)


def ShowPath():
    index = w.Researcher.stack.Size()
    for i in range(index):
        popObj = w.Researcher.stack.Pop()
        if isinstance(popObj,list):
            ColorizeButton(popObj[:2], "Light Green")
            FindButton(popObj[:2]).setText(str(i + 1))
            sleep_program()
        else:
            ColorizeButton(popObj, "Light Green")
            popObj.setText(str(i + 1))
            sleep_program()


def GetRandNumber(Degre):
    Num = random.randint(0,10)
    if Num<=10-Degre:
        return 0
    else:
        return 1

def sleep_program():
    ComboboxTxt=w.AnimationRateComboBox.currentText()
    if ComboboxTxt=="Without Animation":
        pass
    else:
        loop=QEventLoop()
        QTimer.singleShot(int(ComboboxTxt),loop.quit)
        loop.exec_()

def FindNeighbor(Current,Mode):
    if Mode=="With From":
        up = [Current[0] - 1, Current[1],From.bottom]
        right = [Current[0], Current[1] + 1,From.left]
        bottom = [Current[0] + 1, Current[1],From.up]
        left = [Current[0], Current[1] - 1,From.right]
    elif Mode=="Without From":
        up = [Current[0] - 1, Current[1]]
        right = [Current[0], Current[1] + 1]
        bottom = [Current[0] + 1, Current[1]]
        left = [Current[0], Current[1] - 1]

    List = [up, right, bottom, left]

    return List

def FindButton(Possition):
    return w.Buttons[Possition[0]][Possition[1]]

def ColorizeButton(button,color):
    if isinstance(button,list):
        FindButton(button).setStyleSheet(w.Styles[color])
    else:
        button.setStyleSheet(w.Styles[color])


app = QApplication(sys.argv)
w = MyWindow()
w.setWindowTitle('Searchs Algorithm')
w.show()
sys.exit(app.exec_())