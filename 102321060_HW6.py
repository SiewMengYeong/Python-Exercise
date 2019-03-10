def grade(y):
    print('The grade is', y+'.')
def main():
    x=eval(input('Input a score -- '))
    if x>=90:
        grade('A')
    elif x>=80:
        grade('B')
    elif x>=70:
        grade('C')
    elif x>=60:
        grade('D')
    else:
        grade('F')

main()
