import time
import random
import math

def max_sub_seq(x):
      n = len(x)
      
      maxsum=0
      for i in range(n):
          thissum=0
          for j in range(i,n):
              thissum+=x[j];
              if thissum > maxsum:
                    maxsum=thissum
      return maxsum    



for j in range(10):
    n=int(input("enter the size of the array: "))
    average=0
    total=0
    for k in range (10):
         x=[]
         for i in range(n):
             x.append(random.randint(-100,100))
         start_time=time.time()
         maxsum = max_sub_seq(x)
         end_time=time.time()
         total=total+end_time-start_time
         
         print('the array is: \n', x)
         print('the maximum sum is: ' ,maxsum)
         print('Execution time is : ' ,end_time-start_time)
    average=total/10
    print(' \n\n average time is: ', average)
    print(' \n\n log(n) ratio: ', average/math.log(n))
    print(' \n\n n :', average/n)
    print(' \n\n n square :', average/(n*n))
    print(' \n\n n cube :', average/(n*n*n))
    print(' \n\n 2 power n :', average/(2**n))
