x = int(input())
y = int(input())

if x > y:
    print("Second integer can't be less than the first.")
else:
    for num in range(x, y + 1, 5):
        print(num, end=' ')
    print()




   
