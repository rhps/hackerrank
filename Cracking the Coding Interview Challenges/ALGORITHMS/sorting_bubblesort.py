def bublesort(a):
	itr = 0
	for i in range(0,n):
		for j in range(0,n-1):
			if (a[j] > a[j+1]):
				a[j], a[j+1] = a[j+1], a[j]
				itr = itr + 1

	return a, itr


if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().strip().split(' ')))

	sorteda, itr = bublesort(a)
	print('Array is sorted in {} swaps.'.format(itr))
	print('First Element: {}'.format(a[0]))
	print('Last Element: {}'.format(a[-1]))