import math
import copy
import numpy as np
import random
import decimal
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

#simulated annealing algorithm
initionalState = State_chess_board([[0,0],[0,1],[0,2],[0,3],[3,4],[1,5],[2,6],[0,7],[1,0],[3,1]])
currentState=initionalState
resultState = copy.deepcopy(currentState)
temperature=400
sch=0.8
for i in range(0,2000):
    temperature*=sch
    numberOfBioshop = random.randint(0, 9)
    selectedBioShop = currentState.BioshopsLists[numberOfBioshop]
    isRow = random.randint(0, 1)
    jump = random.choice([-1, 1])
    if (isRow == 0):
        if (0 <= selectedBioShop[1] + jump < 8):
            contain = False
            for item in currentState.BioshopsLists:
                if (item[0] == selectedBioShop[0] and item[1] == selectedBioShop[1] + jump):
                    contain = True
            if (not contain):
                currentState.BioshopsLists[numberOfBioshop][1] = selectedBioShop[1] + jump
                #this if statement is diffrent from first choice hill climbing
                dw=currentState.cost()-resultState.cost()
                exp=decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-dw) * decimal.Decimal(temperature)))
                if (dw>0 or random.uniform(0,1)< exp):
                    resultState = copy.deepcopy(currentState)
                else:
                    currentState = copy.deepcopy(resultState)

    else:
        if (0 <= selectedBioShop[0] + jump < 8):
            contain = False
            for item in currentState.BioshopsLists:
                if (item[0] == selectedBioShop[0] + jump and item[1] == selectedBioShop[1]):
                    contain = True
            if (not contain):
                currentState.BioshopsLists[numberOfBioshop][0] = selectedBioShop[0] + jump
                # this if statement is diffrent from first choice hill climbing
                dw = currentState.cost() - resultState.cost()
                exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-dw) * decimal.Decimal(temperature)))
                if (dw>0 or random.uniform(0, 1) < exp):
                    resultState = copy.deepcopy(currentState)
                else:
                    currentState = copy.deepcopy(resultState)
    if(resultState.cost()==64):
        break

print(resultState.cost())