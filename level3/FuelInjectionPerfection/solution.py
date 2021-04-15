def solution(n):
    n = int(n)
    result = 0
    while n > 1:
        if n & 1 == 1:
            if n % 4 == 1 or n==3:
                n -= 1
            else:
                n += 1
        else:
            n = n >> 1
        result += 1
    return result