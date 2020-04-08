def r_gcd(a, b):
	if a == 0 or b == 0:
		return max(a, b)
	if a > b:
		return gcd(a % b, b)
	else:
		return gcd(a, b % a)


def gcd(a, b):
	if a == 0 or b == 0:
		return max(a, b)
	while b != 0:
		a, b = b, a % b
	return a


def bin_gcd(a, b):
	if a == 0 or b == 0:
		return max(a, b)
	if a & 1 == 0 and b & 1 == 0:
		return bin_gcd(a >> 1, b >> 1) << 1
	elif a & 1 == 0:
		return bin_gcd(a >> 1, b)
	elif b & 1 == 0:
		return bin_gcd(a, b >> 1)
	elif a >= b:
		return bin_gcd((a - b) >> 1, b)
	else:
		return bin_gcd(a, (b - a) >> 1)


def main():
	a, b = map(int, input().split(" "))
	print(r_gcd(a, b))


if __name__ == '__main__':
	main()
