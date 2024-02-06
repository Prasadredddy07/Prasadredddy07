'''
num=int(input("Enter the number:"))
count=10
while count>=0:
    prod=num*count
    print(num,"*",count,"=",prod)
    count=count-1
'''
lst=[15,22,35,44,55,66,76,80]
index=0
while index<=7:
    if lst[index]%2==0:
     print(lst[index],"is even")
    else:
        print(lst[index],"is odd")
    index=index+1
    
