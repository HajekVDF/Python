"""
Je dána posloupnost celých čísel. Vytiskněte číslo
s největší absolutní hodnotou.

"""

cisla = [23,68,-84,5,-633,-9,-4,-1,54,-12,-4,-68]
max = 0

for x in cisla:
    if(x<0):
        x *= -1
    if(x>max):
        max = x

print(max)