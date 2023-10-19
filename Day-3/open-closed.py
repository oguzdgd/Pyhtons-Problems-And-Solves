
"""The store is open every day from 10 to 21, except on Saturday and Sunday.

The given program takes the day and the hour as input.

Task
Complete the program to output whether a store is Open or Closed, based on the day of the week and the hour.

The day of the week is represented as an integer (1 for Monday, 2 for Tuesday, etc.)"""


day = int(input())
hour = int(input())

# Mağaza saatleri kontrolü
if day == 6 or day == 7 or hour < 10 or hour >= 21:
    print("Closed")
else:
    print("Open")