import json

adjacencyListRoute = "../dto/lima_adjacency_list.json"
streetsRoute = "../dto/lima_streets.json"
intersectionsRoute = "../dto/intersections.json"


class cityGraph:
    def __init__(self, adjacencyListRoute, streetsRoute, intersectionsRoute):
        self.adjacencyList = {}
        self.streets = {}
        self.intersections = {}

        self.init_graph(adjacencyListRoute, streetsRoute, intersectionsRoute)

    def init_graph(self, adjacencyListRoute, streetsRoute, intersectionsRoute):
        with open(adjacencyListRoute, mode="r", encoding="utf-8") as f:
            self.adjacencyList = json.load(f)

        with open(streetsRoute, mode="r", encoding="utf-8") as f:
            _streets = json.load(f)
            for e in _streets:
                k, v = e
                key = tuple(e[k])
                value = e[v]

                self.streets[key] = value
        with open(intersectionsRoute, mode="r", encoding="utf-8") as f:
            self.intersections = json.load(f)