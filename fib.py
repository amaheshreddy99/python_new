nth=10
n1=0
n2=1
count=0
if nth<=0:
           print('give postive number')
elif nth==1:
           print('1')
else:
           while count<nth:
                      print(n1,nth)
                      nth=n1+n2
                      n1=n2
                      nth=n2
                      count+=1
                      print()
                      
                 
