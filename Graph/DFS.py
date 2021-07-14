def dfs(graph_li,visited_li,root): 
    visited_li[root] = True
    for i in graph_li[root]:
        if not visited_li[i]:
            #print(visited_li, f"next root: {i}")
            dfs(graph_li, visited_li, i)
    return visited_li

if __name__ == '__main__':
    graph = [
        [],
        [2,3],
        [4,5],
        [],
        [],
        [6,7],
        [],
        [1]
    ]

    visited = [False]*len(graph)

    print(dfs(graph,visited,1))