def encode_edges(G, k):
    (E, V) = G
    enc = ''
    #for each edge, encode the corresponding literals
    for edge in E:
        clause = '('
        for i in range(k):
            if clause != '(':
                clause += 'V'
            #build each clause
            clause += str((edge[0] - 1) * k + i + 1) + 'V'
            clause += str((edge[1] - 1) * k + i + 1) 
        #add the clause to the encoding
        enc += clause + ')^' 
    return enc[:-1]

def encode_position(G, k):
    (E, V) = G
    n = len(V)
    enc = ''

    for i in range(1, k + 1):
        #add all the nodes that can ocupy a specific position in the KVC
        aux_nodes = []
        for j in range(n):
            aux_nodes.append(j * k + i)
        aux_nodes = list(map(str,aux_nodes))
        #create a clause based on the added nodes
        clause = '(' + 'V'.join(aux_nodes) + ')'
        enc += clause + '^'
                
        #add a clause that verifies that a node appears at most once in the KVC
        for p in range(n):
            for q in range(p + 1, n):
                enc += '(~' + aux_nodes[p] + 'V~' + aux_nodes[q] + ')^'
                
    return enc[:-1]

def encode_nodes(G, k):
    (E, V) = G
    n = len(V)
    enc = ''
    
    #Iterate through all nodes and build clauses that check that at most one
    #node appears on a specific position in the KVC
    for i in range(n):
        for j in range(1, k + 1):
            for p in range((j + 1), (k + 1)):
                print('ceva')
                first_node = str(i * k + p)
                second_node = str(i * k + j)
                clause = '(~' + first_node + 'V~' + second_node + ')^'
                enc += clause
    return enc[:-1]

def KFC_to_SAT(G, k):
    expr = ''
    #compute all the partial encodings
    expr += encode_edges(G, k) + '^'
    expr += encode_position(G, k) + '^'
    expr += encode_nodes(G, k)
    return expr


def main():
    #Read k and the number of edges and vertices
    k = int(input())
    n = int(input())
    m = int(input())
    
    #Build the list of vertices and the list of edges
    V = list(range(1, n + 1))
    E = []
    for i in range(m):
        edge = input()
        bounds = list(map(int, edge.split(' ')))
        E.append((bounds[0], bounds[1]))
    
    G = (E, V)    
    print(KFC_to_SAT(G,k))
    
if __name__ == "__main__":    
    main()