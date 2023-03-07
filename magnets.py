"""
Zadání: Kevin má N magnétů, které mají na jednom konci + pól a na druhém - pól.
    Jeden po druhém magnety vyndaval a pokládal je do řady na stůl.
    Kevina tedy zajímalo, kolikrát se magnety mezi sebou spojí.

Vstup: Na vstupu bude jedno celé číslo N, které značí počet magnetů a na každém
    dalším řádku bude buď řetězec "+-" nebo "-+" udávající směr magnetu.

Výstup: Na výstupu bude číslo, kolikrát se magnety spojí.

Ukázkový vstup:
    4
    +-
    +-
    -+
    +-

Ukázkový výstup:
    2

"""

def magnets(magnets_arr):
    count = 0
    for x in range(len(magnets_arr)):
        if x == 0:
            continue
        else:
            if magnets_arr[x][0] != magnets_arr[x-1][0]:
                count += 1
    return count


magnets_line = []
magnets_num = int(input())

while magnets_num > 0:
    magnets_line.append(input())
    magnets_num -= 1

print(magnets(magnets_line))