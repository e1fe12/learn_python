class Heap:
    def __init__(self, a=tuple()):
        self.h = [0] * (2 * len(a) + 1)
        self.size = len(a)
        self.h[:self.size] = a
        self.build_heap()

    def build_heap(self):
        for i in range((self.size - 1) // 2, -1, -1):
            self.sift_down(i)

    def insert(self, x):
        if self.size + 1 > len(self.h):
            self.h = self.h + [0] * (len(self.h) + 1)
        self.size += 1
        self.h[self.size - 1] = x
        self.sift_up(self.size - 1)

    def sift_up(self, i: int):
        while i > 0 and self.h[i] > self.h[(i - 1) // 2]:
            self.h[i], self.h[(i - 1) // 2] = self.h[(i - 1) // 2], self.h[i]
            i = (i - 1) // 2

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < self.size and self.h[right] > self.h[left]:
                j = right
            if self.h[i] >= self.h[j]:
                break
            self.h[i], self.h[j] = self.h[j], self.h[i]
            i = j

    def extract_max(self):
        if self.size == 0:
            return
        max_ = self.h[0]
        self.h[0] = self.h[self.size - 1]
        self.size -= 1
        self.sift_down(0)
        return max_

    def __str__(self):
        return ' '.join([str(self.h[i]) for i in range(self.size)])


def main():
    n = int(input())
    h = Heap()
    for i in range(n):
        in_line = input().split()
        if in_line and in_line[0][0] == 'I':
            h.insert(int(in_line[1]))
        elif in_line and in_line[0][0] == 'E':
            print(h.extract_max())


if __name__ == '__main__':
    main()
