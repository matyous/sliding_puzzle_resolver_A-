from Functions import *
import copy
import random


def generateGame():

    generatedList = random.sample(range(9), 9)
    i = 0
    matrice = {1: {1: 1, 2: 2, 3: 3}, 2: {1: 8, 2: 0, 3: 4}, 3: {1: 7, 2: 6, 3: 5}}
    for j in [1, 2, 3]:
        for k in [1, 2, 3]:
            matrice[j][k] = generatedList[i]
            i = i + 1
    return matrice


class GameMatrice:
    def __init__(self, matrice={1: {1: 2, 2: 8, 3: 3}, 2: {1: 1, 2: 6, 3: 4}, 3: {1: 7, 2: 0, 3: 5}},
                 parent={}, parentG=-1):

        self.matrice = matrice
        self.parent = parent
        self.G = parentG + 1
        self.F = self.G + H(self.matrice)

    def child_birth(self, direction):
        """

        :param direction: the direction in witch we ask the blank box (zero) to move
        :return: return the new gameBoard if the action is possible and a None else
        """
        [i_pos, j_pos] = findZero(self.matrice)

        if (self.matrice[i_pos][j_pos] == 0) & (self.matrice != target):

            child = copy.deepcopy(self.matrice)

            if (direction == 'high') & (i_pos > 1):
                child[i_pos][j_pos] = self.matrice[i_pos - 1][j_pos]
                child[i_pos - 1][j_pos] = 0

                if self.parent != child:
                    return child
                else:
                    return None

            elif (direction == 'low') & (i_pos < 3):
                child[i_pos][j_pos] = self.matrice[i_pos + 1][j_pos]
                child[i_pos + 1][j_pos] = 0

                if self.parent != child:
                    return child
                else:
                    return None

            elif (direction == 'right') & (j_pos > 1):
                child[i_pos][j_pos] = self.matrice[i_pos][j_pos - 1]
                child[i_pos][j_pos - 1] = 0

                if self.parent != child:
                    return child
                else:
                    return None

            elif (direction == 'left') & (j_pos < 3):
                child[i_pos][j_pos] = self.matrice[i_pos][j_pos + 1]
                child[i_pos][j_pos + 1] = 0

                if self.parent != child:
                    return child
                else:
                    return None

            else:
                return None

        else:
            return None

        return None

    def print(self):
        """

        :return: a string showing the state of the game Board
        """
        retour = ""
        for i in range(1, 4):
            retour = retour + "\n" + str(self.matrice[i][1]) + " " + str(self.matrice[i][2]) + " " + \
                     str(self.matrice[i][3])

        return retour
