"""
Cílem je vytvořit jednoduchou kalkulačku, které funguje pomocí volání funkcí.

Např. zvoláním funkcí two(times(four())) dostaneme na výstupu číslo 8

"""


def calc(num, x):
        match x[0]:
            case "plus":
                return num+x[1]
            case "minus":
                return num-x[1]
            case "times":
                return num*x[1]
            case "devided_by":
                return num/x[1]

def zero(operand=False): return 0 if not operand else calc(0,operand)
def one(operand=False): return 1 if not operand else calc(1,operand)
def two(operand=False): return 2 if not operand else calc(2,operand)
def three(operand=False): return 3 if not operand else calc(3,operand)
def four(operand=False): return 4 if not operand else calc(4,operand)
def five(operand=False): return 5 if not operand else calc(5,operand)
def six(operand=False): return 6 if not operand else calc(6,operand)
def seven(operand=False): return 7 if not operand else calc(7,operand)
def eight(operand=False): return 8 if not operand else calc(8,operand)
def nine(operand=False): return 9 if not operand else calc(9,operand)

def plus(num): return "plus", num 
def minus(num): return "minus", num
def times(num): return "times", num
def divided_by(num): return "devided_by", num

print(four(times(two())))