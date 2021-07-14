from collections import deque

def bfs(graph_li,visited_li,root):
    queue = deque([root])
    print(visited_li, queue, f"next root: {root}")
    
    while queue:
        root = queue.popleft()
        if not visited_li[root]:
            visited_li[root] = True
            queue+=graph[root]
            print(visited_li, queue, f"next root: {root}")
        else:
            queue.popleft()
    
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
        []
    ]

    visited = [False]*len(graph)

    print(bfs(graph,visited,1))
    
    

'''
1.

def bfs(graph_li,visited_li,root):
    queue = deque([root])
    print(visited_li, queue, f"next root: {root}")
    
    while queue:
        root = queue.popleft()
        if not visited_li[root]:
            visited_li[root] = True
            queue+=graph[root]
            print(visited_li, queue, f"next root: {root}")
        else:
            queue.popleft()
    
    return visited_li
    
2.

def bfs(graph_li,visited_li,root):
    queue = deque([root])
    print(visited_li, queue, f"next root: {root}")
    
    while queue:
        if not visited_li[queue[0]]:
            visited_li[root] = True
            
            #*********************Following code, which is the difference, goes in to the 'if block' while the first code has it out side the 'if block'.**********************
            root = queue.popleft()
            
            queue+=graph[root]
            print(visited_li, queue, f"next root: {root}")
        else:
            queue.popleft()
    
    return visited_li

------------------------------------------------------------------

1. output:
Correct

2. output:
It doesn't mark the last node "searched", which is 'True' in 'visited_li'

'''