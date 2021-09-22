class Verifier():
    def __init__(self, expression):
        expr = expression.split('\n')
        self.expr = expr
        self.var_size = expr[2].split()[-2]

    def verify(self, answer):
        anb = [int(x) for x in list('{0:0{width}b}'.format(answer, width=self.var_size))]
        anb.reverse()
        valid = True
        for c in self.expr[3:]:
            for v in c.split()[:-1]:
                if '-' in v:
                    sign = 1
                else:
                    sign = 0
                pos = abs(int(v)) - 1
                if (sign ^ anb[pos]):
                    break        
            else:
                valid = False   
        return valid
expression = '''
    c example DIMACS-CNF 3-SAT
p cnf 3 3
-1 -2 3 0
1 -2 -3 0
1 2 -3 0'''
veri = Verifier(expression)
r = []
for i in range(8):
    if veri.verify(i):
        r.append(i)

print(r)