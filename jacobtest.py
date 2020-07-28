class Player:
	def __init__(self):
		self.hands = [1, 1]
		self.deadHands = 0
		self.canSplit = ''
		self.currentAction = ''
		self.victimPlayer = ''
		self.victimHand = 3
		self.chosenHand = 3
		self.hasDied = False

# list of the players
players = []

# players input numberOfPlayers. numberOfPlayers must be an integer greater than 1
numberOfPlayers = 0
while numberOfPlayers <= 1:
	print('How many players are there?')
	try:
		numberOfPlayers = int(input())
	except ValueError:
		print('Invalid input: Needs to be an integer (It also needs to be greater than 1)')
		numberOfPlayers = 0
		continue
	if numberOfPlayers < 2:
		print('Invalid input: Needs to be an integer greater than 1')

def reset_turn_vars():
	for i in range(numberOfPlayers):
		players[i].canSplit = ''
		players[i].currentAction = ''
		players[i].victimPlayer = numberOfPlayers + 2
		players[i].victimHand = 3
		players[i].chosenHand = 3
		
# create desired amount of players in player list and set 
for i in range(numberOfPlayers):
	players.append(Player())
reset_turn_vars()

# players input allowKillViaSplit. allowKillViaSplit must be y or n		
allowKillViaSplit = ''
while allowKillViaSplit != 'y' and allowKillViaSplit != 'n':
	print('Allow the player on their turn to kill their own hand(s) via splitting? Y or N')
	allowKillViaSplit = input().lower()
	if allowKillViaSplit != 'y' and allowKillViaSplit != 'n': print('Invalid input')

# keep track of whose turn it is
turnPlayer = 0

print('Player {}\'s turn'.format(turnPlayer + 1))

# show each player's hands
for i in range(numberOfPlayers):
	print("Player {}'s hands: {}, {}".format(i + 1, players[i].hands[0], players[i].hands[1]))

	
# check if current player can split
if players[turnPlayer].deadHands == 2:
	print('You glitched the game and you lose cause my code is perfect')
elif players[turnPlayer].hands[0] == 0 and players[turnPlayer].hands[1] == 1:
	players[turnPlayer].canSplit = False
elif allowKillViaSplit == 'n' and players[turnPlayer].hands[0] == 1 and players[turnPlayer].hands[1] < 3:
	players[turnPlayer].canSplit = False
else:
	players[turnPlayer].canSplit = True

# if player can split, they choose between a and s, unless they can't split, in which they auto attack
if players[turnPlayer].canSplit == True:
	# player inputs their action. Must be a (attack) or s (split)	
	while players[turnPlayer].currentAction != 'a' and players[turnPlayer].currentAction != 's':
		print('Do you want to attack or split? A or S')
		players[turnPlayer].currentAction = input().lower()
		if players[turnPlayer].currentAction != 'a' and players[turnPlayer].currentAction != 's': print('Invalid input')
else:
	print('You cannot split, so you must attack')
	players[turnPlayer].currentAction = 'a'

if players[turnPlayer].currentAction == 'a':
	# player inputs which player to attack. Must be between 1 and numberOfPlayers and must not be themselves
	while players[turnPlayer].victimPlayer < 0 or players[turnPlayer].victimPlayer > numberOfPlayers - 1:
		print('Choose which player would you like to attack')
		try:
			players[turnPlayer].victimPlayer = int(input())
		except ValueError:
			print('Invalid input: Needs to be an integer (It also needs to be between 1 and {})'.format(numberOfPlayers))
			players[turnPlayer].victimPlayer = numberOfPlayers + 2
			continue
		if players[turnPlayer].victimPlayer < 1 or players[turnPlayer].victimPlayer > numberOfPlayers:
			print('Invalid input: Needs to be an integer be between 1 and {}'.format(numberOfPlayers))
			players[turnPlayer].victimPlayer = numberOfPlayers + 2
			continue
		if players[turnPlayer].victimPlayer == turnPlayer + 1:
			print('You cannot attack yourself!')
			players[turnPlayer].victimPlayer = numberOfPlayers + 2
			continue
		players[turnPlayer].victimPlayer = players[turnPlayer].victimPlayer - 1
	
	# check dead hands
	if players[turnPlayer].deadHands == 2:
		print('You glitched the game and you lose cause my code is perfect')
	if players[turnPlayer].deadHands == 1:
		# autochoose alive hand
		for hand in range(2):
			if players[turnPlayer].hands[hand] != 0: players[turnPlayer].chosenHand = hand
	if players[turnPlayer].deadHands == 0:
		# player inputs which hand to attack with. Must be 1 or 2
		while players[turnPlayer].chosenHand != 0 and players[turnPlayer].chosenHand != 1:
			print('Choose which hand you want to attack with')
			try:
				players[turnPlayer].chosenHand = int(input())
			except ValueError:
				print('Invalid input: Needs to be an integer (It also needs to be either 1 or 2)')
				players[turnPlayer].chosenHand = ''
				continue
			if players[turnPlayer].chosenHand != 1 and players[turnPlayer].chosenHand != 2:
				print('Invalid input: Needs to be either 1 or 2')
				continue
			players[turnPlayer].chosenHand = players[turnPlayer].chosenHand - 1