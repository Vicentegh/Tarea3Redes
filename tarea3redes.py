import pdb

def initialize(graph, source):
    d = {} 
    p = {} 
    for node in graph:
        d[node] = float('Inf') 
        p[node] = None
    d[source] = 0
    return d, p
 
def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node
 
def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): 
        for u in graph:
            for v in graph[u]: 
                relax(u, v, graph, d, p) 
 
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
 
    return d, p
 
 
def test():
    arriba = "\tPC\tA\tB\tC\tD\tE\tF\tG\tH\tI\tServer"
    parte1 = ['' for i in range(11)]
    parte2 = ['' for i in range(11)]
    nodos = ['pc', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'se']    
    matriz1 = {
        'pc': {'a': 3},
        'a': {'pc': 3, 'b': 1, 'g': 4, 'i': 10},
        'b': {'a': 1, 'c': 9, 'e': 8},
        'c': {'b': 9, 'd': 2},
        'd': {'c': 2, 'e': 9, 'f': 4, 'i': 2},
	'e': {'b': 8, 'd': 9, 'f': 2, 'i': 1},
        'f': {'d': 4, 'e': 2, 'h': 6},
        'g': {'a': 4, 'h': 7},
        'h': {'f': 6, 'g': 7, 'i': 3},
        'i': {'a': 10, 'd': 2, 'e': 1, 'h': 3, 'se': 1},
	'se': {'i': 1}
        }
    matriz2 = {
        'pc': {'a': 3},
        'a': {'pc': 3, 'b': 1, 'g': 4, 'i': 10},
        'b': {'a': 1, 'c': 9, 'e': 8},
        'c': {'b': 9, 'd': 2},
        'd': {'c': 2, 'e': 9, 'f': 4, 'i': 2},
	'e': {'b': 8, 'd': 9, 'f': 2, 'i': 1},
        'f': {'d': 4, 'e': 2, 'h': 6},
        'g': {'a': 4, 'h': 7},
        'h': {'f': 6, 'g': 7},
        'i': {'a': 10, 'd': 2, 'e': 1, 'se': 1},
	'se': {'i': 1}
        }    
    for b in nodos:
        d, p = bellman_ford(matriz1, b)
        matriz1[b]=d
    for c in nodos:
        d, p = bellman_ford(matriz2, c)
        matriz2[c]=d
    contx=0
    for pos1 in nodos:
        conty=0
        for pos2 in nodos:
            parte1[contx] = parte1[contx] + "\t"+ str(matriz1[pos1][pos2])
            conty+=1
        contx+=1
    contx=0
    for pos1 in nodos:
        conty=0
        for pos2 in nodos:
            parte2[contx] = parte2[contx] + "\t"+ str(matriz2[pos1][pos2])
            conty+=1
        contx+=1
    print "Pregunta 1 de Distancia Vector"
    print arriba
    parte1[0] = "PC"+parte1[0]
    parte1[1] = "A"+parte1[1]
    parte1[2] = "B"+parte1[2]
    parte1[3] = "C"+parte1[3]
    parte1[4] = "D"+parte1[4]
    parte1[5] = "E"+parte1[5]
    parte1[6] = "F"+parte1[6]
    parte1[7] = "G"+parte1[7]
    parte1[8] = "H"+parte1[8]
    parte1[9] = "I"+parte1[9]
    parte1[10] = "Server"+parte1[10]
    for i in range(11):
        print parte1[i]
    print "\n\n"
    print "Pregunta 2 de Distancia Vector"
    print arriba
    parte2[0] = "PC"+parte2[0]
    parte2[1] = "A"+parte2[1]
    parte2[2] = "B"+parte2[2]
    parte2[3] = "C"+parte2[3]
    parte2[4] = "D"+parte2[4]
    parte2[5] = "E"+parte2[5]
    parte2[6] = "F"+parte2[6]
    parte2[7] = "G"+parte2[7]
    parte2[8] = "H"+parte2[8]
    parte2[9] = "I"+parte2[9]
    parte2[10] = "Server"+parte2[10]
    for i in range(11):
        print parte2[i]


if __name__ == '__main__': test()
