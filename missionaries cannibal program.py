from collections import deque
def missionaries_and_cannibals():
    start = (3, 3, 1)
    goal = (0, 0, 0)  
    queue = deque([(start, [])])
    visited = set([start])
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] 
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path + [goal]
        m, c, b = current
        for dm, dc in moves:
            if b == 1:
                next_state = (m - dm, c - dc, 0) 
            else:
                next_state = (m + dm, c + dc, 1)  
            nm, nc, nb = next_state  
            if 0 <= nm <= 3 and 0 <= nc <= 3 and (nm == 0 or nm >= nc) and (3 - nm == 0 or 3 - nm >= 3 - nc):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [current]))
    return "No solution found"
solution = missionaries_and_cannibals()
if solution != "No solution found":
    for step in solution:
        print(step)
else:
    print(solution)
