for i in range(1,101):
	if i % 3 == 0 and i % 5 == 0:
		print(i, 'Fizz Buzz')
	else:
		if i % 3 == 0:
			print(i, 'Fizz')
		elif i % 5 == 0:
			print(i, 'Buzz')
