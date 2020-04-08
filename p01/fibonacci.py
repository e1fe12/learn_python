from rcviz import viz
from matplotlib import pyplot as plt
import time
from functools import lru_cache
import time


def fib1(n):
	assert n >= 0
	return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


cache = {}


# def fib2(n):
# 	assert n >= 0 
# 	if n not in cache: 
# 		cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
# 	return cache[n]                                    


def fib2(n):
	# BU
	assert n >= 0
	if n <= 1:
		return n
	if n in cache:
		return cache[n]
	for i in range(2, n+1):
		cache[i] = fib2(i - 1) + fib2(i - 2)
	return cache[n]


def fib3(n):
	assert n >= 0
	f0 = 0
	f1 = 1
	for i in range(n):
		f0, f1 = f1, f0 + f1
	return f0


def memo(f):
	cache = {}

	def inner(n):
		if n not in cache:
			print(cache)
			cache[n] = f(n)
		return cache[n]

	return inner


def timed(f, *args, n_iter=100):
	acc = float("inf")
	for i in range(n_iter):
		t0 = time.perf_counter()
		f(*args)
		t1 = time.perf_counter()
		acc = min(acc, t1 - t0)
	return acc


def compare(fs, args):
	plt.figure()
	xs = list(range(len(args)))
	for f in fs:
		plt.plot(xs, [timed(f, chunk) for chunk in args], 
			label=f.__name__)
	plt.legend()
	plt.grid(True)
	plt.text(0, -0.1**6, "Сonclusion: cached, so O(1) vs O(N*N)")
	plt.show()


def main():
	nonlocal fib1, fib2, fib3  
	fib1 = lru_cache(maxsize=None)(fib1)
	print(fib1(8), fib2(8), fib3(8))
	cache.clear()
	compare([fib1, fib2, fib3], list(range(200)))


if __name__ == '__main__':
	main()
