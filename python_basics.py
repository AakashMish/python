import input

def main():
	#prime_number(int)
	#generate_factorial(int)
	#is_armstrong(int)
	test()

def prime_number(type):
	number = input.get_input(type)
	is_prime = True

	if number == 1:
		print( ' Prime number' )
	elif number > 1:
		half = int(number/2)
		for i in range(2, half+1):
			if (number % i) == 0:
				is_prime = False
				break
	else:
		print ( 'Not a valid input' ) 

	if is_prime == True:
		print ('Prime number')
	else:
		print('Not a prime number')

def generate_factorial(type):
	number = input.get_input(type)
	factorial = 1
	if number == 0 or number == 1:
		print('Factorial is 1')
	elif number > 1:
		for i in range(1,number+1):
			print ('Factorial = ', factorial , 'range = ', i)
			factorial = factorial * i
		print ('Factorial - ', factorial)

def is_armstrong(type):
	number = input.get_input(type)
	number_str = str(number)
	number_length = len(number_str)
	number_list = []
	final_value = 0
	for x in number_str:
		number_list.append(int(x))

	for x in number_list:
		value = x ** number_length
		final_value = final_value + value

	print('final_value - ', final_value)
	if final_value == number:
		print('No is armstrong')
	else:
		print('No is not armstrong')
		
def test():
	set_example = {'1', '2', '2'}
	dict_example = ('1', '2', '2')
	list_example = ['1', '2', '3']
	print(type(set_example))
	print(type(dict_example))
	print(type(list_example))
	
if __name__ == '__main__':
	main()
