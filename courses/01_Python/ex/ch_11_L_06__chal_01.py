#WORKS 6/2/2026

# #GOTCHA-#SOLVED: The tests all 3 failed although the correct message printed. The solution was to `return` the status string from get_status_message() instead of printing it outright.

GAME_DIFFICULTY = "normal"


def set_game_difficulty(new_level):
    global GAME_DIFFICULTY
    GAME_DIFFICULTY = new_level


def get_status_message(player_name):
    return (f"{player_name} is playing on {GAME_DIFFICULTY} difficulty")


# TESTING #


print(get_status_message("Alice"))
# "Alice is playing on normal difficulty"

set_game_difficulty("hard")
print(get_status_message("Bob"))
# "Bob is playing on hard difficulty"

set_game_difficulty("easy")
print(get_status_message("Cara"))
# "Cara is playing on easy difficulty"