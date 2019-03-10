def main():
   a=eval(input("write down you unicode number:"))
   for i in a.split():
      message=""
      message=message+chr(i)
      print(message,end="")
   print()

main()
