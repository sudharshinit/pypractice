s = "   00432"
l =[]
for i in s :
    if i!= "0" and i!=" ":
       l.append(i)
print(''.join(l))



s = "121"
f = []
g = []
for n in range(1):
  for i in s :
      f.append(i)
      g.insert(0,i)
      a=''.join(f)
      b=''.join(g)
      print(a)
      print(b)
      if a==b:
          print("true")
      else:
        print("false")


  h = input("enter a string : ").lower()
  o = input("enter a string : ").lower()
  l=[]
  j=[]
  for x in h :
    l.append(x)
    m=''.join(l)
  print(m)  
  for d in o :
    j.append(d)
    b=''.join(j)
  print(b)
  if m==b:
        print("true")
  elif d == "*": 
        d = j[o.index("t")-1]
  elif d == ".":
        print("true")
  else:
        print("false")



&9U,CDXu_Bgr:jh