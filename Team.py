n = int(input())
 
solvable_count = 0
for _ in range(n):
    a, b, c = map(int, input().split())  # Read three integers
    if a + b + c >= 2:  # Check if at least two friends are sure
        solvable_count += 1
 
print(solvable_count)
