import random
from art import logo, vs
from game_data import data

def formating_data(acc):
    """Takes the account data returns into printable."""
    return f"Compare A: {acc['name']}, a {acc['description']}, from {acc['country']}"

print(logo)

game_score = 0
game_over = False

compare_A = {}
compare_B = {}

compare_A = random.choice(data)
compare_B = random.choice(data)
if compare_A == compare_B:
    compare_B = random.choice(data)


while not game_over:
    print("Compare A: " + formating_data(compare_A))
    print(vs)
    print("Against B: " + formating_data(compare_B))

    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()


    if user_input == 'A' and compare_A['follower_count'] > compare_B['follower_count'] \
            or user_input == 'B' and compare_A['follower_count'] < compare_B['follower_count']:
        game_score += 1
        print(f"You are right! Current score {game_score}")
        compare_A = compare_B
        compare_B = random.choice(data)
    else:
        print(f"Sorry that's wrong. Final score: {game_score}")
        print(f"{compare_A['name']} has {compare_A['follower_count']} millions and {compare_B['name']} has {compare_B['follower_count']} millions followers!")
        game_over = True
