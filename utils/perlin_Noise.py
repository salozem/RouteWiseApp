import json
import math
from graph_lima import cityGraph
from perlin_noise import PerlinNoise


def generate_perlin_noise(n):
    noise = PerlinNoise(octaves=5, seed=1563)
    xpix, ypix = n*5, 1
    per_noise = [[noise([i/xpix, j/ypix]) for i in range(xpix)]
                 for j in range(ypix)]
    values = []
    min_i = math.inf
    max_i = -math.inf

    for v in per_noise:
        for e in v:
            e = int(e*100)
            min_i = min(min_i, e)
            max_i = max(max_i, e)
            values.append(e)

    if min_i < 0:
        values = list(map(lambda x: x+abs(min_i), values))

    d = max_i - min_i
    converter = d / 50
    values = list(map(lambda x: int(x / converter), values))
    return values


def bfs(graph: cityGraph, perNoise):
    seen = {}
    for k, v in graph.adjacencyList.items():
        for e in v:
            seen[(k, e)] = False

    indexPer = 0

    def bfsUtil(node):
        nonlocal indexPer

        queue = []

        queue.append(node)
        seen[node] = True

        while queue:
            current_node = queue.pop(0)
            for child_node in graph.adjacencyList[str(current_node)]:
                if not seen[str(current_node), child_node]:
                    seen[(str(current_node), child_node)] = True
                    queue.append(child_node)

                    graph.streets[(int(current_node), int(child_node))].update(
                        {"val": perNoise[indexPer]})

                    indexPer += 1

    for k, v in graph.adjacencyList.items():
        for e in v:
            if not seen[(k, e)]:
                bfsUtil(k)


adjacencyListRoute = "../dto/lima_adjacency_list.json"
streetsRoute = "../dto/lima_streets.json"
intersectionsRoute = "../dto/intersections.json"

cityGraph = cityGraph(adjacencyListRoute=adjacencyListRoute,
                      streetsRoute=streetsRoute, intersectionsRoute=intersectionsRoute)
perNoise = generate_perlin_noise(len(cityGraph.streets))

bfs(cityGraph, perNoise)

flag = True
for v in cityGraph.streets.values():
    try:
        if v["val"] is not None:
            break
    except:
        isSuccess = False
        continue


def remap_keys(edges):
    return [{"key": k, "value": v} for k, v in edges.items()]


if flag:
    with open("lima_streets.json", mode="w", encoding="utf-8") as f:
        lima_streets = json.dumps(remap_keys(cityGraph.streets))
        f.write(lima_streets)

else:
    print("Failed generation")