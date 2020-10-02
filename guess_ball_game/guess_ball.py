from random import shuffle

def shuffle_list(mylist):
	shuffle(mylist)
	return mylist


def player_guess():
	guess = ''
	while guess not in ['0','1','2']:
		guess = input("pick a number 0 , 1 or 2: ")
	return int(guess)



def check_guess(mylist,guess):
	if mylist[guess] == 'O':
		print('correct')
	else:
		print('wrong')
		print(mylist)


my = [' ', ' ', 'O']

mixed_list = shuffle_list(my)

guess = player_guess()

check_guess(mixed_list, guess)
