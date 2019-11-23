# Connect 4

## Game Rules

I hope everyone knows the rules. You can find everything you need to know (here)[https://en.wikipedia.org/wiki/Connect_Four]

Basically there is 2 players: Red and Yellow. You goal is to get your tokens on the grid so that you have 4 of your tokens in a row, vertically, horizontally, or diagonally.

The tokens get staked onto a grid (7 wide, 6 high).

## Game Results

- If you win you earn 3 points
- If you draw you earn 1 point
- If you loose you do not get any point

## Code input

You can create as many functions as you wish but you need to have at least 2 set. These are going to be the ones I call

#### `__init__(self, mark)`

This will be called once per game per player. You will be informed which color you are: Red (`'r'`) or Yellow (`'y'`) as a String

#### `play(self, grid)`

This function will return the column you wish to play your token in.

You receive a grid of the current state of the game. It will be a 2D array of each slot. Each slot will contain one of these 3 values: `'r'`, `'y'`, `''` (all as String).

The first dimension of the list will be the different columns of the grid (7 of them).

The second dimension will be the rows among each column starting from the bottom(6 rows).

Take this grid as an example: ![Example grid](https://s3.eu-west-2.amazonaws.com/aigaming2/helpPagesAssets/Connect4/cn4Example1.png)
The correspondent input would be:
```
[
	['y', '', '', '', '', ''],
	['r', 'y', 'r', 'y', 'y', 'y'],
	['r', 'r', 'r', 'y', 'y', 'r'],
	['y', 'r', 'y', 'y', 'r', 'r'],
	['y', 'r', 'r', 'r', '', ''],
	['y', '', '', '', '', ''],
	['y', '', '', '', '', '']
]
```

## Submissions

Please submit your code by sending me this zipped folder with your code.

You can send them to `costelouis96@gmail.com`


## Final competition

At the end your code will be run against all the other players. I will have code to do all of this. Here is how I will run them.

You will be playing against all the other players. You will face each player 8 times (You will go first 4 times)

For each game a new instance of your class will be created. The initialization will not be timed.

The `play()` function will be timed. The average running time of this function will be recorded.

Your code will also be run in games where we expect errors to be raised.

You will be ranked based on your number of points, errors caught, and running time of your code. 

Initially the winner will be the one with the highest score. If there is a tie then it will be who caught the most errors. If there is a tie there again then it will be decided based on running time. Hopefully there is no more tie then.
