import random
from game_data import data
import art

print(art.logo)

account_a = random.choice(data)
score = 0
lose = False
while not lose:
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {account_a['name']}, {account_a['description']},"
          f" {account_a['country']}")
    print(art.vs)
    print(f"Compare B: {account_b['name']}, {account_b['description']},"
          f" {account_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if guess == 'A' and account_a['follower_count'] > account_b['follower_count']:
        score += 1
        account_a = account_b
        print(f"You're right! Current score: {score}")
    elif guess == 'B' and account_a['follower_count'] < account_b['follower_count']:
        score += 1
        account_a = account_b
        print(f"You're right! Current score: {score}")
    else:
        print(f"You lose! Final score: {score}")
        lose = True


