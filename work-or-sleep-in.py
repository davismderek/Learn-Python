day = int(input('Day (0-6)? '))
if (day == 0) or (day == 6):
    print("Sleep in")
elif (day <= 5) and (day >= 1):
    print("Go to work!")
else: 
    print("Yuu didn't listen, I said 0-6.")