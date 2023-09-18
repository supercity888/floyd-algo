# Floyd Warshall Algorithm
### to obtain the shortest path algorithm between two nodes of a graph
### from the distance matrix shared:
    INF = float("inf")
    matrix =    [[0, 7, INF, 8],
                [INF, 0, 5, INF],
                [INF, INF, 0, 2],
                [INF, INF, INF, 0]]
    nV = len(matrix[0])

### using the Python code for the above algorithm:
    def floyd_warshall(matrix):
    distance = list(map(lambda i: list(map(lambda j: j, i)), matrix))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)

    # Printing the solution
    def print_solution(distance):
        for i in range(nV):
            for j in range(nV):
                if(distance[i][j] == INF):
                    print("INF", end=" ")
                else:
                    print(distance[i][j], end="  ")
            print(" ")

    floyd_warshall(matrix)

### validating using recursive version
    def floyd_recursive(distance, start_node, end_node, intermediate):
        if intermediate == nV:
            return distance[start_node][end_node]
        
        direct_distance = distance[start_node][end_node]
        through_intermediate_distance = (
            floyd_recursive(distance, start_node, end_node, intermediate + 1),
            floyd_recursive(distance, start_node, intermediate, intermediate + 1) +
            floyd_recursive(distance, intermediate, end_node, intermediate + 1)
        )
        
        return min(direct_distance, min(through_intermediate_distance))

    def compute_shortest_paths(distance):
        shortest_paths = [[0] * nV for _ in range(nV)]
        
        for start_node in range(nV):
            for end_node in range(nV):
                shortest_paths[start_node][end_node] = floyd_recursive(distance, start_node, end_node, 0)
        
        return shortest_paths

    result = compute_shortest_paths(matrix)
    for row in result:
        print(row)
### Output from Python terminal
    [0, 7, 12, 8]
    [inf, 0, 5, 7]    
    [inf, inf, 0, 2]  
    [inf, inf, inf, 0]    

Check Requirements File [here](./requirements.txt)