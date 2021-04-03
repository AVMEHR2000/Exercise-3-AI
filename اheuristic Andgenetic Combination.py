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
listOfCosts=list()
for i in range(0,8):
    for j in range(0,8):
        listOfCosts.append([i,j])
listOfCosts.sort(key=lambda x: State_chess_board([x]).cost(), reverse=True)
#find how many elements have maximum cost
indexOfMax=0
for i in range(0,63):
    if(listOfCosts[i]==listOfCosts[0]):
        indexOfMax+=1
    else: break
#find the best chromosome
bestChromosome=list()
for i in range(0,indexOfMax):
    index=0
    bestcost=State_chess_board([listOfCosts[i]]).cost()
    templist=[listOfCosts[i]]
    for bioshops in range(1,10):
        for k in range(i,64):
            templist.append(listOfCosts[k])
            tempState = State_chess_board(templist)
            if(tempState.cost()>=bestcost):
                bestcost=tempState.cost()
                index=copy.deepcopy(k)
            templist.remove(listOfCosts[k])
        templist.append(listOfCosts[index])
    currentState=State_chess_board(templist)
    if (currentState.cost() == 64):
        bestChromosome.append(copy.deepcopy(templist))

for i in range(0,bestChromosome.__len__()):
    solution=State_chess_board(bestChromosome[i])
    solution.ShowChessBoard()
    print(solution.cost())









