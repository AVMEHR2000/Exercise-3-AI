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
def contain(element,listOfElements):
    for item in listOfElements:
        for index in range(0,9):
            if(item.BioshopsLists[index][0]!=element.BioshopsLists[index][0] and item.BioshopsLists[index][0]!=element.BioshopsLists[index][0]):
                solution=False
                return False
    return True
#local beam search algorithm for k=4
listOfStates=list()
listOfStates.append(State_chess_board([[0,0],[5,1],[0,2],[0,3],[0,4],[1,5],[2,6],[0,7],[1,0],[1,1]]))
listOfStates.append(State_chess_board([[0,0],[5,1],[4,2],[0,3],[0,4],[1,5],[2,6],[6,5],[1,0],[2,1]]))
listOfStates.append(State_chess_board([[0,0],[2,1],[5,2],[0,3],[0,4],[1,5],[2,6],[1,7],[1,0],[1,1]]))
listOfStates.append(State_chess_board([[0,0],[0,1],[0,2],[0,3],[3,4],[1,5],[2,6],[0,7],[1,0],[3,1]]))
successors=list()
listOfMaxStates=copy.deepcopy(listOfStates)
for i in range(0,300):
    for state in listOfStates:
        numberOfBioshop = random.randint(0, 9)
        selectedBioShop = state.BioshopsLists[numberOfBioshop]
        rightNeighberOfState = copy.deepcopy(state)
        leftNeighberOfState = copy.deepcopy(state)
        upNeighberOfState = copy.deepcopy(state)
        downNeighberOfState = copy.deepcopy(state)
        if (0 <= selectedBioShop[1] + 1 < 8):
            rightNeighberOfState.BioshopsLists[numberOfBioshop][1] += 1
            if (not contain(rightNeighberOfState, listOfMaxStates)):
                successors.append(rightNeighberOfState)
        if (0 <= selectedBioShop[1] - 1 < 8):
            leftNeighberOfState.BioshopsLists[numberOfBioshop][1] -= 1
            if (not contain(leftNeighberOfState, listOfMaxStates)):
                successors.append(leftNeighberOfState)
        if (0 <= selectedBioShop[0] + 1 < 8):
            upNeighberOfState.BioshopsLists[numberOfBioshop][0] += 1
            if (not contain(upNeighberOfState, listOfMaxStates)):
                successors.append(upNeighberOfState)
        if (0 <= selectedBioShop[0] - 1 < 8):
            downNeighberOfState.BioshopsLists[numberOfBioshop][0] -= 1
            if(not contain(downNeighberOfState,listOfMaxStates)):
                successors.append(downNeighberOfState)
    # sort list of neighbers according to the cost function
    successors.sort(key=lambda x: x.cost(), reverse=True)
    del successors[4:]
    listOfMaxStates.sort(key=lambda x: x.cost(), reverse=True)
    if(len(successors)>0):
        if(successors[0].cost()>listOfMaxStates[0].cost()):
            del listOfMaxStates[:]
            for suc in range(0,3):
                if(successors[suc].cost()==successors[0].cost()):
                    listOfMaxStates.append(successors[suc])
        else:
            for suc in range(0,3):
                if(successors[suc].cost()==successors[0].cost()):
                    listOfMaxStates.append(successors[suc])
        if(successors[0].cost==64):
            print("solution:")
            successors[0].ShowChessBoard()
            break
    listOfStates=copy.deepcopy(successors)
    #print max of costs
for j in range(0,successors.__len__()):
    print(listOfStates[j].cost())
    print()