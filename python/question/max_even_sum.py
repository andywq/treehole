'''
sum K numbers from list A (length N),
sum should be an even number and as large as possible
if K > len(A) returns -1
'''

def is_even(n):
    return 0 == n % 2

def solution(A, K):
    if K > len(A):
        return -1


    A.sort(key=lambda x: -x)
    larger = A[:K]
    smaller = A[K:]
    result = sum(larger)

    if is_even(result):
        return result

    for i in range(K - 1, -1 , -1):
        for x in smaller:
            if not is_even(larger[i] + x):
                return result - larger[i] + x

    return -1
