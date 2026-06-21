import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choices(friends))
print(friends[random.randint(0, len(friends))])
