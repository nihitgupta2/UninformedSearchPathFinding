# UninformedSearchPathFinding

In assignment 1 you implemented a random search for the 25 × 25 two-dimensional maze problem:
Assume a 25 × 25 two-dimensional maze. Each square in the maze has an (x,y) coordinate, with the bottom-left corner being (0,0) and the top-right corner being (24,24). Each position in the maze can be either empty or blocked. In addition, there are two “special” positions, the starting position and the exit position.
The agent can only move up, down, left or right, but never diagonally. It also cannot enter blocked positions or move outside the maze. Its objective is to find a path from its starting position (S) to an exit position (E1 or E2), preferably the cheapest one. The cost of a path is the number of positions the agent has to move through, including the starting and exit position. The map of the maze is given in the figure below.

![image](https://user-images.githubusercontent.com/118135114/209768767-9583a7c3-deb8-4bda-932d-2925705e84ca.png)


Implement a code to find a path from the starting position to an exit position using (1) Breath-First Search, and (2) Depth-First Search. Assume two different orders for tie breaking: (1) LEFT, UP, RIGHT, DOWN, (2) RIGHT, UP, LEFT, DOWN. Ignore repeated states.
Your implementation should output information about the search, including, which exit is found, the complete path (show the path on the maze map), its cost, and the number of nodes explored (or squares checked) before finding it.
