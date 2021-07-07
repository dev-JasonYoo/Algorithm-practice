esm = list(map(int,input().split()))
count = [1,1,1]
y = 1

while True:
    if count==esm:
        print(y)
        break
    
    y+=1
    for i in range(3):
        count[i]+=1
    
    if count[0]==16:
        count[0] = 1
        
    if count[1]==29:
        count[1] = 1
        
    if count[2]==20:
        count[2] = 1
    