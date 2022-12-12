#AI Final project: Tic-Tac-Toe 

#Implementation of Tic Tac Toe 

##Introduction:

Artificial intelligence (or AI) is a computer program that can intelligently respond to the player’s moves. This game doesn’t introduce any complicated new concepts. 
Two people play Tic Tac Toe against each other, and it is a 3 x 3 grid. One player is X, and the other player is O. Players take turns placing their X or O. 

If a player gets three of their marks on the board in a row, column, or one of the two diagonals, they win. When the board fills up with neither player winning, the game ends in a draw.

##Programming Language:

We will be using the python programming language (version 3.7) to build this project. The advantages of using python AI-based projects include less code, flexibility, simplicity, and consistency, and access to great libraries and frameworks for AI and its platform independence. 

##Algorithms used:

We have created four Agents to play against each other.
1. Minimax Agent
2. Alpha beta Minimax Agent
3. Expectimax Agent
4. Q-Learning Agent

Minimax Algorithm: Minimax is a type of backtracking algorithm used in game theory and decision-making to determine a player's best course of action, provided that your opponent is likewise playing well. In two-player turn-based games like Tic-Tac-Toe, it is frequently utilized. The two participants in Minimax are referred to as the maximizer and minimizer. The maximizer strives to achieve the maximum score, whereas the minimizer strives to achieve the lowest score.

Alpha-Beta Minimax Algorithm: A modified variant of the minimax method is alpha-beta pruning. It is a minimax algorithm optimization approach. The Alpha-beta pruning to a standard minimax algorithm yields the same move as the regular approach, but it eliminates all the nodes that are merely slowing down the algorithm without having any significant bearing on the result. Thus, by cutting these nodes, the algorithm becomes quick. 

Expectimax Algorithm: A game theory approach used to maximize expected utility is called the Expectimax search algorithm. It uses a Minimax algorithm variant. Expectimax does not assume made by Minimax that the opponent (the minimizer) performs optimally. This is helpful for simulating circumstances where adversarial agents behave haphazardly or inefficiently.

Q-Learning Algorithm: Q-Learning is a reinforcement-based algorithm where initially agent has no idea about the environment. It learns about the environment by playing a few games and getting rewards. By obtaining rewards agents realize which move is good and which is not. This Agent should be trained in the game environment before it can be played with other players in the tournament.

##Instructions to run code:

Run the file tictactoe.py 

Enter agent1 and agent2 as shown in the console and select each algorithm and see how the agents play.

Make sure you select 2 different agents for the Tic-Tac-Toe game.

Run multiple times and check with multiple agents to compare which agent plays the game better.
