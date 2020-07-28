class Player:
	def __init__(self):
		self.hands = [1, 1]
		self.tempHands = [1, 1]
		self.deadHands = 0
		self.tempDeadHands = 0
		self.hasDied = False

# list of the players
players = []

# players input numberOfPlayers. numberOfPlayers must be an integer greater than 1
numberOfPlayers = 0
while numberOfPlayers < 2:
	print('How many players are there?')
	try:
		numberOfPlayers = int(input())
	except ValueError:
		print('Invalid input: Needs to be an integer (It also needs to be greater than 1)')
		numberOfPlayers = 0
		continue
	if numberOfPlayers < 2:
		print('Invalid input: Needs to be an integer greater than 1')
		numberOfPlayers = 0
		continue
		
# create desired amount of players in player list
for i in range(numberOfPlayers):
	players.append(Player())

# players input allowKillViaSplit. allowKillViaSplit must be y or n		
allowKillViaSplit = ''
while allowKillViaSplit != 'y' and allowKillViaSplit != 'n':
	print('Allow the player on their turn to kill their own hand(s) via splitting? Y or N')
	allowKillViaSplit = input().lower()
	if allowKillViaSplit != 'y' and allowKillViaSplit != 'n': print('Invalid input')

# keep track of whose turn it is
turnPlayer = 0

# turn variables
TPcanSplit = ''
TPcurrentAction = ''
victim = numberOfPlayers + 2
victimHand = 3
TPchosenHand = 3
TPunchosenHand = 3
TPisSureOfTurn = ''
amountGettingSubtactedSplitting = 0
validSplit = False
splitSameHandCount = 0
firstSplitChecker = 0

deadPlayers = 0
gameOver = False

