s = input().strip()
t = input().strip()
 
position = 1
 
for instruction in t:
    if s[position - 1] == instruction:
        position += 1  # Move to the next stone
 
print(position)
