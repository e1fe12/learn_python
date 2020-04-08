class Item:
    def __init__(self, cost, volume):
        self.cost = cost
        self.volume = volume
        self.sp_cost = cost / volume


def swap(a: list, i: int, j: int):
    a[i], a[j] = a[j], a[i]


def insertion_sort(a: list, key: str, ascending=True):
    ascending_check = lambda x: getattr(a[x], key) < getattr(a[x - 1], key)
    descending_check = lambda x: getattr(a[x], key) > getattr(a[x - 1], key)
    check = ascending_check if ascending else descending_check

    for i in range(1, len(a)):
        j = i
        while j > 0 and check(j):
            swap(a, j, j - 1)
            j = j - 1


def main():
    n, w = map(int, input().split(' '))
    items = []
    for i in range(n):
        c, v = map(int, input().split())
        items.append(Item(c, v))
    insertion_sort(items, "sp_cost", False)

    total_cost = 0
    for item in items:
        if w == 0:
            break
        if item.volume <= w:
            total_cost += item.cost
            w -= item.volume
        else:
            total_cost += item.sp_cost * w
            w = 0

    print("%.3f" % total_cost)


if __name__ == '__main__':
    main()
