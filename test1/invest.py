principal = int(input("Enter Principal amount"))
rate = float(input("Enter Rate of interest"))
year = int(input("Enter number of years"))

def invest(principal,rate,year):
    for y in range(1,year + 1):
        principal = principal + principal*rate
        print(f"year {y}: ${principal:.2f}")
        
invest(principal,rate,year)
