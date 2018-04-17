from GameMatrice import *

target = {1: {1: 1, 2: 2, 3: 3}, 2: {1: 8, 2: 0, 3: 4}, 3: {1: 7, 2: 6, 3: 5}}


def findZero(matrice):
    """

    :param matrice: a gameboard matrix
    :return: the indexes of the blank box (zero)
    """
    for i in range(1, 4):
        for j in range(1, 4):
            if matrice[i][j] == 0:
                return [i, j]

    return []


def H(gameBoard):
    """

    :param gameBoard: the gameboard
    :return: reserch heuristic, it helps our algorithm find the solution faster (number of missplased cases)
    """
    heuristique = 0

    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            if gameBoard[i][j] != target[i][j]:
                heuristique += 1

    return heuristique


def A_etoile(file=[]):
    """

    :param file: a list containing the solution paths
    :return: the same list after treating it with A* algorithm
    """
    s0 = file[0][-1]
    print(s0.print())
    for i in range(10):

        s0.child_birth()

        for child in s0.children:
            file.append(file[0] + [child])

        file.pop(0)
#        file = A_etoile_cleaner(file)
        s0 = file[0][-1]

    return file


def drop_duplicates(tosort_list=[[]]):
    """

    :param tosort_list: list of paths to drop duplicated from based on the last element of each path
    :return: the unique elements list
    """
    sorted_list = [tosort_list[0]]

    for i in range(1, len(tosort_list)):
        if tosort_list[i][-1].matrice is not tosort_list[i-1][-1].matrice:
            sorted_list = sorted_list + [tosort_list[i]]

    return sorted_list
