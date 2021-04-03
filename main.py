import math
import copy
import numpy as np
import random


class State_chess_board:
    def __init__(self,BioShopList):
        self.BioshopsLists=np.array(BioShopList)
    def ShowChessBoard(self):
        EmptyState = np.zeros((8, 8))
        for i in self.BioshopsLists:
            EmptyState[i[0]][i[1]]=1
        print(EmptyState)
    def cost(self):
        self.treatenCell=list()
        for bioshop in self.BioshopsLists :
            for i in range(-8,8):
                if(-1<bioshop[0]+i<8 and -1<bioshop[1]+i<8 and i !=0):
                    if (not [bioshop[0] + i, bioshop[1] + i] in self.treatenCell):
                        self.treatenCell.append([bioshop[0]+i,bioshop[1]+i])
                if (-1 < bioshop[0] - i < 8 and -1 < bioshop[1] + i < 8 and i != 0):
                    if(not [bioshop[0] - i, bioshop[1] + i] in self.treatenCell ):
                        self.treatenCell.append([bioshop[0] - i, bioshop[1] + i])
        return len(self.treatenCell)











# creat initioal state
initionalState = State_chess_board([[0,0],[0,1],[0,2],[0,3],[3,4],[1,5],[2,6],[0,7],[1,0],[3,1]])
currentState=initionalState
#first choice hill climbing algorithm
resultState = copy.deepcopy(currentState)
for counter in range(1,2000):
    numberOfBioshop=random.randint(0,9)
    selectedBioShop=currentState.BioshopsLists[numberOfBioshop]
    #creat neighbor and compare with current cost
    isRow=random.randint(0,1)
    jump = random.choice([-1, 1])
    if(isRow==0):
        if(0<=selectedBioShop[1]+jump<8):
            contain=False
            for item in currentState.BioshopsLists:
                if(item[0] == selectedBioShop[0] and item[1] ==selectedBioShop[1]+jump ):
                    contain=True
            if( not contain):
                currentState.BioshopsLists[numberOfBioshop][1]=selectedBioShop[1]+jump
                if(currentState.cost()>=resultState.cost()):
                    resultState = copy.deepcopy(currentState)
                else:
                    currentState=copy.deepcopy(resultState)

    else:
        if (0 <= selectedBioShop[0] + jump < 8):
            contain = False
            for item in currentState.BioshopsLists:
                if (item[0] == selectedBioShop[0]+jump and item[1] == selectedBioShop[1] ):
                    contain = True
            if ( not contain):
                currentState.BioshopsLists[numberOfBioshop][0]=selectedBioShop[0]+jump
                if (currentState.cost() >= resultState.cost()):
                    resultState = copy.deepcopy(currentState)
                else:
                    currentState=copy.deepcopy(resultState)

print(resultState.cost())



