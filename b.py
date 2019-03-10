def f(p):
	 if p: return 'T'
	 else: return 'F'
	 
def main():
    str = "{0:<10}\t{1:<10}\t{2:<15}\t{3:<15}"
    print(str.format("P", "Q", "not (P or Q)", "not P and not Q") )
    print(str.format("===", "===", "===", "===") )
    for P in [True, False]:
        for Q in [True, False]:          
            print(str.format( f(P), f(Q), not(P or Q),not P and not Q ) )
            

main()
