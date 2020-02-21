import sys
import time
import math
import random
def mergesort_util(arr,lo,hi):
	total=0
	if(lo<hi):
		mid=lo+(hi-lo)//2
		total+=mergesort_util(arr,lo,mid)
		total+=mergesort_util(arr,mid+1,hi)
		total+=merge(arr,lo,mid,hi)
	return total
def merge(arr,lo,mid,hi):
	left=[]
	right=[]
	li=0
	ri=0
	total=0
	#print(lo,mid,hi)
	for i in range(lo,mid+1):
		#print(li,i)
		left.append(arr[i])
		li+=1
	for i in range(mid+1,hi+1):
		right.append(arr[i])
		ri+=1
	#print(left,right)
	n1=len(left)
	n2=len(right)
	i=j=0
	k=lo
	while(i<n1 and j<n2):
		if(left[i]<=right[j]):
			arr[k]=left[i]
			i+=1
			k+=1
		else:
			arr[k]=right[j]
			j+=1
			k+=1
			total+=mid-i+1
	while(i<n1):
		arr[k]=left[i]
		i+=1
		k+=1
	while(j<n2):
		arr[k]=right[j]
		j+=1
		k+=1
	return total
def mergesort(arr):
	return mergesort_util(arr,0,len(arr)-1)
arr=[int(i) for i in input().split()]
# n=int(input())
# arr=[]
# for i in range(n):
# 	arr.append(random.randint(1,9))
print(arr)
start=time.time()
print("The number of inversions are",mergesort(arr))
end=time.time()
print("The sorted array is",arr)
print("The time taken is ",end-start)

