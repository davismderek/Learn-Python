bill = input("Total bill amount? ")
servicelevel = input("Level of service? Please write 'Good', 'Fair', or 'Bad': ")
tip = 0

if servicelevel == "Good":
    tip = (float(bill)) * (float(.20))

elif servicelevel == "Fair":
    tip = (float(bill)) * (float(.15))   

elif servicelevel == "Bad":
    tip = (float(bill)) * (float(.10))

tiprounded = ("%.2f" % tip)
total = tip + float(bill)
totalrounded = ("%.2f" % total)
print("Tip Amount: $" + (str(tiprounded)))
print("Total Amount: $" + str(totalrounded))