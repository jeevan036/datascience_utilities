#check if reversible

a=int(input("enter a 3 digit number"))
t=0
while(a>0):
    r= a%10
    t=t+r
    a=a/10

if(t==r):
    print("reversible")

else:
    print("irreversible")