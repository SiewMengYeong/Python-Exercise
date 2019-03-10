def star(n):
    return '*'*n

height = 5
for i in range(height):
    template = "{0:^" + str( 2 * height - 1 ) + "}"
    print( template.format( star( 2 * i + 1 ) ) )

def star(n):
    return '*'*n

def layer(width, n):
    left = (width - n) // 2
    right = width - left
    return ' '*left + star(n) + ' '*right

height = 4
for i in range(height):
    print( layer( 2 * height - 1 , 2 * i + 1 ) )

def modify(aList):
    aList[0] = 5
    aList = aList + [2]
    return aList

a = [3]
modify(a)
print(a) 

def modify(aList):
    aList = aList + [2]
    aList[0] = 5
    return aList

a = [3]
modify(a)
print(a)

def modify(aList):
    aList[0] = 5
    aList.append(2)
    return aList

a = [3]
modify(a)
print(a)

def modify(aList):
    aList[0] = 5
    aList.insert(0, 2)
    return aList

a = [3]
print( modify( a ) )

class Triangle:
    def __init__(self, h):
        self.height = h
    def __str__(self):
        s = ""
        for i in range(self.height):
            s = s + ( i + 1 ) * '*' + '\n'
        return s

def main():
    print( Triangle( 2 ) )
    print( Triangle( 5 ) )
    # Please clearly specify how many blank lines are there between
    # these two triangles
main()

class Rational:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
#    def __str__(self):
#        return str(n) + '/' + str(d)

def main():
    a = Rational(14, 8)
    print(a)

main()

def gcd(a, b):      # Greatest Common Divisor
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

class Rational:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
    def reduce(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // g
        self.denominator = self.denominator // g
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

def main():
    a = Rational(14, 8)
    print(a)

main()

msg = "DRO ZYBD XEWLOB SC DGOXDI DRYECKXN YXO REXNBON KXN PYBDI YXO"
key = 16
plaintext = ""

for ch in msg:
    if ch.isalpha():
        plaintext = plaintext + chr( (ord(ch) - 65 + key) % 26 + 65 )
    else:
        plaintext = plaintext + ch

print(plaintext)
