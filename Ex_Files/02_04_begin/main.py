NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

# zip doesn't build a new list in memory.
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate
# The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
for i, name in enumerate(NAMES):
    print(f"{i} {name}")