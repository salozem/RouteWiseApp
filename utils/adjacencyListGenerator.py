from datetime import datetime
import json
import math

def generateAdjacencyList(listPath, streetPath):
    adjacencyList={}
    current_time=datetime.now().hour
    street={}
    keyValue={}

    def initializeData():
        with open(listPath, mode="r", encoding="utf-8") as f:
            nonlocal adjacencyList
            adjacencyList = json.load(f)
            adjacencyList = [(int(key), value) for key, value in adjacencyList.items()]
            adjacencyList = sorted(adjacencyList, key=lambda x: x[0])

            i = 0
            for key, val in adjacencyList:
                keyValue[key] = i
                i += 1
        
        with open(streetPath, mode="r", encoding="utf-8") as file:
            nonlocal street
            streetList = json.load(file)

            for element in streetList:
                k, v = element

                key = tuple(element[k])
                value = element[v]

                street[key] = value
    
    def trafficHour(time):
        fact = round(5 * math.cos(2 * (time / 3) - 1) * math.sin((time / 6) - 2) +5, 3)
        if fact > 10: return 10
        if fact < 0 : return 0
        return fact

    def calcTrafficFactor(val, time):
        value = val * trafficHour(time)
        return value / 10

    def calcWeight(val , length, time):
        return calcTrafficFactor(val, time) * math.log10(length)
    
    def getWeight(city1, city2):
        str = street[(city1, city2)]
        val = str["val"]
        length = str["length"]
        return calcWeight(val, length, current_time)

    def newAdjacencyList():
        nonlocal adjacencyList
        nonlocal keyValue

        newAdjacencyList = []
        for key, arr in adjacencyList:
            newAdjacencyList.append(list(map(lambda x: (keyValue[x], getWeight(key, x)), arr)))
        return newAdjacencyList

        initializeData()
        return newAdjacencyList()
