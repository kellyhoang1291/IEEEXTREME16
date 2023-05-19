

def addEdge(x, y):
    v[x].append(y)
    v[y].append(x)


def printPath(stack):
    for i in range(len(stack) - 1):
        path_array.append(stack[i])
    path_array.append(stack[-1])

def DFS(vis, x, y, stack):
    stack.append(x)
    if (x == y):
        printPath(stack)
        return
    vis[x] = True

    if (len(v[x]) > 0):
        for j in v[x]:
            if (vis[j] == False):
                DFS(vis, j, y, stack)
    del stack[-1]


def DFSCall(x, y, n, stack):
    vis = [0 for i in range(n + 1)]
    DFS(vis, x, y, stack)

for i in range(int(input())):
    weight_arr = []
    n = int(input())
    v = [[] for i in range(n * n)]
    weight_arr = list(map(int, input().split()))
    for i in range(n-1):
        v1, v2 = list(map(int, input().split()))
        addEdge(v1, v2)
    for i in range(int(input())):
        result = 1
        option, val1, val2 = list(map(int, input().split()))
        if option == 1:
            weight_arr[val1 - 1] = val2
        if option == 2:
            path_array = []
            stack = []
            DFSCall(val1, val2, n, stack)
            # print(path_array)
            for index in path_array:
                result *= weight_arr[index - 1]
            print(result % (pow(10, 9) + 7))
        # print(path_array)