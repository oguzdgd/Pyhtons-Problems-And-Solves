"""A Word Game
The given code declares a list that holds the letters of the English alphabet.

Task
Complete the program to take 3 numbers as input and output letters from the array that correspond to those indexes.

Input Example
2
0
19
Output Example

CAT"""


alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
 "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
  "T", "U", "V", "W", "X", "Y", "Z"]

#your code goes here

for i in range(3):
  a=int(input())
  print(alpha[a],end='')
