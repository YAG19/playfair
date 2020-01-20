import numpy as np
a=[]
l1=[]
str="keyword"     
l1=list(str)

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

for s in range(97,123):
    if s == 106 :
      continue
    a.append(chr(s))
    
l1.extend(a)
l2=Remove(l1)

n = 5
m = 5
val = [0] * n
for x in range (n):
    val[x] = [0] * m
k=0
for x in range(n):
  for j in range(m):
      val[x][j]=l2[k]
      k+=1

a="Hi Hello how are you"
print("\nPlain Text:",a,"\n\n")
a=a.lower()
def remove(string): 
    return "".join(string.split()) 
a=remove(a) 
l1=list(a)

def RemoveSame(duplicate): 
    final_list = [] 
    for i in range(0, len(duplicate) - 1):
        final_list += duplicate[i]
        if duplicate[i] == duplicate[i+1]:
            final_list += 'x'
    return final_list

l3=RemoveSame(l1)
z=(len(l3))

if (z%2 != 0 ):
  l3.append("x")

matrix=(np.asarray(val))
print(matrix)
k=0
def addre(word,k):
  for x in range(n):
    for j in range(m):
      if (matrix[x][j]==word):
        return((x,j))
y=[]
for word in l3:
    y.append(addre(word,k))
m2=np.asarray(y)

z1=[]
z2=[]

for i in y:
  for j in i:
    z1.append(int(j))

def encrypted(y1,y2,y3,y4):
  if y2==y4:
    if y1>=4:
        y1=0
    elif(y3>=4):
        y3=0
    else:
      y1=y1+1
      y3=y3+1
  else:
    if y1==y3:
      if y2>=4:
        y2=0
      elif(y4>=4):
        y4=0
      else:
        y2=y2+1
        y4=y4+1
    
    else:
      temp=y2
      y2=y4
      y4=temp
  return(y1,y2,y3,y4)

op=0 
z3=[] 
for i in z1:
  z2.append(i)
  op+=1
  if op%4==0:
    z3.append(encrypted(z2[op-4],z2[op-3],z2[op-2],z2[op-1]))

z4=[]
for i in z3:
  for j in i:
    z4.append(j)
cipher_text=[]
def alls(x,y):
    cipher_text.append(matrix[x][y]) 
rip=0
for i in range(len(z4)):
  if rip%2==0:
    alls(z4[rip],z4[rip+1])
  rip=rip+1  

str1 = ''.join(cipher_text)
str2 = ''.join(l3)

print("\nEncryted message :",str1)
print("\nDecoded message  :",str2)
