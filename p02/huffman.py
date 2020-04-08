import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, prefix):
        self.left.walk(code, prefix + "0")
        self.right.walk(code, prefix + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, prefix):
        code[self.char] = prefix or '0'


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _pass1, left = heapq.heappop(h)
        freq2, _pass2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _no_matter, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded, code):
    decoded = ""
    seq = ""
    code = {v: k for k, v in code.items()}
    for ch in encoded:
        seq += ch
        if seq in code:
            decoded += code[seq]
            seq = ""
    return decoded


def huffman_decode_test():
    n, _ = map(int, input().split())
    codes = {}
    for i in range(n):
        v, k = input().split(': ')
        codes[k] = v
    encoded = input()
    print(huffman_decode(codes, encoded))


def huffman_encode_test():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


def test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, 32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        assert huffman_decode(encoded, code) == s
    print("Ok. Passed all tests.")


def main():
    test()


if __name__ == '__main__':
    main()
