
n,p=map(int,input().split())
count=1
while True:
    if count==p:
        print(n)
        break
    if n==1:
        print(-1)
        break
    if(n%2):
        n=((3*n)+1)
        
    else:
        n=n//2
    count+=1
       

        
    
    
    
