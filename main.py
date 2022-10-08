result = int(input("Enter your mark: "))
if result <= 100:
    if result >= 80 :
        print("You got  A+")
    elif result >= 75:
        print('You got  A')
    elif result >= 70:
        print("You got  A-")
    elif result >= 65:
        print("You got  B+")
    elif result >= 60:
        print("You got  B")
    elif result >= 55:
        print("You got  B-")
    elif result >= 50:
        print("You got C+")
    elif result >= 45 :
        print("You got C")
    elif result >= 40 :
        print("You got D")
    elif result < 40 :
        print(" You fail")
else:
    print("something wrong")
