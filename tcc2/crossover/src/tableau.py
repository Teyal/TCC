import random


def tableau():
    f = open("sat.cnf","r")
    # p cnf {num_var} {num_cla}
    _, _, v, c = f.readlines()[1].split()

    vars = []*v

    temp = ""
    for l in range(3,len(f.readlines()))
        temp += f.readlines()[l]:.replace(' 0', '')
        vars[]
    f.close
    k = open("sat.kb", "w")
    k.write(kb)
    k.close()
    print(kb)


def gen_sat(num_var, num_cla):
    sat = f'''3-SAT autogerated in DIMACS-CNF format
p cnf {num_var} {num_cla}'''

    for c in range(num_cla):
        sat += '\n'
        for i in range(3):
            v = random.randint(1,num_var)
            sign = random.randint(0,1)
            if sign:
                v = -v
            sat += f'''{v} '''
        sat += '0'
    f = open("sat.cnf", "w")
    f.write(sat)
    print('done')

gen_sat(12,10)
tableau()