class ContinueC(Exception):
    pass
cnf = '''
c example DIMACS-CNF 3-SAT
p cnf 3 3
1 2 0
-2 -3 0
-2 3 0'''
expr = cnf.split('\n')
print(expr[3:])
variables = expr[2].split()[-2]
for i in range(7):
    ans = i
    anb = [int(x) for x in list('{0:0{width}b}'.format(ans, width=variables))]
    anb.reverse()
    #print(anb)

    valid = True
    for c in expr[3:]:
        try:    
            for v in c.split()[:-1]:
                if '-' in v:
                    sign = 0
                else:
                    sign = 1
                pos = abs(int(v)) - 1
                if not(sign ^ anb[pos]):
                    #print(sign,anb[pos], pos)
                    #print('e')
                    raise ContinueC
            valid = False
            break
        except ContinueC:
            continue
    if valid:
        print(ans," is valid")
    else:
        print(ans," is invalid")
