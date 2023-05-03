"""
Sára sbírá loutky a chce si je vyvěsit do skříně - musí tedy nakoupit věšáčky. Každý věšák unese maximálně dvě loutky, ale má taky maximální nosnost.
Zjistěte, kolik si Sára musí koupit věšáčků, aby na ně mohla rozvěsit loutky.

Na vstupu bude číslo N - počet loutek a číslo K - maximální nosnost věšáků. Každé další číslo na vstupu bude udávat váhu loutky.
Na výstupu bude jedno číslo - nejmenší počet věšáků, které bude Sára potřebovat.

Ukázkový vstup:
4
20
20
8
15
10

Ukázkový výstup:
3
"""
pocet_loutek = int(input("Zadej počet loutek: "))
max_nosnost = int(input("Zadej nosnost věšáku: "))
seznam_loutek = []

while pocet_loutek > 0:
    user_input = int(input("Zadej váhu loutky: "))
    seznam_loutek.append(user_input)
    pocet_loutek-=1


def pocet_vesaku(loutky, nosnost):
    x = sum(loutky)
    x //= nosnost
    if (x%nosnost) != 0:
        x += 1
    return x

print(pocet_vesaku(seznam_loutek, max_nosnost))