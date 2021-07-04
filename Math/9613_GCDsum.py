def euc_gcd(a,b): #Returns LCM of 'a' and 'b' by Euclidean Algorithm
    if a%b == 0 :
        return b
    return euc_gcd(b,a%b)

t = int(input())

while t:
    num = list(map(int,input().split(" ")))
    sum = 0
    
    for i in range(1, len(num)):
        for j in range(i+1, len(num)):
            sum += euc_gcd(num[i],num[j])
    
    print(sum)
    t -= 1