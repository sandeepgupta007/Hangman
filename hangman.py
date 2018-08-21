'''
    Hangman, Fun and recreational game through which one can increase his vocab and thinking abilities.

    Requirements - python 3.6, and module RandomWords.

    how to install Module RandomWords ?
        pip install RandomWords

    How to use ?
    This game will soon be deployed on website, untill then you can clone the repo and directly run the python script on terminal or python GUI.

    Developer's:
		This game is made in two levels one is for beginners and other is for pro players, seperate functions are there for all the activities so it's easy to debug the program. Variables names declared are self_explantory.For any doubt comment on git.

	NOTE: I haven't checked it thouroughly so there might be some unsual crashes.Fixed all the bugs which I'm aware of, while playing this game if you find an error please comment and I'll try to remove that ambiguity. 

'''

import os
from random_words import RandomWords
import random
import string

def main():
	print ('*** Play HangMan ****')
	type()

def type():
	print ('Its gonna be tough, play easy or be a pro!')
	print ('Enter 1 to play easy')
	print ('Enter 2 to play pro')
	print ('Enter 3 to QUIT     ',end='')
	game_choice = int(input())
	if(game_choice == 1):
		gameEasy()
	elif (game_choice == 2):
		gamePro()
	else:
		quit()
	type()

def check(word_show):
	for i in word_show:
		if(i == '_'):
			return False
	return True

def disp(word_show):
	for i in word_show:
		print (i.upper(),end=' ')
	print ('\n')

def gameEasy():
	rw = RandomWords()
	lose = False
	while(lose == False):
		w = rw.random_word()
		length = len(w)
		word=[]

		for i in range(length):
			word.append(w[i].lower())
		
		word_show = []
		for i in range(int(length)):
			word_show.append('_')

		show = True
		life = length
		count = random.randint(1,length)-1
		while(count > 0 and check(word_show) == False):
			vshown = random.choice(string.ascii_letters)
			show = True
			for i in range(len(word)):
				if(word[i] == vshown):
					word_show[i]=vshown
					show = False
					life-=1
			if(show == False):
				count-=1

		print ('Character to be guessed - ',life)

		#print (word_show.strip('"\''))
		disp(word_show)
		#print '[%s]' % ', '.join(map(str,word_show))

		while(check(word_show) == False and lose == False):
			print ('Health - ',life)
			print ('\nGuess a character - ',end='')
			character = input()
			character = character.lower()
			flag = False

			for i in range(length):
				if(word[i] == character):
					flag = True
					word_show[i] = character.upper()
			
			os.system('clear')
			if(flag == False):
				life-=1
				print ('You missed it!')
			else:
				print ('Congo : Your guess was correct!')

			disp (word_show)
			if(life <= 0):
				lose = True
				disp (word)
				print ('Game Over')

		if(check(word_show)):
			print ('\nHurray - You won! \n')

def gamePro():
	rw = RandomWords()
	lose = False
	while(lose == False):
		w = rw.random_word()
		length = len(w)
		word=[]
		for i in range(length):
			word.append(w[i].lower())
		
		life = length
		print ('Character to be guessed - ',life)
		word_show = []
		
		for i in range(int(length)):
			word_show.append('_')

		#print (word_show.strip('"\''))
		disp(word_show)
		#print '[%s]' % ', '.join(map(str,word_show))

		while(check(word_show) == False and lose == False):
			print ('Health - ',life)
			print ('\nGuess a character - ',end='')
			character = input()
			character = character.lower()
			flag = False

			for i in range(length):
				if(word[i] == character):
					flag = True
					word_show[i] = character.upper()
			
			os.system('clear')
			if(flag == False):
				life-=1
				print ('You missed it!')
			else:
				print ('Congo : Your guess was correct!')

			disp (word_show)
			if(life <= 0):
				lose = True
				disp (word)
				print ('Game Over')
		if(check(word_show)):
			print ('\nHurray - You won! \n')

main()
