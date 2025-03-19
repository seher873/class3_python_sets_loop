#serching with else
numbers=[2,6,6,8,10]
target=5
for num in numbers:
    if num == target:
        print(f"{target} is found")
        break
    else:
        print(f"{target }is not found")