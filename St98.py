  
ch,cha=map(int,input().split())
sho,sha=ch,cha
while(cha):
  ch,cha=cha,ch%cha
sasu=(sho*sha)//ch
print(sasu)
