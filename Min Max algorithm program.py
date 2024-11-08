import math
def minimax(depth, index, is_max, scores, max_depth):
    if depth == max_depth:
        return scores[index]
    if is_max:
        return max(minimax(depth + 1, index * 2, False, scores, max_depth),
                   minimax(depth + 1, index * 2 + 1, False, scores, max_depth))
    return min(minimax(depth + 1, index * 2, True, scores, max_depth),
               minimax(depth + 1, index * 2 + 1, True, scores, max_depth))
scores = [3, 5, 2, 9, 12, 5, 23, 23]
max_depth = int(math.log2(len(scores)))
print("The optimal value is:", minimax(0, 0, True, scores, max_depth))
