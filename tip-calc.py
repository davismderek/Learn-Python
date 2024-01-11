bill = input("Total bill amount? ")
servicelevel = input("Level of service? Please write 'Good', 'Fair', or 'Bad': ")
if servicelevel == "Good":
    tip = (float(bill)) * (float(.20))
    tiprounded = ("%.2f" % tip)
    total = tip + float(bill) 
    totalrounded = ("%.2f" % total)
    print("Tip Amount: $" + (str(tiprounded)))
    print("Total Amount: $" + str(totalrounded))


elif servicelevel == "Fair":
    tip = (float(bill)) * (float(.15))
    tiprounded = ("%.2f" % tip)
    total = tip + float(bill)
    totalrounded = ("%.2f" % total)
    print("Tip Amount: $" +  (str(tiprounded)))
    print("Total Amount: $" + str(totalrounded))

elif servicelevel == "Bad":
    tip = (float(bill)) * (float(.10))
    tiprounded = ("%.2f" % tip)
    total = tip + float(bill)
    totalrounded = ("%.2f" % total)
    print("Tip Amount: $" + (str(tiprounded)))
    print("Total Amount: $" + str(totalrounded))