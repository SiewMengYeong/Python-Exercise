def sum():
   sumlist=input("please write down the sum list=")
   a=0
   for i in sumlist.split():
      a=a+eval(i)
   print(a)

sum()
