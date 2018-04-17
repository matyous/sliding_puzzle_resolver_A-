"""
Author: Mohamed Amine TURKI

Computer Science Engineering Student at National School of Coputer Science (ENSI), Artificial Intelligence Sector

April 2018
"""

from GameMatrice import *

directions = ['high', 'low', 'right', 'left']

root = GameMatrice(matrice=generateGame())
print(root.print())
fileA = [[root]]
killer = 0

while (fileA[0][-1].matrice != target) & (killer < 2000):

    killer = killer + 1
    for d in directions:

        childMatrice = fileA[0][-1].child_birth(d)

        if childMatrice is not None:
            child = GameMatrice(matrice=childMatrice, parent=fileA[0][-1].matrice, parentG=fileA[0][-1].G)
            fileA = fileA + [fileA[0] + [child]]

    fileA.pop(0)
    drop_duplicates(fileA)
    fileA.sort(key=lambda chemain: chemain[-1].F)
if fileA[0][-1].matrice == target:
    print("result found \n ")

    for element in fileA[0]:
        print(element.print())

else:
    print("result not found!")
