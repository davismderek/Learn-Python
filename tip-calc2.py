bill = float(input("Total bill amount? "))
servicelevel = input("Level of service? Please write 'Good', 'Fair', or 'Bad': ")
split = int(input("Split how many ways? "))

# def tipCalc(): pass
if servicelevel == "Good":
    tip = bill * .20
    tiprounded = ("%.2f" % tip)
    total = tip + bill 
    totalrounded = ("%.2f" % total)
    print("Tip Amount: $" + (str(tiprounded)))
    print("Total Amount: $" + str(totalrounded))
    perperson = (float(totalrounded) / split)
    print("Amount per person: $" + str(perperson))

elif servicelevel == "Fair":
    tip = bill * .15
    tiprounded = ("%.2f" % tip)
    total = tip + bill
    totalrounded = ("%.2f" % total)
    print("Tip Amount: $" +  (str(tiprounded)))
    print("Total Amount: $" + str(totalrounded))
    perperson = (float(totalrounded) / split)
    print("Amount per person: $" + str(perperson))

elif servicelevel == "Bad":
    tip = bill * .10
    tiprounded = ("%.2f" % tip)
    total = tip + bill
    totalrounded = ("%.2f" % total)
    print("Tip Amount: $" + (str(tiprounded)))
    print("Total Amount: $" + str(totalrounded))
    perperson = (float(totalrounded) / split)
    print("Amount per person: $" + str(perperson))
