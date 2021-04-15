# Solution 1
def solution(l):
    d = dict.fromkeys(l, 0)
    for v in l:
        d[v] = [map(int, num) for num in v.split(".")]
    d = sorted(d.items(), key=lambda x: x[1])
    return [v[0] for v in d]

# Solution 2
# This may faster then Solution 3. Function sorted() in python use insertion sort and 
# merge sort while Solution 3 use insertion only
from distutils.version import LooseVersion
def solution(l):
    return sorted(l, key=LooseVersion)

# Solution 3
def is_key_smaller(key, j_elevator):
    key_versions = [int(v) for v in key.split(".")]
    j_versions = [int(v) for v in j_elevator.split(".")]
    k_len = len(key_versions)
    j_len = len(j_versions)
    step = k_len if k_len < j_len else j_len
    start = 0
    while (step - (start)) > 0:
        if key_versions[start] < j_versions[start]:
            return True
        if key_versions[start] > j_versions[start]:
            return False
        start += 1
    if len(key_versions) < len(j_versions):
        return True
    return False

def solution(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and is_key_smaller(key, l[j]):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

# Solution4
# It is similar to Solution3, because python use lexicographical ordering to compare
# sequence objects.
# https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
def solution(l):
    int_l = [map(int, v.split(".")) for v in l]
    for i in range(1, len(int_l)):
        key = int_l[i]
        j = i -1
        while j >= 0 and key < int_l[j]:
            int_l[j+1] = int_l[j]
            j -= 1
        int_l[j+1] = key
    result = [".".join(map(str, v)) for v in int_l]
    return result