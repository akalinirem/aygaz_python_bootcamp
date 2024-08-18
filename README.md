# Rock Paper Scissors Game

This Python application allows you to play the classic "Rock Paper Scissors" game with a graphical user interface using Tkinter.

## Features

- **Start Game**: You can start the game by clicking the "Play" button.
- **Selections**: Make choices of Rock, Paper, or Scissors.
- **Round Results**: Shows the result of each round and the winner.
- **End Game**: After the game ends, it reports the winner and asks if you want to play a new game.

## Requirements

- Python 3.x
- Tkinter (comes with Python)

## `GameApp` Class

- **`__init__(self, root)`**: Initializes the application. Creates the interface components.
- **`make_move(self, player_move)`**: Processes the player's move and updates the game.
- **`update_game_info(self, player_move, computer_move, result, result_color)`**: Updates game information and displays the result in color.
- **`tas_kagit_makas_iremnur_akalin(self)`**: Starts the game and presents the options to the user.
- **`update_tour_results(self)`**: Updates the round results.
- **`end_tour(self)`**: Processes the end of a round and shows the result.
- **`end_game(self)`**: Evaluates the game result and displays the outcome on the screen.
- **`ask_to_play_again(self)`**: Asks the user if they want to play a new game.
- **`reset_game(self)`**: Resets the game and starts it again.