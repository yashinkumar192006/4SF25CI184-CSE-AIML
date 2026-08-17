import random
ranks=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suits=["Hearts","Diamonds","Clubs","Spades"]

def create_deck():
    return[f"{rank} of {suit}" for suit in suits for rank in ranks]

def no_of_players():
    while True:
        Number=input("Enter no.of Players :").strip()
        try:
            num_players=int(Number)
        except ValueError :
            print("Invalid input.Please enter a valid whole number.")
            continue
        if num_players <=0:
            print("Number of Players cannot be less tahn or equal to Zero.")
            continue
        if num_players >52:
            print("You cannot enter more than 52 players.")
            continue

        cards_per_player=52// num_players
        if cards_per_player==0:
            print("More players than 52 not possible.")
            continue

        return num_players , cards_per_player

def deal_cards(deck,num_players,cards_per_player):
    hand={}
    for player in range(1,num_players+1):
        start=(player-1)*cards_per_player
        end=start+cards_per_player
        hand[player]= deck[start:end]

    return hand

def round_winner(num_players,cards_played):
    while True:
      Player=input(f"Which player won this round? (1-{num_players}): ").strip()
      try:
          winner=int(Player)
      except ValueError:
          print("Invalid input. Please enter a player number.")
          continue
      if winner not in cards_played:
        print(f"Invalid player number. Choose between 1 and {num_players}.")
        continue
      
      return winner


def play_game():
    print("------Welcome to the Card Game------")

    deck=create_deck()
    random.shuffle(deck)

    num_players,cards_per_player = no_of_players()
    hand = deal_cards(deck, num_players, cards_per_player)

    scores = {}
    for player in range(1, num_players + 1):
        scores[player] = 0
    print(f"\nEach player gets {cards_per_player} cards. Let's begin!\n")

    for round_num in range(1, cards_per_player + 1):
        print(f" Round {round_num} ")

        cards_played = {}
        for player in range(1, num_players + 1):
            card = hand[player].pop()
            cards_played[player] = card
            print(f"Player {player} plays: {card}")

        winner = round_winner(num_players, cards_played)
        scores[winner] = scores[winner] + 1
        print(f"Player {winner} wins Round {round_num}!\n")


    print("--- Final Scores ---")
    for player in range(1, num_players + 1):
        print(f"Player {player}: {scores[player]} round(s) won")

    highest_score = 0
    for player in range(1, num_players + 1):
        if scores[player] > highest_score:
            highest_score = scores[player]

    winners = []
    for player in range(1, num_players + 1):
        if scores[player] == highest_score:
            winners.append(player)

    print("\n=== Game Over ===")
    if len(winners) == 1:
        print(f"Player {winners[0]} wins the game with {highest_score} round(s) won!")
    else:
        tied = ""
        for i in range(len(winners)):
            tied = tied + str(winners[i])
            if i < len(winners) - 1:
                tied = tied + ", "
        print(f"It's a tie between players {tied}, each with {highest_score} round(s) won!")

if __name__ == "__main__":
    play_game()
