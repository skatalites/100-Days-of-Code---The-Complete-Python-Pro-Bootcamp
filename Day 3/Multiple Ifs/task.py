import random
import string

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age >= 30 and age <= 50:
        combo = input("We have a special combo for this week $5 and 20% discount if you have kids playing in kids attraction, y or n")
        if combo:
            print("Please pay $5.")
            num = random.randint(1, 100)
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=num))
            print(f"Please pay $5, and present this discount code {random_string}")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
