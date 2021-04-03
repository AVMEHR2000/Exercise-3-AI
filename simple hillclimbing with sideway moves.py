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

#simple hill climbing with sideway moves search
#this initioal state is optional
initionalState = State_chess_board([[0,0],[2,1],[5,2],[0,3],[0,4],[1,5],[2,6],[1,7],[1,0],[1,1]])
currentState=initionalState
for counter in range(1,2000):
    numberOfBioshop=random.randint(0,9)
    selectedBioShop=currentState.BioshopsLists[numberOfBioshop]
    #creat neighbers
    rightNeighberOfState=copy.deepcopy(currentState)
    leftNeighberOfState=copy.deepcopy(currentState)
    upNeighberOfState=copy.deepcopy(currentState)
    downNeighberOfState=copy.deepcopy(currentState)
    listOfNeighbors=list()
    if(0<=selectedBioShop[1]+1<8):
        rightNeighberOfState.BioshopsLists[numberOfBioshop][1]+=1
        listOfNeighbors.append(rightNeighberOfState)
    if (0 <= selectedBioShop[1] - 1 < 8):
        leftNeighberOfState.BioshopsLists[numberOfBioshop][1] -= 1
        listOfNeighbors.append(leftNeighberOfState)
    if (0 <= selectedBioShop[0] + 1 < 8):
        upNeighberOfState.BioshopsLists[numberOfBioshop][0] += 1
        listOfNeighbors.append(upNeighberOfState)
    if (0 <= selectedBioShop[0] - 1 < 8):
        downNeighberOfState.BioshopsLists[numberOfBioshop][0] -= 1
        listOfNeighbors.append(downNeighberOfState)
    #sort list of neighbers according to the cost function
    listOfNeighbors.sort(key= lambda x:x.cost(),reverse=True)
    #diffrence point in if statement(>=)
    if(listOfNeighbors[0].cost()>=currentState.cost()):
        currentState=copy.deepcopy(listOfNeighbors[0])
print(currentState.cost())