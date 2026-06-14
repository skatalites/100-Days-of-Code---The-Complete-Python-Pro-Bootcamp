print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    day = int(input("What is the number of the day? "))
    if day >= 5 or day <= 7:
        print("Weekday costs: 5")
    else:
        print("Weekend costs: 4")
else:
    print("Sorry you have to grow taller before you can ride.")
