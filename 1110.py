def main():
    aList = [1, 2, 3]
    print(aList)
    append(aList, 4)
    print(aList)

def append(s, n):
    s = s + [n]
    print("This updated list is", s)

main() 
