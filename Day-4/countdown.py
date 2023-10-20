"""
Task
Create a timer program that will take the number of seconds as input, and countdown to 0.

Input Example
3
Output Example
3
2
1
0  """
number = int(input())

while number >= 0:
    print(number)
    number -= 1

