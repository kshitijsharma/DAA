def ordered_insert_util(num,arr,lo,hi,new): 
	if(lo==hi and arr[lo]>=num):
		new[lo+1]=arr[lo]
		new[lo]=num
		return lo
	elif(lo==hi):
		new[lo]=arr[lo]
		new[lo+1]=num
		return len(arr)
	mid=lo+(hi-lo)//2
	if(arr[mid]>=num):
		new[mid+2:hi+2]=arr[mid+1:hi+1]
		#print(new)
		hi=mid
	else:
		new[lo:mid+1]=arr[lo:mid+1]
		lo=mid+1
	return ordered_insert_util(num,arr,lo,hi,new)
def ordered_insert(num,arr):
	new=[0 for i in range(0,len(arr)+1)]
	if(len(arr)==0):
		new[0]=num
	else:
		pos=ordered_insert_util(num,arr,0,len(arr)-1,new)
	return new	
def ordered_merge(u,v):
	if(len(u)==0):
		return arr
	else:
		return ordered_merge(sub[1:len(u)],ordered_insert(u[0],v))
u=[]
v=[]
print("Enter the array")
u=[int(i) for i in input().split()]
print("The sorted array is",ordered_merge(u,v))
