class Seg:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def insertion_sort(a: list):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j].right < a[j - 1].right:
            a[j], a[j - 1] = a[j - 1], a[j]
            j = j - 1


def main():
    n = int(input())
    segments = []
    for i in range(n):
        l, r = map(int, input().split())
        segments.append(Seg(l, r))
    insertion_sort(segments)
    i = 0
    ans = []
    while i < n:
        x = segments[i].right
        ans.append(x)
        i += 1
        while i < n and segments[i].left <= x:
            i += 1

    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
