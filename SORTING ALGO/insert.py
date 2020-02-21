def locate(num,arr,lo,hi,length):
	if(lo==hi and arr[lo]>=num):
		return lo
	elif(lo==hi):
		return length
	mid=lo+(hi-lo)//2
	if(arr[mid]>=num):
		hi=mid
	else:
		lo=mid+1
	return locate_rec(num,arr,lo,hi,length)
def linear_locate(num,arr,length):
	if(length==0):
		return 0
	return locate(num,arr,0,length-1,length)
def linear_iterate(num,arr,length):  
	for i in range(length):
		if(arr[i]>=num):
			return i
	return length-1
def linearsearch(num,arr,length):
	if(length==0):
		return -1
	pos=ll_iterate(num,arr,length)
	if(arr[pos]==num):
		return pos
	else:
		return -1
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
	return ordered_insert_helper(num,arr,lo,hi,new)
def ordered_insert(num,arr):
	new=[0 for i in range(0,len(arr)+1)]
	if(len(arr)==0):
		new[0]=num
	else:
		pos=ordered_insert_util(num,arr,0,len(arr)-1,new)
	return new	
def itr_insert(num,arr,length):
	pos=linear_locate(num,arr,length)
	print(pos)
	for i in range(length,pos,-1):
		arr[i]=arr[i-1]
	arr[pos]=num
	return arr
def insertion_sort(arr):
	if(len(arr)==0):
		return arr
	else:
		return ordered_insert(arr[0],insertion_sort(arr[1:len(arr)]))
def main():
	arr=[]
	arr=[int(i) for i in input().split()]
	length=len(arr)
	new=arr+[0]
	num=int(input("Enter number"))
	# if(length==0):
	# 	print(0)
	# 	exit()
	print("The position to insert ",num," is ",linear_locate(num,arr,length))
	print("The element is in ",linear_search(num,arr,length))
	arr=ordered_insert(num,arr)
	print("The new inserted array is ",arr)
	print("The iteratively inserted array is",itr_insert(num,new,length))
	s=[]
	print("Enter array for sorting")
	s=[int(i) for i in input().split()]
	print("The sorted array is ",insertion_sort(s))
if __name__=='__main__':
	main()
    