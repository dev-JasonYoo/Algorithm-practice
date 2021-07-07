import sys

# height = list(map(int,sys.stdin.readline().split()))
#or
height = [0]*9
for i in range(9):
    height[i] = int(sys.stdin.readline())

height = sorted(height)

for_break = False
for i in range(len(height)):
    for j in range(len(height)):
        if (sum(height) - (height[i]+height[j])) == 100:
            one = height[i]
            two = height[j]
            height.remove(one)
            height.remove(two)
            for_break = True
            break
    if for_break:
        break

for i in range(len(height)):
    print(height[i])