def solution(area):
    squares = []
    while area > 0:
        largest_sub_square = int(area ** 0.5)
        squares.append(largest_sub_square ** 2)
        area -= largest_sub_square ** 2
    return squares
