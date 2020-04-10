import sys


def binary_search(a: list, k: int):
    l, r = 0, len(a)
    while l + 1 < r:
        mid = (l + r) // 2
        if a[mid] <= k:
            l = mid
        else:
            r = mid
    return l + 1 if a[l] == k else -1


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, *a = next(reader)
    k, *b = next(reader)
    ans = [binary_search(a, x) for x in b]
    print(*ans)


if __name__ == '__main__':
    main()
