n = input("Введите набор цифр: ")
n = list(n)

i = 0

length = len(n) - 1
while i <= length:
	n.sort()
	n.reverse()
	print(n[i])
	i += 1
#--------------------------------------------------------------------------------
fib1 = 1
fib2 = 1

n = input("Number element: ")
n = int(n)

i = 0
while i < n -2:
	fib_sum = fib1 + fib2
	fib1 = fib2
	fib2 = fib_sum
	print (fib2)
	i+=1 
#--------------------------------------------------------------------------------