# AI_Project
## connect 4 game with python  "minmax algorithm"


This project was for a course in the university. The code implements a Connect Four game with an AI opponent using the minimax algorithm with alpha-beta pruning. It initializes a 6x7 game board and allows two players: a human and an AI.

The drop function places a piece on the board, while validation checks if a column is available for a move. The win function detects if a player has won by checking all possible win conditions. The minimax function calculates the best possible move for the AI by evaluating board positions and potential future moves. The game alternates between the human and AI players, printing the board after each move, and ends when a player wins or there are no valid moves left.

The difficulty level of the game can be adjusted by changing the numeric values in the if conditions within the evaluate_window function, which influence the scoring of different board states.
