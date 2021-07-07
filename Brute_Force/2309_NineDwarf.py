import sys

# height = list(map(int,sys.stdin.readline().split()))
#or
height = [0]*9
for i in range(9):
    height[i] = int(sys.stdin.readline())

height = sorted(height)

def solution():
    sum_height = sum(height)
    for i in range(len(height)):
        for j in range(len(height)):

            if (sum_height - (height[i]+height[j])) == 100:
                for k in range(len(height)):
                    if k != i and k != j: # Don't need to edit the list. Instead, just print it out without invalid values.
                        print(height[k])
                return

solution()