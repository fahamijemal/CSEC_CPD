n, h = map(int, input().split())
a = list(map(int, input().split()))
width = sum(2 if height > h else 1 for height in a)
print(width)