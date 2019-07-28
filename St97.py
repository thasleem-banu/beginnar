ch,cha=map(int,input().split())
p=1
waht=0
while(p<=ch and p<=cha):
  if(ch%p==0 and cha%p==0):
    waht=p
  p+=1
print(waht)
