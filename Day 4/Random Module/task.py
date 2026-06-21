import random
import my_module

print(random.randint(-10, 0))
print(random.randint(0, 2))
print(random.randint(1, 1))
print(random.randint(-10, 10))

print(my_module.my_value)

#print(random.randint(10, -10)) #raise ValueError

print(random.random())
print(round(random.random()*5))

print(random.uniform(1, 10))
print(round(random.uniform(1, 10)))


random_value = random.randint(0,1)
print(random_value)
if random_value == 0:
    print(f"Tails: {random_value}")
else:
    print(f"Heads: {random_value}")


