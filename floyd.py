# Floyd Warshall Algorithm
# getting the shortest path algorithm between two nodes on a graph
INF = float("inf")
matrix = [[0, 7, INF, 8],
     [INF, 0, 5, INF],
     [INF, INF, 0, 2],
     [INF, INF, INF, 0]]
nV = len(matrix[0])

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