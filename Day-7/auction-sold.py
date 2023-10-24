
maxBid = 0

while True:
    bid = input("Enter a bid or press 'q' to quit: ")
    
    if bid == "q":
        break
    
    bid = int(bid)
    
    if bid > maxBid:
        maxBid = bid

print("Sold:", maxBid)