def sum(nums):
   a=0
   for i in nums.split():
      a=a+eval(i)
   return a

def main():
   sumlist=input("please write down the sum list=")
   print(sum(sumlist))

main()
