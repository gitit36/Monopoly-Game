##Net ID: sl5583
##Name: Sangjin Lee

##This game is Monopoly. N-number of players can play. The game is a board game where players develop properties
##and charge others for staying on his/her properties. The aim of this game is to win by staying on the game longer
##than other players without being driven into bankruptcy.


import random

def get_board(csv_file): # Creates the board. Returns the list that is the board. 
	board = open(csv_file)
	hdr = board.readline()
	board_list = []
	for line in board:
		line_split = line.strip().split(',')
		board_list.append(line_split)
	return board_list


def get_players(n): # Creates player start-up info. It returns the info of n-number of players.
	player = []
	player_s = []
	for i in range(n):
		player.append('Player' + ' ' + str(i + 1))                           
		player.append(0)	                         
		player.append(1500)		                     
		player_s.append(player)                      
		player = []			                         
	return player_s


def print_board(board, players): # print board
        for i in board:
                print(i[0]) 
                for p in players:
                        residency = "\tResidents: "
                        if p[1] == i[5]:
                                residency += p[0]
                                print(residency)
                if i[2] != '' and i[2] != 'bank':
                        print('\towner is:', i[2])
                        


def print_player(player, board): # printing individual player info.
        count = 0
        print("Player ", player[0])

        print("\tWallet:", player[2])

        i=0
        for j in board:
                j.append(i)
                i += 1                
        print("\tPosition:", end='')               
        for i in board:
                if player[1] == i[5]:
                        print(i[0])
                        
        print("\tProperties:", end='')
        for i in board:
                if player[0] == i[2]:
                        print(i[0])
        print()
                        

def dice_roll(): # rolling the dice
        dice_value = random.randint(1, 6) + random.randint(1,6)
        return dice_value


def move_player(player, board, dice_roll): # Moving the player around the board and adding the money everytime he/she passes GO.
	if (player[1] + dice_roll) / len(board) >= 1:
		player[2] += abs(board[0][4])
	player[1] = (player[1] + dice_roll) % len(board) 


def type_counter(player, board, tile_type): #counting types. Returns the count.
        count = 0
        for i in board:
                if i[2] == player[0] and tile_type == i[3]:
                        count += 1
        return count

board = get_board('monopoly.csv')

i=0
for j in board:
        j.append(i)
        i += 1

players = get_players(3)
current_player = 0
# This is the actual play of the monopoly game. It carries out whether the square is purchasable
# or not, if you have to pay for the rent, the conditions for the winner to be announced or the game to be over,
# basic layout that a player could choose from.
while True: 
        player = players[current_player]
        isEnd = False
        while True:
                choice = input(player[0] + ' [i: info, b: board, p: play, q: quit]: ')
                if choice == 'i':
                        print_player(player, board)
                elif choice == 'b':
                        print_board(board, players)
                elif choice == 'p':
                        dice = dice_roll()
                        move_player(player, board, dice)
                        for i in board:
                                if player[1] == i[5]:
                                        print('Welcome to ', i[0])
                                        if int(i[3]) > 0 and i[2] == 'bank' and player[2] >= int(i[1]): #if purchasable
                                                while True:
                                                        option = input('Would you like to buy [y/n]: ')
                                                        if option == 'y':
                                                                player[2] -= int(i[1])
                                                                i[2] = player[0]
                                                                break
                                                        elif option == 'n':
                                                                break
                                        elif int(i[3]) > 0 and i[2] != 'bank' and i[2] != '': #if you have to pay the rent
                                                if i[3] == '1':
                                                        rent = int(i[4])
                                                elif i[3] == '2':
                                                        for j in players:
                                                                if j[0] == i[2]:
                                                                        rent = 25*type_counter(j, board, '2')
                                                elif i[3] == '3':
                                                        for j in players:
                                                                if j[0] == i[2]:
                                                                        utility = type_counter(j, board, '3')
                                                                        if utility == 1:
                                                                                rent = 4*dice
                                                                        elif utility == 2:
                                                                                rent = 10*dice
                                                player[2] -= rent
                                                for j in players:
                                                        if j[0] == i[2]:
                                                                j[2] += rent
                        if player[2] < 0:
                                player[0] = 'DEAD'
                                for i in board:
                                        if i[2] == player[0]:
                                                i[2] = 'bank'

                        break
                elif choice == 'q':
                        print('The player has quit')
                        isEnd = True
                        break
        if isEnd == True:
                break
        count = 0
        for i in players:
                if i[0] != 'DEAD':
                        count += 1
                        winner = i
        if count == 1:
                print('Winner is: ' + winner[0])
                break
                
        while True:
                current_player += 1
                current_player %= 3
                if players[current_player][0] != 'DEAD':
                        break
                


