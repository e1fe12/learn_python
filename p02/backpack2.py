import sys
import heapq


def fractional_knapsack(capacity, cost_and_volumes):
    order = [(-c / v, v) for c, v in cost_and_volumes]
    heapq.heapify(order)

    total_cost = 0
    while order and capacity:
        c_per_v, v = heapq.heappop(order)
        can_take = min(v, capacity)
        total_cost -= c_per_v * can_take
        capacity -= can_take

    return total_cost


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    cost_and_volumes = list(reader)
    ans = fractional_knapsack(capacity, cost_and_volumes)
    print("{:.3f}".format(ans))


if __name__ == '__main__':
    main()
