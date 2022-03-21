import random

class Player:
    def __init__(self, name):
        self.name = name


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randrange(1, self.sides, 1)


if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    die = Die(6)
    player1_score = 0
    player2_score = 0
    while player1_score < 100 or player2_score < 100:
        player1_turn_score = 0
        player2_turn_score = 0
        print("Player 1 is rolling")
        first_roll = die.roll()
        if first_roll == 1:
            player1_turn_score = 0
            print(f"Player 1 rolls a {first_roll}, their score for the turn is {player1_turn_score}, and their total score is {player1_score}")
        else:
            player1_turn_score += first_roll
            print(f"Player 1 rolls a {first_roll}, their score for the turn is {player1_turn_score}, and their total score is {player1_score}.")
            decision = input("Will Player 1 roll (r) or hold (h)?")
            if decision == 'r':
                pass
            else:
                player1_score += player1_turn_score
                print("Player 2 is rolling")
                second_roll = die.roll()
                if second_roll == 1:
                    player2_turn_score = 0
                    print(f"Player 2 rolls a {second_roll}, their score for the turn is {player2_turn_score}, and their total score is {player2_score}")
                else:
                    player2_turn_score += second_roll
                    print(f"Player 2 rolls a {second_roll}, their score for the turn is {player2_turn_score}, and their total score is {player2_score}.")
                    decision2 = input("Will Player 2 roll (r) or hold (h)?")
                    if decision2 == 'r':
                        pass
                    else:
                        player2_score += player2_turn_score
    print(f"The final score is Player1: {player1_score} and Player2: {player2_score}")
