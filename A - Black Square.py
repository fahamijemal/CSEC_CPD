a = list(map(int, input().split()))
s = input()
 
 
calories = sum(a[int(ch) - 1] for ch in s)
 
print(calories)
