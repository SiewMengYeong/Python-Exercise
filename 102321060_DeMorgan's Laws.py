def main():
    print('{0:<10}'.format('P'),
          '{0:<10}'.format('Q'),
          '{0:<10}'.format('not(P or Q)'),
          '{0:<10}'.format('not P and not Q'),sep='\t')
    for i in range(4):
        print('{0:<10}'.format('==='),end='\t')
    print()
    for P in [True, False]:
        for Q in [True, False]:
            x=P, Q, not(P or Q),not P and not Q
            for i in x:
                if i==True:
                    print('{0:<10}'.format('T'),end='\t')
                else:
                    print('{0:<10}'.format('F'),end='\t')
            print()
    print()

main()
