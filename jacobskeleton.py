Players
	One
		hands
			[1,1]
		deadHands
			1
	Two
		hands
			[1,1]
		deadHands
			1	
Do the players allow killing hands via splitting?
	
check if turn player cannot split?		
	if both hands are dead
		they glitched the game and they lose cause my code is perfect
	if one hand is dead and the other is 1
		turn player cannot split
	if killing hands via splitting is not allowed
		 if one hand is one and the other hand is < 3
			turn player cannot split
if turn player can split
	choose between attack or split
else
	auto attack

if attack
	check turn hands for dead hands
		if both hands are dead
			they glitched the game and they lose cause my code is perfect
		if one hand is dead
			auto choose hand
		if no hands are dead
			let turn player choose hand
	chosen hand will be attack hand
	check victim hands for dead hands
		if both hands are dead
			they glitched the game and they lose cause my code is perfect
		if one hand is dead
			auto choose hand
		if no hands are dead
			let turn player choose hand
	chosen hand will be victim hand
			show the aftermath
		if not auto turn
			check if player is sure
				if player is sure
					add turn hand to victim hand
				else
					end turn and do not change turn player
	check opponent hands for both dead
		if opponent hands are both dead
			turn player wins
		else
			next turn
if split
	check turn hands for dead hands
		if both hands are dead
			they glitched the game and they lose cause my code is perfect
		if one hand is dead
			auto choose alive hand
		if no hands are dead
			let turn player choose hand
	
	
	
	[0,0] 
	[0,1] 
	[0,2] 
	[0,3] 
	[0,4] 
	[1,1] 
	[1,2] 
	[1,3] 
	[1,4] 
	[2,2] 
	[2,3] 
	[2,4] 
	[3,3]
	[3,4] 
	[4,4] 