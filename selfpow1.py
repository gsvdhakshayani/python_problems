li = []
sum = sum(x ** x for x in range(1,1001))
li = [l for l in str(sum)]
print(li[-10:])
