def F(n:int):
    if n <= 1:
        return n
    a = [1, 1, 1, 0]
    c = [1, 0, 1, 0]
    k = n - 1
    while k != 0:
        if k & 1 == 0:
            k //= 2
            a11 = a[0] * a[0] + a[1] * a[2]
            a12 = a[0] * a[1] + a[1] * a[3]
            a21 = a[2] * a[0] + a[3] * a[2]
            a22 = a[2] * a[1] + a[3] * a[3]
            a = [a11, a12, a21, a22]
        else:
            k -= 1
            c11 = c[0] * a[0] + c[1] * a[2]
            c12 = c[0] * a[1] + c[1] * a[3]
            c21 = c[2] * a[0] + c[3] * a[2]
            c22 = c[2] * a[1] + c[3] * a[3]
            c = [c11, c12, c21, c22]
    return c[0]


def main():
    n = int(input())
    print(F(n))

if __name__ == '__main__':
    main()
