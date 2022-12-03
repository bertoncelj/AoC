"""
A Rock 1 
B Paper 2
C Scissors 3

X Rock
Y Paper
Z Scissors

Lost 0
Draw 3
Win 6

X Lose
Y Draw
Z Win
"""

possible_games = {
    #draw
    "AX": 3,
    "BY": 3,
    "CZ": 3,
    # loss
    "AZ": 0,
    "BX": 0,
    "CY": 0,
    # win
    "AY": 6,
    "BZ": 6,
    "CX": 6,
}

response_value = {
    "X":1,
    "Y":2,
    "Z":3,
}

get_move = {
    # lose
    "X": { 
        "A": "Z", 
        "B": "X",
        "C": "Y",
    },
    # draw
    "Y": {
        "A": "X", 
        "B": "Y",
        "C": "Z",
    },
    # win
    "Z": {
        "A": "Y", 
        "B": "Z",
        "C": "X",
    },
}

test = [("A", "Y"), ("B", "X"), ("C", "Z")]

def get_all_games_played(input_file):
    file = open(input_file, "r")
    text = file.readlines()
    text = [a.rstrip('\n') for a in text]
    return list(map(lambda x: (x[0],x[2]), text))

def get_winner(ply1, ply2):
    return possible_games[ply1 + ply2]

def get_reponse_value(response):
    return response_value[response]

def get_game_resoult(ply1, ply2):
    return get_winner(ply1,ply2) + get_reponse_value(ply2)


def set_your_play(input):
    return [(game[0], get_move[game[1]][game[0]]) for game in input]

game_input = get_all_games_played("file2.txt")
print("day2_part_1: ", sum(map(lambda x: get_game_resoult(*x), game_input)))

my_moves = set_your_play(game_input)
print("day2_part_2: ", sum(map(lambda x: get_game_resoult(*x), my_moves)))
