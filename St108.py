ch=int(input())
cho=list(map(int,input().split()))
for p in range(len(cho)-1):
     if(cho[p]>cho[p+1]):
           print(p)
           break
