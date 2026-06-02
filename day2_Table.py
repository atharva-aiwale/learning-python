number = 2
limit = 10

print(f"multiplication table of {number}")
print("_"*30)

for i in range(1, limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
