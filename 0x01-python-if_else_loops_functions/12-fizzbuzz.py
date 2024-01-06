def fizzbuzz():
	for num in range(1, 101):
		if abs(num) % 3 == 0 and num % 5 == 0:
			print("FizzBuzz ", end=" ")
		if abs(num) % 3 == 0:
			print("Fizz", end=" ")
		elif abs(num) % 5 == 0:
			print("Buzz", end=" ")
		else:
			print(num, end=" ")
	return (num)
