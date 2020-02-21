import sys
import math
import time
import random
def count(arr):
    c=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)): 
            if(arr[i]>arr[j]):
               c=c+1
    return c
#arr=[int(i) for i in input().split()]
arr=[]
n=int(input())
for i in range(n):
     arr.append(random.randint(1,9))
print(arr)
start=time.time()
print("The number of out-of-order pairs is",count(arr)) 
end=time.time()
print("Time",end-start)
