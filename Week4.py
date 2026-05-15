The random walk:

The hashes (#) represent the "walk", this program will start at the origin (0, 0).
It will then choose a random movement from (1 -> 4).
  1 : up
  2 : down
  3 : left
  4 : right
Depending on the direction, it will "move" to the next coordinate.

IF direction IS 4 (right):
  0 1 2 ... 8 9
0 S # . ... . .
1 . . . ... . .
2
...
9

THEN IF direction IS 2 (down):
  0 1 2 ... 8 9
0 S # . ... . .
1 . # . ... . .
2
...
9

Eventually, it should look like this:

  0 1 2 3 4 5 6 7 8 9
0 S # # # # . . . . .
1 . . . . # # # . . .
2 . # # # # # # # # #
3 . # # # # . # # E #
4 . # # # # # # # # #
5 # # . . # # # # # #
6 # . # # # # # . . .
7 # # # # # . . . . .
8 # # # # # # . . . .
9 # # # # # # . . . .

S represents the Starting point, while E represents the End point.
Note: The program must end once there are no longer any legal moves.

  0 1 2 3 4 5 6 7 8 9
0 S # # . . . . . . .
1 # E # . . . . . . .
2 # # # . . . . . . .
3 . . . . . . . . . .
4 . . . . . . . . . .
5 . . . . . . . . . .
6 . . . . . . . . . .
7 . . . . . . . . . .
8 . . . . . . . . . .
9 . . . . . . . . . .
