ch=input()
cha=[]
for i in ch:
  if i.isnumeric():
    cha.append(i)
print("".join(cha))
