import numpy as np
from collections import defaultdict
import networkx as nx

simp =[]

class di_Graph:
    def __init__(self):
        self.graph = {}
        self.edge = []
        self.list_paths = []

    def add_edge(self, source, target):
        if source not in self.graph:
            self.graph[source] = [target]
        else:
            self.graph[source].append(target)
        if target not in self.graph:
            self.graph[target] = []

    def print_graph(self):
        print(self.graph)

    def nodes(self):
        return sorted(self.graph.keys())

    def edges(self):
        for i in self.graph.keys():
            for j in self.graph[i]:
                self.edge += [[i, j]]

        return sorted(self.edge)

    def adjacent(self, source):
        return self.graph[source]

    def path(self, source, target, path, visited, sim):
        if source == target:
            sim.append(list(path))
        else:
            for i in self.adjacent(source):
                if visited[i] is False:
                    visited[i] = True
                    path.append(i)
                    self.path(i, target, path, visited, sim)
                    visited[i] = False
                    path.pop()

        return sim

    def dfs(self):
        p = []
        for i in self.nodes():
            for j in self.nodes():
                if i!=j:
                    p+=self.dfsRecursive(i, j, [i], [i],[])
                if (i in self.adjacent(j)) and (j in self.adjacent(i)) and ([i,j,i] not in p) and ([j,i,j] not in p):
                    p.append([i,j,i])
                    p.append([j,i,j])
        return p

    def dfsRecursive(self, source, target, path, visited, sim):
        lastNode = path[-1]
        if lastNode == target:
            sim.append(list(path))
        else:
            for i in self.adjacent(lastNode):
                if i not in visited:
                    path.append(i)
                    visited.append(i)
                    self.dfsRecursive(source, target, path, visited, sim)
                    visited.remove(i)
                    path.pop()
        return sim



    def simple_path(self):
        thing = []
        visited = [False] * len(self.nodes())

        for i in self.nodes():
            for j in self.nodes():
                if i != j:
                    path = [i]
                    thing += self.path(i,j,path,visited,[])
                if (i in self.adjacent(j)) and (j in self.adjacent(i)) and ([i,j,i] not in thing) and ([j,i,j] not in thing):
                    thing.append([i,j,i])
                    thing.append([j,i,j])
        return thing

    def prime_path(self):
        pat = self.dfs()
        prime = []
        for i in range(len(pat)):
            is_true = [False] * len(pat)
            for t in range(len(pat)):
                if KMPSearch(pat[i], pat[t]) and (i != t) and (pat[i] != pat[t]):
                    is_true[t] = True
            if any(is_true) is False:
                prime.append(pat[i])
        return list(prime)



def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)


    lps = [0] * M
    j = 0

    computeLPSArray(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            return True


        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def computeLPSArray(pat, M, lps):
    len = 0

    lps[0]
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def prime_path(graph):
    prime = []
    for i in range(len(graph)):
        is_true = [False] * len(graph)
        for t in range(len(graph)):
            if KMPSearch(graph[i], graph[t]) and (i != t) and (graph[i] != graph[t]):
                print(graph[i], graph[t])
                is_true[t] = True
        if any(is_true) is False:
            prime.append(graph[i])
    return prime




def main():
    di_graph = di_Graph()
    di_graph.add_edge(0, 1)
    di_graph.add_edge(0, 2)
    di_graph.add_edge(1, 2)
    di_graph.add_edge(2, 4)
    di_graph.add_edge(2, 3)
    di_graph.add_edge(4, 5)
    di_graph.add_edge(5, 4)
    di_graph.add_edge(4, 6)
    di_graph.add_edge(3, 6)

    di_graphs = nx.DiGraph()
    di_graphs.add_edge(0, 1)
    di_graphs.add_edge(0, 2)
    di_graphs.add_edge(1, 2)
    di_graphs.add_edge(2, 4)
    di_graphs.add_edge(2, 3)
    di_graphs.add_edge(4, 5)
    di_graphs.add_edge(5, 4)
    di_graphs.add_edge(4, 6)
    di_graphs.add_edge(3, 6)

    simple = []
    #print(di_graph.dfs())
    simple_paths = 0
    for i in di_graphs.nodes():
        for j in di_graphs.nodes():
            if i != j:
                simple += list(nx.all_simple_paths(di_graphs, i, j))
    print(simple)
    print(di_graph.prime_path())
    if KMPSearch(simple[0],simple[0]):
        print('yes')




main()
