# Merge Sort from pseudocode of Introduction To Algorithms
# (T.H. Cormen, C.E. Leiserson, R.L. Rivest, C. Stein)
# Third Edition
# Index problems that not allow a correct sort were fixed!
# I decided not include the 2 ugly whiles at the end of the pseudocode of the fourth edition :)

import math

max_value = 10000


def merge_sort(p, r):  # index: 0 -> (n-1)
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)


def merge(p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])
    L.append(max_value)
    R.append(max_value)
    i = 0
    j = 0
    k = p
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


if __name__ == '__main__':
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10]
    print(A)
    merge_sort(0, len(A) - 1)
    print(A)
