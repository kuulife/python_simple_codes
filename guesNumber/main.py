import random

guesnumber = random.randint(0,100)

count = 0

while True:
	inp = int(input('enter number: ')) 
	if guesnumber == inp:
		print('you guess the number, number was : {}'.format(guesnumber))
		print('you guessed bumber in {} try'.format(count+1))
		break
	elif guesnumber > inp:
		print('your number is less choose higher number')
		count = count +1
		print('{} try'.format(count))
		continue
	elif guesnumber < inp:
		print('your number is big choose lower number')
		count = count+1
		print('{} try'.format(count))
		continue	

