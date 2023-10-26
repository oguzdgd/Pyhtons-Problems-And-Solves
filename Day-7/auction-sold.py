"""Going Once, Going Twice, Sold!
You are writing a program for an auction where the maximum bid is set. The number of bids is variable.

Task
Complete the program to take all bids from auction participants until the maximum bid is met.

The program should output a message with the winning bid.

Input Example
1600
800
1300
1700

Output Example
Sold: 1700"""

maxBid = 0

while True:
    bid = input("Enter a bid or press 'q' to quit: ")
    
    if bid == "q":
        break
    
    bid = int(bid)
    
    if bid > maxBid:
        maxBid = bid

print("Sold:", maxBid)