def solution(l):
    # store the possibility of each node for future use
    possibilities = [0] * len(l) 
    triples = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                # update possibility
                possibilities[i] += 1 
                # add possibility of l[j] from possibilities
                triples += possibilities[j]
    return triples