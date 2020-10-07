import math


ini_share = 5
ini_tot_share = 3
days = 5
try:
    days = int(input("Enter number of days in integer: "))
except:
    print("\nWrong input. Integer was not given as input.\n\nDefault 5 days value is given as output.")

cumulative=0

if days > 50:
    days =50
    print("You cant go above 50 days for input. So you are being shown for 50 days.")
    
print("Format: Day - Shared - Liked - Cumulative")
for i in range(days):
    if i == 0:
        like = math.floor( ini_share /2)
        cumulative = like
    else:
        ini_share = math.floor( ini_share /2)*ini_tot_share
        like = math.floor( ini_share /2)
        cumulative = cumulative + like

    print(i+1,'-', ini_share,'-', like,'-',cumulative)

