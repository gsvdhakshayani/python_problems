import sys
p = 1
while True:
	r = 2
	c = 2
	li = []
	a = []
	for k in range(r):
		a = [x for x in input()]
		if 'Z' in a:
               		sys.exit()
		li.append(a)
	str = input()
	print('PUZZLE #',end='')
	print(p)
	p = p + 1
	for k in range(r):
		for m in range(c):
			if li[k][m] == ' ':
				i = k 
				j = m
	for l in str:
		if i < 0 or i > r - 1 or j < 0 or j > c - 1:
			print('this puzzle has no final configuration')
			break
		else:
			if l == 'A':
				li[i][j],li[i-1][j] = li[i - 1][j],li[i][j]
				i = i - 1
			elif l == 'B':
				li[i][j],li[i + 1][j] = li[i + 1][j],li[i][j]
				i = i + 1
			elif l == 'R':
				li[i][j],li[i][j+1] = li[i][j + 1],li[i][j]
				j = j + 1
			elif l == 'L':
				li[i][j],li[i][j-1] = li[i][j - 1],li[i][j]
				j = j - 1	
			elif l == 'O':
				break	
	if i >= 0 and j >= 0 and j < c  and i < r :
		for i in range(r):
			for j in range(c):
				print(li[i][j],end = '')	
			print()	

		
