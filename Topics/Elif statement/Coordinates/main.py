x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("It's the origin!")
elif x == 0 or y == 0:
    print("One of the coordinates is equal to zero!")
else:
    xp = x > 0  # xp = x is positive
    yp = y > 0  # yp = y is positive
    quadrant = ""

    if xp:
        quadrant = "I" if yp else "IV"
    else:
        quadrant = "II" if yp else "III"

    print(quadrant)
