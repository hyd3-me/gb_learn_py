from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

#print(1/2 + 1/3)

#print(frac1.split('/'))

def get_d(_str):
    a, b = _str.split('/')
    return int(a), int(b)

def find_d(a, b):
    return b, a

def sum_ab(args):
    d1, div1 = get_d(args[0])
    d2, div2 = get_d(args[1])
    if div1 != div2:
        d1 *= div2
        d2 *= div1
        div1 *= div2
        div2 *= div1
    print(f'{d1 + d2}/{div1}')
    return d1, d2, div1, div2



def mult_ab(args):
    d1, div1 = get_d(args[0])
    d2, div2 = get_d(args[1])
    print(f'{d1 * d2}/{div1 * div2}')
    return d1, d2, div1, div2

sum_ab((frac1, frac2))
mult_ab((frac1, frac2))

print(Fraction(frac1) + Fraction(frac2))
print(Fraction(frac1) * Fraction(frac2))