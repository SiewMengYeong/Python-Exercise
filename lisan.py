def main():
  increment=0
  sum=0
  for i in range (1,11):
   for j in range (1,i+1):
    for k in range (1,j+1):
       increment=increment+1
       sum=sum+increment
       print(sum)
       
main()
