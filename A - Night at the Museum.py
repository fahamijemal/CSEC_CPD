s = input() 
 
current = 'a'
rotations = 0
 
for char in s:
  
    clockwise = abs(ord(char) - ord(current))
    counterclockwise = 26 - clockwise  
    rotations += min(clockwise, counterclockwise)
 
    
    current = char

print(rotations)
