
# metrik: mm
# Schräge Mauern!
# Stockwerke: Gleiches Prinzip, können komplett unterschiedlich sein
# Treppen
# Verschiedene Muster

# Eigene Metrik; Links oben 0: 0; rechts unten x:x

import json


def draw(walls):
    stringList = []
    for y in range(0, 10000, 500):

        xString = ""
        for x in range(0, 10000, 500):
            wallFound = False
            for wall in walls:
                xStart = int(wall["start"]["coordinates"]["x"])
                xEnd = int(wall["end"]["coordinates"]["x"])
                yStart = int(wall["start"]["coordinates"]["y"])
                yEnd = int(wall["end"]["coordinates"]["y"])

                #
                isHorizontalWall = yStart == yEnd
                isVerticalWall = xStart == xEnd
                if (isHorizontalWall):
                    wallOnYLevel = y == yStart
                    if (wallOnYLevel and x in range(xStart, xEnd)):
                        xString = xString + "_"
                        wallFound = True
                elif (isVerticalWall):
                    wallOnXLevel = x == xStart
                    if (wallOnXLevel and y in range(yStart, yEnd)):
                        xString = xString + "|"
                        wallFound = True

            if (wallFound == False):
                xString = xString + " "

        stringList.append(xString)

    for string in stringList:
        print(string)


file = open('data-models/layout.json')
data = json.load(file)

draw(data["layout"]["walls"])

file.close
