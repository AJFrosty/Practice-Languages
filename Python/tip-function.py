def tip(cost:float, percent:float) -> float:
    calc = (float(percent)/100) * float(cost)
    tip = calc + float(cost)
    print("The tip amount is $" + str(tip))
tip(100,20)