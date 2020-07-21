import numpy as np


def solution(N):
    memo = [[0 for x in range(N+2)] for y in range(N+2)]
    memo[3][2] = memo[4][2] = 1  # setting base cases

    for y in range(5, N+1):
        memo[y][2] = memo[y-2][2] + 1  # @2 steps: # of staircases inc by 1
        # when n inc by 2
        for x in range(3, y + 1):
            memo[y][x] = memo[y-x][x-1] + memo[y-x][x]
            if memo[y][x] == 0:
                break  # no more steps possible beyond this
    return np.sum(memo[N])

# _-_-_-_-_-_-_-_-_-_-_-_-TEST--CASES-_-_-_-_-_-_-_-_-_-_-_-_


print(solution(3))  # => 1
print(solution(200))  # => 487067745

'''
7=6.1,5.2,4.3,4.21
10=9.1,8.2,7.3,7.21,6.4,6.31,5.41,5.32,4.321
12=11.1,10.2,9.3,9.21,8.4,8.31,7.5,7.41,7.32,6.51,6.42,6.321,5.43,5.421
'''
