"""
Smart Home 🏠
You’re making a voice recognition system.
The given code declares the list of supported commands.

Task
Complete the program to take a command as input, check if it's supported, and output "OK", if it is and "Unknown" if it's not.

Sample Input
Lights Off

Sample Output
OK
"""

supported = ["Lights off", "Lock the door", 
    "Open the door", "Make coffee", "Shut down"]

#your code goes here
command=input()

if command in supported:
    print("OK")
else:
    print("Unknown")