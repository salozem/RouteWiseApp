import json
import math
import heapq as hq
import sys
import os
sys.path.append(os.path.abspath("../utils"))
from adjacencyListGenerator import generateAdjacencyList, generateListForUI


def transform_city_graph():
    adjacencyList = "../dto/lima_adjacency_list.json"
    street = "../dto/lima_streets.json"
    intersections = "../dto/intersections.json"
    G = generateAdjacencyList(adjacencyList, street)
    Loc = generateListForUI(intersections)
    return G, Loc




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


def dijkstra(G, s, t):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    cost = [math.inf]*n

    top = 0
    posh = [0, 0]
    cost[s] = 0
    pq = [(0, s)]

    while pq:
        cdis, ci = hq.heappop(pq)
        if not visited[ci]:
            visited[ci] = True
            for v, w in G[ci]:
                if not visited[v]:
                    d = cdis + w
                    if d < cost[v]:
                        cost[v] = d
                        path[v] = ci
                        hq.heappush(pq, (d, v))

    head = t
    while path[head] != -1:
        for n, w in G[head]:
            if w > top:
                top = w
                posh = [v, head]
        head = path[head]

    return path, cost, posh

G, Loc = transform_city_graph()

def graph():
    return json.dumps({"loc": Loc, "g": G})


def paths(s, t):
    bestpath, _, h = dijkstra(G, s, t)
    path1 = bfs(G, s)
    path2 = dfs(G, s, t)

    return json.dumps({"bestpath": bestpath, "path1": path1, "path2": path2})
