'''
A string is called diverse if no three consecutive letters are the same.
Examples:
    1. Given A = 6, B = 1 and C = 1 => 'aabaacaa' | 'aacaabaa' ...
    2. Given A = 1, B = 3 and C = 1 => 'abbcb' | 'bcbab' | 'bacbb' ...
    3. Given A = 0, B = 1 and C = 8 =>  'ccbcc'
'''


def solution(A, B, C):
    l = [(A, 'a'), (B, 'b'), (C, 'c')]
    l.sort()

    n_max = l[2][0]
    n_medium = l[1][0]
    n_min = l[0][0]

    x, y, z = divide_first(n_max, n_medium, n_min)
    print('x, y, z = ', x, y, z)
    a1 = to_array(n_max, x, l[2][1])
    # print('a1 = ', a1)
    a2 = to_array(n_medium, z, l[1][1])
    # print('a2 = ', a2)
    a3 = to_array(n_min, y, l[0][1])
    # print('a3 = ', a3)

    r = ''
    tmp = a2 + a3
    for i, x in enumerate(tmp):
        r += a1[i] + x

    # print(len(a1) > len(tmp))
    if len(a1) > len(tmp):
        # print(a1[len(tmp)])
        r += a1[len(tmp)]

    return r

def to_array(n, blocks, char):
    return ([char + char,] * (n - blocks))+([char,] * (blocks - (n - blocks)))


def least_blocks(n):
    return int(n / 2) + (n % 2)


def divide_first(n_max, n_medium, n_min):
    y = n_min
    z = n_medium

    for x in range(n_max, least_blocks(n_max) - 1, -1):
        for y in range(least_blocks(n_min), n_min+1):
            for z in range(least_blocks(n_medium), n_medium+1):
                if x <= y + z:
                    return x, y, z

    return x, y, z

if __name__=='__main__':
    print(solution(6, 1, 1))
    print(solution(1, 3, 1))
    print(solution(0, 1, 8))
    print(solution(6, 6, 6))
    print(solution(6, 0, 0))
    print(solution(1, 0, 0))
    print(solution(-1, 0, 0))

    '''
    import random
    import collections

    for x in range(1000):
        A = random.randint(0, 100)
        B = random.randint(0, 100)
        C = random.randint(0, 100)

        s = solution(A, B, C)
        print(s)
    '''


