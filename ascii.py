s=input("enter a string:")
s1=""
for i in s:
           if i.isalpha():
                      s1=s1+str(ord(i))
print(s1)
