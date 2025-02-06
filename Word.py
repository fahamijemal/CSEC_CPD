s = input().strip()
 
uppercase_count = sum(1 for c in s if c.isupper())
lowercase_count = len(s) - uppercase_count 
 
if uppercase_count > lowercase_count:
    print(s.upper())
else:
