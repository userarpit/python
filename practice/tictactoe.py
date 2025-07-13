from random import randint
player_win_combination={(1,2):3,(1,3):2,(1,4):7,(1,7):4,(2,5):8,(2,8):5,(3,6):9,(3,9):6,(4,5):6,
                      (4,6):5,(4,7):1,(5,6):4,(5,8):2,(6,9):3,(7,8):9,(7,9):8,(8,9):7,
                      (1,5):9,(1,9):5,(5,9):1,(3,5):7,(3,7):5,(5,7):3}

def draw_board(pos,value_list):
    """
    draw the board
    """
    print("   |   |   ")
    print(f" {value_list[0]} | {value_list[1]} | {value_list[2]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {value_list[3]} | {value_list[4]} | {value_list[5]}  ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {value_list[6]} | {value_list[7]} | {value_list[8]}  ")
    print("   |   |   ")

def get_input():
    while True:
        invalid_input = False
        try:
            pos = int(input("Please select a position to place an 'X' (1-9) : "))
        except ValueError:
            print("Invalid Input")
            invalid_input = True
        if invalid_input:
            continue
        elif pos not in list(range(1,10)):
            print("Please enter number between 1 and 9")
            continue
        else:
            break
    return pos

def user_turn(value_list,record_user_input):
    while True:
        user_pos = get_input()
        if value_list[user_pos - 1] == ' ':
            break
    value_list[user_pos - 1] = 'X'
    record_user_input.append(user_pos)
    record_user_input.sort()
    draw_board(user_pos,value_list)
    return record_user_input

def check_if_user_winning(computer_pos, value_list,record_user_input):
    if len(record_user_input) > 1:
        res = [(a, b) for idx, a in enumerate(record_user_input) for b in record_user_input[idx + 1:]]
        for x in res:
            if x in player_win_combination:
                if value_list[player_win_combination[x]-1] == " ":
                    return player_win_combination[x]
        return computer_pos        
    else:
        return computer_pos

def check_if_computer_winning(computer_pos, value_list,record_computer_input):
    if len(record_computer_input) > 1:
        res = [(a, b) for idx, a in enumerate(record_computer_input) for b in record_computer_input[idx + 1:]]
        for x in res:
            if x in player_win_combination:
                if value_list[player_win_combination[x]-1] == " ":
                    return player_win_combination[x]
        return computer_pos        
    else:
        return computer_pos

def computer_turn(value_list,record_user_input,record_computer_input):
    while True:
        computer_pos = randint(1,9)
        if value_list[computer_pos-1] == ' ':
            break
    
    computer_pos = check_if_user_winning(computer_pos,value_list,record_user_input)
    computer_pos = check_if_computer_winning(computer_pos,value_list,record_computer_input)
    value_list[computer_pos - 1] = 'O'
    record_computer_input.append(computer_pos)
    record_computer_input.sort()
    print(f"Computer placed 'O' at {computer_pos}")
    draw_board(computer_pos,value_list)

def check_win(player,value_list):
    match player:
        case "user":
            if (value_list[0] == value_list[1] == value_list[2] == 'X'):
                return True    
            if (value_list[3] == value_list[4] == value_list[5] == 'X'):
                return True
            if (value_list[6] == value_list[7] == value_list[8] == 'X'):
                return True
            if (value_list[0] == value_list[3] == value_list[6] == 'X'):
                return True
            if (value_list[1] == value_list[4] == value_list[7] == 'X'):
                return True
            if (value_list[2] == value_list[5] == value_list[8] == 'X'):
                return True
            if (value_list[0] == value_list[4] == value_list[8] == 'X'):
                return True
            if (value_list[2] == value_list[4] == value_list[6] == 'X'):
                return True    
        case "computer":
            if (value_list[0] == value_list[1] == value_list[2] == 'O'):
                return True    
            elif (value_list[3] == value_list[4] == value_list[5] == 'O'):
                return True
            elif (value_list[6] == value_list[7] == value_list[8] == 'O'):
                return True
            elif (value_list[0] == value_list[3] == value_list[6] == 'O'):
                return True
            elif (value_list[1] == value_list[4] == value_list[7] == 'O'):
                return True
            elif (value_list[2] == value_list[5] == value_list[8] == 'O'):
                return True
            elif (value_list[0] == value_list[4] == value_list[8] == 'O'):
                return True
            elif (value_list[2] == value_list[4] == value_list[6] == 'O'):
                return True    

def check_tie(value_list):
    if ' ' not in value_list:
        return True
    return False

def start_game():
    record_user_input = []
    record_computer_input = []
    print("Welcome to Tic Tac Toe")
    value_list = [' '] * 9
    draw_board(0,value_list)
    while True:
        record_user_input = user_turn(value_list,record_user_input)
        status = check_win("user",value_list)
        if status:
            print("you win")
            break

        if check_tie(value_list):
            print("it's a draw")
            break

        computer_turn(value_list,record_user_input,record_computer_input)
        status = check_win("computer",value_list)
        if status:
            print("computer win")
            break
    choice = input("Do you want to play again Y/N - ")
    if choice.lower() == 'y':
        start_game()

if __name__ == "__main__":
    start_game()