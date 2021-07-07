e,s,m = map(int,input().split())
y = 1

while True:
    if (y-e)%15==0 and (y-s)%28==0 and (y-m)%19==0: 
        #Instead of using x%y==r, use (x-r)%y==0 that is a lot faster while they conduct the same calculation.
        #Division operator, including modulo opeartor, should involve a number as small as possible since its time complexity isn't that efficient
        #https://stackoverflow.com/questions/27977834/why-is-modulus-operator-slow
        print(y)
        break
    y+=1