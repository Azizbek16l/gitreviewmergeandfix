import random 

guess=int(random.randint()*10)
n=int(input('son kirit'))
guesses=0
while True:
		if n==guess:
			print('topding')
			break
		
		if guess>=3:
			print('yutqading')
		
