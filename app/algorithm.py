import json
import random as r
import math
import heapq as hq
from perlin_noise import PerlinNoise


def transform_city_graph():
    adjacencyList= "../dto/lima_adjacency_list.json"
    street = "../dto/lima_district_streets.json"
    intersections = "../dto/intersecciones.json"
    return G, Loc

G, Loc= transform_city_graph()


def bfs(G, s):
    n = len(G)
    visited = [False]*n
    path = [-1]*n  # parent
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for v, _ in G[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u
                queue.append(v)

    return path


def dfs(G, s, t):
    n = len(G)
    path = [-1]*n
    visited = [False]*n

    stack = [s]
    while stack:
        u = stack.pop()
        visited[u] = True
        if u == t:
            break
        for v, _ in G[u]:
            if not visited[v]:
                path[v] = u
                stack.append(v)

    return path


def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    cost = [math.inf]*n

    cost[s] = 0
    pqueue = [(0, s)]
    while pqueue:
        g, u = hq.heappop(pqueue)
        if not visited[u]:
            visited[u] = True
            for v, w in G[u]:
                if not visited[v]:
                    f = g + w
                    if f < cost[v]:
                        cost[v] = f
                        path[v] = u
                        hq.heappush(pqueue, (f, v))

    return path, cost


def graph():
    return json.dumps({"loc": Loc, "g": G})


def paths(s, t):
    bestpath, _ = dijkstra(G, s)
    path1 = bfs(G, s)
    path2 = dfs(G, s, t)

    return json.dumps({"bestpath": bestpath, "path1": path1, "path2": path2})
