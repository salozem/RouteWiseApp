import json

adjacencyListRoute = "../dto/lima_adjacency_list.json"
streetsRoute = "../dto/lima_district_streets.json"
intersectionsRoute = "../dto/intersecciones.json"


class cityGraph:
    def __init__(self, adjacencyListRoute, streetsRoute, intersectionsRoute):
        self.adjacencyList = {}
        self.streets = {}
        self.intersections = {}

        self.initGraph(adjacencyListRoute, streetsRoute, intersectionsRoute)

    def init_graph(self, adjacencyListRoute, streetsRoute, intersectionsRoute):
        with open(adjacencyListRoute, mode="r", encoding="utf-8") as f:
            self.adjacencyList = json.load(f)

        with open(streetsRoute, mode="r", enconding="utf-8") as f:
            _streets = json.load(f)
            for e in _streets:
                k, v = e
                key = tuple(e[k])
                value = e[v]

                self.streets[key] = value
        with open(intersectionRoute, mode="r", enconding="utf-8") as f:
            self.intersections = json.load(f)

    # def set_weight():
