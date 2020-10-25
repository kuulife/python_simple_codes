import random
print('Hello this is a guess number game')
print('Enter 0 to stop the game')
n = random.randint(1,50)
hh = True

while True:
	inputt = int(input('Guess a number from 1,100: '))
	if inputt ==  0:
		print('You stop the game')
		break
	elif inputt > n:
		print('Your number is high, try again!')
		continue
	elif inputt < n:
		print('Your number is less, try again!')
		continue
	else:
		print('Congratulations!  You guessed a number')
		break
