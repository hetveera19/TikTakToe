actual_board={7:'',8:'',9:'',4:'',5:'',6:'',1:'',2:'',3:''}
win_positions=[[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[7,5,3]]
isGameTied=False
winningPlayer=''

def create_tiktaktoe_board():
    count = 3
    string = ''
    for value in actual_board:
        if count != 0:
            if count - 1 != 0:
                string = string + str(value) + ' | '
                count = count - 1
            else:
                string = string + str(value)
                count = count - 1
        else:
            print(string)
            string = ''
            string = str(value) + ' | '
            count = 2
    print(string)


def display_tiktaktoe_board():
    count = 3
    string = ''
    for value in actual_board:
        if count != 0:
            if count - 1 != 0:
                string = string + actual_board[value] + ' | '
                count = count - 1
            else:
                string = string + actual_board[value]
                count = count - 1
        else:
            print(string)
            string = ''
            string = actual_board[value] + ' | '
            count = 2
    print(string)

def enter_mark_at_location(loc,mark):
    actual_board[loc]=mark
    display_tiktaktoe_board()

def input_location_to_enter_a_mark(mark):

    numbernotInputed = True
    while numbernotInputed:

        pos = input("Player "+ mark +" please enter a location to enter your mark from 1 to 9: ")
        if pos.isdigit():
            if actual_board.keys().__contains__(int(pos)):
                if actual_board[int(pos)] != '':
                    print("Location Entered has already been used. Please choose some other location")
                    numbernotInputed = True
                else:
                    numbernotInputed = False
                    return int(pos)
            else :
                print("Number or location entered is not in range. please enter a number between 1 and 9 inclusive")
                numbernotInputed=True
        else:
            print("Could not understand "+pos+" . Please enter a digit ")
            numbernotInputed=True

def check_if_player_won():
    global winningPlayer
    for posArray in win_positions:
        temp = ''
        index=0
        for position in posArray:
            temp+=actual_board[position]
        if temp=='XXX':
            winningPlayer='X'
            return True
        elif temp=='OOO':
            winningPlayer = 'O'
            return True
    return False




    #         if index==1:
    #             startingMark = actual_board[position]
    #             if startingMark=='':
    #                 gameWon=False
    #                 break
    #             index+=1
    #         else:
    #             if actual_board[position] == '':
    #                 gameWon = False
    #                 break
    #             if actual_board[position] in win_positions:
    #                 if startingMark == actual_board[position]:
    #                     if index==2:
    #                         gameWon = True
    #                         break
    #                     else:
    #                         index+=1
    #                 if startingMark != actual_board[position]:
    #                     gameWon = False
    #                     break
    #     if gameWon:
    #         winningPlayer=startingMark
    #         return gameWon
    #     else:
    #         index=1
    #         startingMark=''
    # return gameWon


print("Welcome to Tik Tak Toe !!")

playGame = input("Do you want to try it out? Y or N : ")

while playGame=='Y':
    create_tiktaktoe_board()

    print("Which player you want to be ? X or O? ")

    player1_input = input("Enter your preference: ")
    player2_input = ''
    if player1_input == 'X':
        player2_input = 'O'
    else:
        player2_input = 'X'

    print("Player 1 is :" + player1_input)
    print("Player 2 is :" + player2_input)
    marks_available = [player1_input, player2_input]
    markChance = 0
    positionToEnter = 0
    for chances in range(0, 9):
        if markChance == 1:
            positionToEnter = input_location_to_enter_a_mark(marks_available[markChance])
            enter_mark_at_location(positionToEnter, marks_available[markChance])
            if check_if_player_won():
                if winningPlayer == player1_input:
                    print("player 1 has won the game !!! Cheers!!!")
                    break
                else:
                    print("player 2 has won the game !!! Cheers!!!")
                    break
            markChance = 0
        else:
            positionToEnter = input_location_to_enter_a_mark(marks_available[markChance])
            enter_mark_at_location(positionToEnter, marks_available[markChance])
            if check_if_player_won():
                if winningPlayer == player1_input:
                    print("player 1 has won the game !!! Cheers!!!")
                    break
                else:
                    print("player 2 has won the game !!! Cheers!!!")
                    break
            markChance = 1
        if chances==8 and winningPlayer=='':
            print("The Game has Tied")
    if input("Do you want to try again? Y or N") == 'Y':
        actual_board = {7: '', 8: '', 9: '', 4: '', 5: '', 6: '', 1: '', 2: '', 3: ''}
        playGame = 'Y'
        winningPlayer=''
    else:
        playGame = 'N'

print("Thank you... Will see you Later!!!")





