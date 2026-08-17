Problem Statement
Create a multi-player card game that simulates round-based competition between players. Each player receives an equal number of cards, and they compete across multiple rounds. The player who wins the most rounds becomes the overall winner.

Requirements
Game Setup
Create a standard deck of 52 cards (13 ranks × 4 suits)
Shuffle the deck randomly
Accept user input for number of players
Distribute cards evenly among all players

Gameplay Mechanics
Play rounds equal to the number of cards each player has
In each round, randomly select one card from each player's hand
Display all cards played in the current round
Accept user input to determine the round winner
Track scores for each player across all rounds

Game Completion
Continue until all cards are played
Calculate final scores
Announce the player with the highest number of rounds won

Input/Output Specifications

Input
Number of players (positive integer)
Round winner selection (player number: 1, 2, 3, ...)

Output
Round number display
Cards played by each player in the current round
Final game result with winner announcement

Technical Constraints
Use list comprehension for deck creation
Implement random card selection from each player's hand
Handle invalid inputs with proper error messages
Ensure fair card distribution (equal cards per player)
