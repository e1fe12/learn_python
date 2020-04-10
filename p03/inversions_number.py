import sys
from collections import deque


cnt = 0


def merge(a: list, b: list):
    global cnt
    n, m = len(a), len(b)
    i, j = 0, 0
    c = [0] * (n + m)

    while i + j < n + m:
        if j == m or (i < n and a[i] <= b[j]):
            c[i + j] = a[i]
            i += 1
        else:
            c[i + j] = b[j]
            j += 1
            cnt += n - i

    return c


def main():
    _ = next(sys.stdin)
    a = [[int(s)] for s in next(sys.stdin).split()]
    q = deque(a)

    while len(q) > 1:
        i1 = q.popleft()
        i2 = q.popleft()
        if len(i1) < len(i2):
            q.append(i1)
            q.appendleft(i2)
        else:
            q.append(merge(i1, i2))
    print(cnt)


if __name__ == '__main__':
    main()
