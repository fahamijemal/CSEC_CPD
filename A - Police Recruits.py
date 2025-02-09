n = int(input())
events = list(map(int, input().split()))
 
police = 0  
untreated = 0  
 
for event in events:
    if event == -1:  
        if police > 0:
            police -= 1  
        else:
            untreated += 1  
    else:
        police += event  
 
print(untreated)
