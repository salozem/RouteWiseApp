import geojson
import json


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = self.processNodes(nodes)
        self.edges, self.adjacencyList = self.processEdges(edges)

    def processNodes(self, nodes):
        mapOfNodes = {}
        for node in nodes:
            mapOfNodes[node["id"]] = node
        return mapOfNodes

    def processEdges(self, egdes):
        mapOfEdges = {}
        adjacencyList = {}

        for edge in egdes:
            source = edge["source"]
            target = edge["target"]

            mapOfEdges[(source, target)] = edge

            if adjacencyList.get(source) is None:
                adjacencyList[source] = []
            if adjacencyList.get(target) is None:
                adjacencyList[target] = []

            adjacencyList[source].append(target)

        return mapOfEdges, adjacencyList


def initGraph(documentPath):
    with open(documentPath, mode="r", encoding="utf-8") as f:
        data = geojson.load(f)

    graph = Graph(data["nodes"], data["links"])
    return graph


graph = initGraph("dto/lima_district_streets.json")
