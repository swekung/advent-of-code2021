from typing import Counter
import numpy as np
import sys
import time
import networkx as nx
start_time = time.time()

def readFile(file):
    text = open(file)
    out = []
    for line in text:
        out.append(list(line.rstrip('\n')))
    text.close()
    out = np.array(out, dtype=np.int16)
    out = np.pad(out, 1, 'constant', constant_values=9)
    return out

def toNetwork(map):
    G = nx.Graph()
    for i in range(1,len(map)-1):
        for j in range(1,len(map[i])-1):
            G.add_node(i*(len(map[i]))+j)
    for i in range(1,len(map)-1):
        for j in range(1,len(map[i])-1):
            G.add_edge(i*len(map[i])+j, (i-1)*len(map[i])+j, weight=map[i-1][j])
            G.add_edge(i*len(map[i])+j, (i+1)*len(map[i])+j, weight=map[i+1][j])
            G.add_edge(i*len(map[i])+j, i*len(map[i])+j+1, weight=map[i][j+1])
            G.add_edge(i*len(map[i])+j, i*len(map[i])+j-1, weight=map[i][j-1])
    return G
    

def solve(map, start, visited):
    risk = 0
    mapSize = [len(map) - 1, len(map[0]) - 1]
    while not start == mapSize:
        next = lowestNeigh
    return start

def lowestNeigh(map, start, visited):
    min = 9
    coord = []
    pattern = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for pat in pattern:
        tmp = [start[0] - pat[0], start[1] - pat[1]]
        if tmp in visited:
            pass
        else:
            if map[tmp[0]][tmp[1]] < min:
                coord = tmp
                min = map[tmp[0]][tmp[1]]
    return coord

def calcScore(string):
    count = Counter(string)
    mostCommon = count.most_common(1)
    leastCommon = count.most_common()[-1]
    return mostCommon[0][1] - leastCommon[1]


def __main__():
    file = "Day 15/input.txt"
    arr = readFile(file)
    G = toNetwork(arr)
    path = nx.dijkstra_path(G, 1*len(arr[1])+1, 100*len(arr[1])+100, weight='weight')
    weight = nx.path_weight(G, path, 'weight')
    print(weight)


__main__()
print("--- %s seconds ---" % (time.time() - start_time))