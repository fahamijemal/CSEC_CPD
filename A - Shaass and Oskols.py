n = int(input())
birds = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1

    left_birds = y - 1
    right_birds = birds[x] - y

    if x > 0:
        birds[x - 1] += left_birds
    if x < n - 1:
        birds[x + 1] += right_birds

    birds[x] = 0

print("\n".join(map(str, birds)))
