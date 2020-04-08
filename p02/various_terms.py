def main():
    n = int(input())
    terms = []
    s = 0
    i = 1
    while s <= n:
        s += i
        terms.append(i)
        i += 1

    del terms[s - n - 1]
    print(len(terms))
    print(*terms)


if __name__ == '__main__':
    main()
