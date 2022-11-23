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


graph = initGraph("../dto/lima_district_streets.json")

with open("lima_adjacency_list.json", mode="w", encoding="utf-8") as f:
    adjacencyList = json.dumps(graph.adjacencyList)
    f.write(adjacencyList)

# Extract edges from the district of Lima


def map_edges_keys(edges):
    return [{"key": k, "value": v} for k, v in edges.items()]


with open("lima_streets.json", mode="w", encoding="utf-8") as f:
    lima_streets = json.dumps(map_edges_keys(graph.edges))
    f.write(lima_streets)

# Extract intersectuibs from the district of Lima

with open("intersections.json", mode="w", encoding="utf-8") as f:
    intersection = json.dumps(graph.nodes)
    f.write(intersection)
