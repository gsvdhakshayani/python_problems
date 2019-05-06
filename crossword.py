r = int(input())
c = int(input())
li = []
s = 0
y = []
x = []
z = 0
for i in range(r):
	a = [w for w in input()]
	li.append(a)
for i in range(r):
	x = []
	for j in range(c):
		if (i == 0 or j == 0) and li[i][j] != '*':
			s += 1
			x.append(s)
		elif li[i][j] != '*' and (li[i - 1][j] == '*' or li[i][j - 1] == '*') :
			s += 1
			x.append(s)
		else:
			x.append(0)
	y.append(x)
print('PUZZLE#',z+1)
print('ACROSS===========================')
for i in range(r):
	s1 = ''
	for j in range(c):
		if li[i][j] != '*':
			if len(s1) == 0:
				num = y[i][j]
			s1 = s1 + li[i][j]
		if j == c - 1 or li[i][j] == '*':
			s1 = s1 + '\0'
			if s1[0] != '\0':
				print(str(num)+'.'+s1)
			s1 = ''
print('DOWN=========================')
li1 = []
li2 = []
for j in range(c):
	s1 = ''
	for i in range(r):
		if li[i][j] != '*':
			if len(s1) == 0:
				num = y[i][j]
			s1 = s1 + li[i][j]
		if i == r - 1 or li[i][j] == '*':
			s1 = s1 + '\0'
			if s1[0] != '\0':
				li1.append(num)
				li2.append(s1)	
			s1 = ''
dictionary = dict(zip(li1,li2))
for i in dictionary:
	print(str(i)+'.'+dictionary[i])