while gameOver == False:	
	# show each player's hands
	for i in range(numberOfPlayers):
		if players[i].hasDied == False:
			print('Player {}\'s hands: {}, {}'.format(i + 1, players[i].hands[0], players[i].hands[1]))
		
	print('Player {}\'s turn'.format(turnPlayer + 1))
	
	# check if current player can split
	if players[turnPlayer].deadHands == 2:
		print('You glitched the game and you lose')
	elif players[turnPlayer].deadHands == 1:
		for hand in range(2):
			if players[turnPlayer].hands[hand] == 1: TPcanSplit = False
	if allowKillViaSplit == 'n':
		for handNumber in range(2):
			if players[turnPlayer].hands[handNumber] == 1:
				firstSplitChecker = firstSplitChecker + 1
				continue
			if players[turnPlayer].hands[handNumber] < 3: 
				firstSplitChecker = firstSplitChecker + 1
				continue
		if firstSplitChecker == 2: TPcanSplit = False
	if TPcanSplit != False:
		TPcanSplit = True

	# player's action gets decided
	if TPcanSplit == True:
		# player inputs their action. Must be a (attack) or s (split)	
		while TPcurrentAction != 'a' and TPcurrentAction != 's':
			print('Do you want to attack or split? A or S')
			TPcurrentAction = input().lower()
			if TPcurrentAction != 'a' and TPcurrentAction != 's': print('Invalid input')
	elif TPcanSplit == False:
		# player is forced to attack
		print('You cannot split, so you must attack')
		TPcurrentAction = 'a'

	if TPcurrentAction == 'a':
		# victim gets decided
		if deadPlayers >= numberOfPlayers - 2:
			# auto choose victim
			for playerNumber in range(numberOfPlayers):
				if players[playerNumber].hasDied == False and playerNumber != turnPlayer: 
					print('Because there is only one other player left, you must attack Player {}'.format(playerNumber + 1))
					victim = playerNumber
		else:
			# player inputs which player to attack. Must be between 1 and numberOfPlayers. Must not be themselves or dead
			while victim < 0 or victim > numberOfPlayers - 1:
				print('Choose which player would you like to attack')
				try:
					victim = int(input())
				except ValueError:
					print('Invalid input: Needs to be an integer (It also needs to be between 1 and {})'.format(numberOfPlayers))
					victim = numberOfPlayers + 2
					continue
				if victim < 1 or victim > numberOfPlayers:
					print('Invalid input: Needs to be an integer be between 1 and {}'.format(numberOfPlayers))
					victim = numberOfPlayers + 2
					continue
				if victim == turnPlayer + 1:
					print('You cannot attack yourself!')
					victim = numberOfPlayers + 2
					continue
				if players[victim - 1].hasDied == True:
					print('You cannot attack a dead player!')
					victim = numberOfPlayers + 2
					continue
				victim = victim - 1

		# attacking hand gets decided
		if players[turnPlayer].deadHands == 2:
			print('You glitched the game and you lose')
		elif players[turnPlayer].deadHands == 1:
			# autochoose alive hand
			print('Because you have a dead hand, you must attack with your alive hand')
			for handNumber in range(2):
				if players[turnPlayer].hands[handNumber] != 0:
					TPchosenHand = handNumber
		elif players[turnPlayer].deadHands == 0:
			# player inputs which hand to attack with. Must be 1 or 2 and cannot be dead
			while TPchosenHand != 0 and TPchosenHand != 1:
				print('Choose which hand you want to attack with')
				try:
					TPchosenHand = int(input())
				except ValueError:
					print('Invalid input: Needs to be an integer (It also needs to be either 1 or 2)')
					TPchosenHand = 3
					continue
				if TPchosenHand != 1 and TPchosenHand != 2:
					print('Invalid input: Needs to be either 1 or 2')
					continue
				TPchosenHand = TPchosenHand - 1

		# victim hand gets decided
		if players[victim].deadHands == 2:
			print('You glitched the game and you lose')
		elif players[victim].deadHands == 1:
			# autochoose alive hand
			print('Because the player you are attacking has a dead hand, you must attack their alive hand')
			for handNumber in range(2):
				if players[victim].hands[handNumber] != 0:
					victimHand = handNumber
		elif players[victim].deadHands == 0:
			# player inputs which hand to attack. Must be 1 or 2
			while victimHand != 0 and victimHand != 1:
				print('Choose which hand you want to attack')
				try:
					victimHand = int(input())
				except ValueError:
					print('Invalid input: Needs to be an integer (It also needs to be either 1 or 2)')
					victimHand = 3
					continue
				if victimHand != 1 and victimHand != 2:
					print('Invalid input: Needs to be either 1 or 2')
					continue
				victimHand = victimHand - 1
		
		# what will happen
		players[victim].tempHands[victimHand] = players[victim].hands[victimHand] + players[turnPlayer].hands[TPchosenHand]
		if players[victim].tempHands[victimHand] >= 5:
			players[victim].tempHands[victimHand] = players[victim].tempHands[victimHand] - 5
			
		# show what will happen
		for i in range(numberOfPlayers):
			tempStr = 'Player {}\'s hands: {}, {}'.format(i + 1, players[i].hands[0], players[i].hands[1])
			if i == victim:
				tempStr = tempStr + ' --> {}, {}'.format(players[i].tempHands[0], players[i].tempHands[1])
			print(tempStr)

		# ask if reset
		while TPisSureOfTurn != 'y' and TPisSureOfTurn != 'n':
			print('Are you sure of your attack? Y or N')
			TPisSureOfTurn = input().lower()
			if TPisSureOfTurn != 'y' and TPisSureOfTurn != 'n': print('Invalid input')
		if TPisSureOfTurn == 'y':
			players[victim].hands[victimHand] = players[victim].tempHands[victimHand]
			
			# calculate deadhands
			players[victim].deadHands = 0
			for hand in players[victim].hands:
				if hand == 0:
					players[victim].deadHands = players[victim].deadHands + 1
			
			# check if victim has died
			if players[victim].deadHands == 2:
				print('Player {} has died!'.format(victim + 1))
				players[victim].hasDied = True
	elif TPcurrentAction == 's':
		while validSplit == False:
			# hand getting subtracted from gets decided
			if players[turnPlayer].deadHands == 2:
				print('You glitched the game and you lose')
			elif players[turnPlayer].deadHands == 1:
				# autochoose alive hand
				print('Because you have a dead hand, you must split with your alive hand')
				for handNumber in range(2):
					if players[turnPlayer].hands[handNumber] != 0:
						TPchosenHand = handNumber
			elif players[turnPlayer].deadHands == 0:
				# player inputs which hand to subtract from. Must be 1 or 2 and cannot be dead
				while TPchosenHand != 0 and TPchosenHand != 1:
					print('Choose which hand you want to subtract from')
					try:
						TPchosenHand = int(input())
					except ValueError:
						print('Invalid input: Needs to be an integer (It also needs to be either 1 or 2)')
						TPchosenHand = 3
						continue
					if TPchosenHand != 1 and TPchosenHand != 2:
						print('Invalid input: Needs to be either 1 or 2')
						continue
					TPchosenHand = TPchosenHand - 1
					if TPchosenHand == 0:
						TPunchosenHand = 1
					else: 
						TPunchosenHand = 0

			# amount getting subtracted gets decided. Must be between 1 and hand
			while amountGettingSubtactedSplitting < 1 or amountGettingSubtactedSplitting > players[turnPlayer].hands[TPchosenHand]:
					print('Decide how much you want to subtract from this hand')
					try:
						amountGettingSubtactedSplitting = int(input())
					except ValueError:
						print('Invalid input: Needs to be an integer (It also needs to be between 1 and 4)')
						amountGettingSubtactedSplitting = 6
						continue
					if amountGettingSubtactedSplitting < 1 or amountGettingSubtactedSplitting > players[turnPlayer].hands[TPchosenHand]:
						print('Invalid input: Needs to be between 1 and your hand')
						continue

			# what will happen
			players[turnPlayer].tempHands[TPchosenHand] = players[turnPlayer].hands[TPchosenHand] - amountGettingSubtactedSplitting
			players[turnPlayer].tempHands[TPunchosenHand] = players[turnPlayer].hands[TPunchosenHand] + amountGettingSubtactedSplitting
			for tempHandNumber in range(2):
				if players[turnPlayer].tempHands[tempHandNumber] >= 5:
					players[turnPlayer].tempHands[tempHandNumber] = players[turnPlayer].tempHands[tempHandNumber] - 5

			# check if hands are the same after split
			for handNumber in range(2):
				for handNumber1 in range(2):
					if players[turnPlayer].tempHands[handNumber] == players[turnPlayer].hands[handNumber1]:
						splitSameHandCount = splitSameHandCount + 1

			# reset back to beginning if hands are the same
			if splitSameHandCount == 2:
				print('Because this split leads to just switching the hands, please retry the split')
				TPchosenHand = 3
				TPunchosenHand = 3
				amountGettingSubtactedSplitting = 0
				validSplit = False
				splitSameHandCount = 0
			elif splitSameHandCount < 2:
				validSplit = True
			
			# calculate future dead hands
			players[turnPlayer].tempDeadHands = 0
			for tempHand in players[turnPlayer].tempHands:
				if tempHand == 0:
					players[turnPlayer].tempDeadHands = players[turnPlayer].tempDeadHands + 1
			
			# reset if a hand has died and if killViaSplit is off
			if players[turnPlayer].tempDeadHands > players[turnPlayer].deadHands and allowKillViaSplit == 'n':
				print('Because this split leads to killing a hand, please retry the split')
				TPchosenHand = 3
				TPunchosenHand = 3
				amountGettingSubtactedSplitting = 0
				validSplit = False
				splitSameHandCount = 0
			else:
				validSplit = True

		# show what will happen
		for i in range(numberOfPlayers):
			tempStr = 'Player {}\'s hands: {}, {}'.format(i + 1, players[i].hands[0], players[i].hands[1])
			if i == turnPlayer:
				tempStr = tempStr + ' --> {}, {}'.format(players[i].tempHands[0], players[i].tempHands[1])
			print(tempStr)
		
		# ask if reset
		while TPisSureOfTurn != 'y' and TPisSureOfTurn != 'n':
			print('Are you sure of your split? Y or N')
			TPisSureOfTurn = input().lower()
			if TPisSureOfTurn != 'y' and TPisSureOfTurn != 'n': print('Invalid input')
		if TPisSureOfTurn == 'y':
			for handNumber in range(2): 
				players[turnPlayer].hands[handNumber] = players[turnPlayer].tempHands[handNumber]

			# calculate deadhands
			players[turnPlayer].deadHands = 0
			for hand in players[turnPlayer].hands:
				if hand == 0:
					players[turnPlayer].deadHands = players[turnPlayer].deadHands + 1

			# check if turn player has died
			if players[turnPlayer].deadHands == 2:
				print('Player {} has killed themselves! (What a dumbass)'.format(turnPlayer + 1))
				players[turnPlayer].hasDied = True
			
	# calculate dead players
	deadPlayers = 0
	for player in players:
		if player.hasDied == True:
			deadPlayers = deadPlayers + 1
					
	if deadPlayers == numberOfPlayers - 1: 
		gameOver = True
		continue
	
	# next turn
	if TPisSureOfTurn == 'y':
		turnPlayer = turnPlayer + 1
		if turnPlayer > numberOfPlayers - 1:
			turnPlayer = 0
		while players[turnPlayer].hasDied == True:
			turnPlayer = turnPlayer + 1
			if turnPlayer > numberOfPlayers - 1:
				turnPlayer = 0
	for player in players:
		for handNumber in range(2):
			player.tempHands[handNumber] = player.hands[handNumber]
	TPcanSplit = ''
	TPcurrentAction = ''
	victim = numberOfPlayers + 2
	victimHand = 3
	TPchosenHand = 3
	TPunchosenHand = 3
	TPisSureOfTurn = ''
	amountGettingSubtactedSplitting = 0
	validSplit = False
	splitSameHandCount = 0
	firstSplitChecker = 0
	
if gameOver == True:
	for playerNumber in range(numberOfPlayers):
		if players[playerNumber].hasDied == False:
			print('Player {} wins!'.format(playerNumber + 1))