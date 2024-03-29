

def max_pressure(valves, start, time_limit):
    pipes = valves[start]
    print(pipes)

    # for pipe in pipes: 
        # max_pressure(pipe

    pass


valves = {
     "EJ": (25, ["MC"]),
     "WC": (0, ["OW", "RU"]),
     "NP": (0, ["VR", "KL"]),
     "AA": (0, ["QT", "AP", "EZ", "AK", "XV"]),
     "VO": (6, ["KM", "RF", "HS", "LJ", "IA"]),
     "CB": (0, ["UI", "UP"]),
     "TE": (18, ["JT"]),
     "CZ": (0, ["UP", "OW"]),
     "LJ": (0, ["DV", "VO"]),
     "UP": (7, ["SK", "CB", "CZ"]),
     "FP": (0, ["OW", "RE"]),
     "KM": (0, ["SE", "VO"]),
     "DV": (0, ["LJ", "UM"]),
     "FL": (0, ["AH", "TS"]),
     "VR": (24, ["DM", "TF", "NP"]),
     "IA": (0, ["VS", "VO"]),
     "RF": (0, ["VO", "JF"]),
     "RT": (0, ["UM", "SE"]),
     "RU": (0, ["AR", "WC"]),
     "SE": (4, ["GU", "KM", "CX", "RT"]),
     "MC": (0, ["EJ", "AR"]),
     "TF": (0, ["AH", "VR"]),
     "CX": (0, ["SE", "TO"]),
     "GL": (11, ["UY", "KL", "CY"]),
     "GU": (0, ["SE", "EZ"]),
     "VS": (0, ["XN", "IA"]),
     "EZ": (0, ["AA", "GU"]),
     "GK": (0, ["FI", "HZ"]),
     "JT": (0, ["TE", "XN"]),
     "DM": (0, ["VR", "HZ"]),
     "AR": (16, ["UI", "RU", "MC"]),
     "XN": (9, ["XP", "JT", "VS", "GT", "CY"]),
     "CY": (0, ["XN", "GL"]),
     "QT": (0, ["UM", "AA"]),
     "KL": (0, ["GL", "NP"]),
     "SK": (0, ["XV", "UP"]),
     "OW": (12, ["CZ", "WC", "FP"]),
     "AK": (0, ["AA", "HS"]),
     "XV": (0, ["AA", "SK"]),
     "GT": (0, ["XN", "UM"]),
     "FI": (0, ["JF", "GK"]),
     "UY": (0, ["JF", "GL"]),
     "UM": (5, ["DV", "GT", "RT", "QT"]),
     "IQ": (0, ["HZ", "AH"]),
     "JF": (10, ["RF", "FI", "UY", "RE", "TS"]),
     "TS": (0, ["JF", "FL"]),
     "AH": (23, ["IQ", "FL", "TF"]),
     "HS": (0, ["AK", "VO"]),
     "HZ": (20, ["IQ", "DM", "GK"]),
     "TO": (15, ["CX"]),
     "XP": (0, ["AP", "XN"]),
     "AP": (0, ["XP", "AA"]),
     "RE": (0, ["JF", "FP"]),
     "UI": (0, ["AR", "CB"])
}


# valves = {
#     'AA': (0, ['DD', 'II', 'BB']),
#     'BB': (13, ['CC', 'AA']),
#     'CC': (2, ['DD', 'BB']),
#     'DD': (20, ['CC', 'AA', 'EE']),
#     'EE': (3, ['FF', 'DD']),
#     'FF': (0, ['EE', 'GG']),
#     'GG': (0, ['FF', 'HH']),
#     'HH': (22, ['GG']),
#     'II': (0, ['AA', 'JJ']),
#     'JJ': (21, ['II'])
# }
#
print(max_pressure(valves, 'AA', 30))


import networkx as nx
import matplotlib.pyplot as plt

# Create a new directed graph
G = nx.DiGraph()

# Add nodes with their attributes
for valve in valves.keys():
    print(valve)
    G.add_node(valve, flow_rate=0)


# Add edges
for key, item in valves.items():
    x, y = item
    for cc in y:
        G.add_edge(key, cc)


# Draw the graph
pos = nx.spring_layout(G)
labels = nx.get_node_attributes(G, 'flow_rate')
nx.draw(G, pos, with_labels=True, arrows=True)
nx.draw_networkx_edge_labels(G, pos)
nx.draw_networkx_labels(G, pos, labels)
plt.show()


# valves = {
#     "EJ": (25, ["MC"]),
#     "WC": (0, ["OW", "RU"]),
#     "NP": (0, ["VR", "KL"]),
#     "AA": (0, ["QT", "AP", "EZ", "AK", "XV"]),
#     "VO": (6, ["KM", "RF", "HS", "LJ", "IA"]),
#     "CB": (0, ["UI", "UP"]),
#     "TE": (18, ["JT"]),
#     "CZ": (0, ["UP", "OW"]),
#     "LJ": (0, ["DV", "VO"]),
#     "UP": (7, ["SK", "CB", "CZ"]),
#     "FP": (0, ["OW", "RE"]),
#     "KM": (0, ["SE", "VO"]),
#     "DV": (0, ["LJ", "UM"]),
#     "FL": (0, ["AH", "TS"]),
#     "VR": (24, ["DM", "TF", "NP"]),
#     "IA": (0, ["VS", "VO"]),
#     "RF": (0, ["VO", "JF"]),
#     "RT": (0, ["UM", "SE"]),
#     "RU": (0, ["AR", "WC"]),
#     "SE": (4, ["GU", "KM", "CX", "RT"]),
#     "MC": (0, ["EJ", "AR"]),
#     "TF": (0, ["AH", "VR"]),
#     "CX": (0, ["SE", "TO"]),
#     "GL": (11, ["UY", "KL", "CY"]),
#     "GU": (0, ["SE", "EZ"]),
#     "VS": (0, ["XN", "IA"]),
#     "EZ": (0, ["AA", "GU"]),
#     "GK": (0, ["FI", "HZ"]),
#     "JT": (0, ["TE", "XN"]),
#     "DM": (0, ["VR", "HZ"]),
#     "AR": (16, ["UI", "RU", "MC"]),
#     "XN": (9, ["XP", "JT", "VS", "GT", "CY"]),
#     "CY": (0, ["XN", "GL"]),
#     "QT": (0, ["UM", "AA"]),
#     "KL": (0, ["GL", "NP"]),
#     "SK": (0, ["XV", "UP"]),
#     "OW": (12, ["CZ", "WC", "FP"]),
#     "AK": (0, ["AA", "HS"]),
#     "XV": (0, ["AA", "SK"]),
#     "GT": (0, ["XN", "UM"]),
#     "FI": (0, ["JF", "GK"]),
#     "UY": (0, ["JF", "GL"]),
#     "UM": (5, ["DV", "GT", "RT", "QT"]),
#     "IQ": (0, ["HZ", "AH"]),
#     "JF": (10, ["RF", "FI", "UY", "RE", "TS"]),
#     "TS": (0, ["JF", "FL"]),
#     "AH": (23, ["IQ", "FL", "TF"]),
#     "HS": (0, ["AK", "VO"]),
#     "HZ": (20, ["IQ", "DM", "GK"]),
#     "TO": (15, ["CX"]),
#     "XP": (0, ["AP", "XN"]),
#     "AP": (0, ["XP", "AA"]),
#    "RE": (0, ["JF", "FP"]),
#     "UI": (0, ["AR", "CB"])
# }
#
