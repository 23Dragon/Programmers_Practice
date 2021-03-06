def solve(level, begin):
    if level == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(begin, N):
            result[level] = arr[i]
            solve(level+1, i)


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [int(x) for x in range(1, N+1)]
    result = [0] * M
    check = [0] * N

    solve(0, 0)

'''
4 2
'''