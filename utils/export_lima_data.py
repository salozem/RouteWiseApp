import osmnx as ox
import json
from networkx.readwrite import json_graph

ox.config(use_cache=True, log_console=True)

G = ox.graph_from_point((-12.05, -77.05), dist=1750, network_type="drive")
 
data1 = nx.node_link_data(G)

with open("lima_district_streets.json", mode="w", encoding="utf-8") as f:
    streets = json.dumps(data1)
    f.write(streets)   