import copy

def solution(src, dest):
    graph = {}
    nodes = [src]
    curr_nodes = [src]
    visited = []
    moves = 0
    near_positions = [[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1]]
    for i in range(64):
        graph[i] = []
        x = i % 8
        y = i / 8
        for np in near_positions:
            if x + np[0] >= 0 and x + np[0] < 8:
                if y + np[1] >= 0 and y + np[1] < 8:
                    graph[i].append(((y + np[1]) * 8 + (x + np[0])))
    while nodes:
        node = nodes.pop()
        visited.append(node)
        if node == dest:
            return moves
        if len(nodes) == 0:
            for cn in curr_nodes:
                for n in graph[cn]:
                    if n not in visited:
                        nodes.append(n)
            curr_nodes = copy.deepcopy(nodes)
            moves += 1
    return moves