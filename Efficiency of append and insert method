import time
from datetime import datetime
def odd_no_generator(n,m):
  """
  to calculate the timetaken for creating odd numbers within a specific range using append and insert.Finding the time taken and understanding the logic
  """
  d=n
  c=m
  t1=datetime.now() #using the epoch time to know the present time
  a=[]     #empty list for append method

  while n < m:
    a.append(n)
    n=n+2
  t2=datetime.now()
  print('The time taken:',t2-t1)
  #print(a)
  print(n,m)

  b=[]  #empty list for insert method
  i=0
  t3=datetime.now()
  while d < c:
    #print(i)
    b.insert(i,d)
    d=d+2
    i=i+1
  t4=datetime.now()
  print('The time taken:',t4-t3)
  print("{0},{1}".format(d,c))
  #print(b)

odd_no_generator(1,100000000)

#We conclude that append method being more efficient in larger computation


