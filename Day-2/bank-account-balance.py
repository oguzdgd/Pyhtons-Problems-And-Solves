balance = int(input())
withdraw = int(input())

if(balance>=withdraw):
    balance-=withdraw
else:
    print("Bakiyeniz yetersiz")
print("Your balance: " +str(balance))