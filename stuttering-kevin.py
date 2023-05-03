"""
„P-p-p-pomoc!“ vrazil Kevin ráno do třídy. „Proč jdeš pozdě?“ 
ptala se přísně učitelka. Od začátku hodiny uplynulo už deset minut. 
„P-p-před-de d-d-dveřmi…“ snažil se odpovědět Kevin, ale bylo na něm
vidět, že je celý rozčílený.

Aby byla učitelka schopná pochopit, co se Kevinovi stalo, musí si 
poradit s jeho dočasnou koktavostí. Chtěla by z jeho vět odstranit všechna
přebytečná písmena, která Kevin vykoktává víckrát po sobě. Pomůžete jí?

Na vstupu váš program obdrží záznam Kevinovy řeči. Na výstupu chceme pro
každý řádek tu samou řeč, ale stejné znaky vedle sebe budou vypsány jenom jednou. 
Platí to i pro mezery, naopak s ch si lámat hlavu nemusíte (skládá se ze dvou znaků).

ukázkový vstup:
Ppppommmoccc
vvvvyyysssstrasssil
  mmmne    vvvelky
pppavvouk

ukázkový výstup:
Ppomoc
vystrasil
 mne velky
pavouk
"""

def odkoktat(text):
    clean_text = ""
    for x in range(len(text)):
        if x == 0:
            clean_text += text[x]
            continue
        else:
            if text[x] != text[x-1]:
                clean_text += text[x]
    return clean_text

print(odkoktat("ppppoooomooc vvvvyyysssstrasssil     mmmmeeee   veeeelkyyy ppppaavvvvouuk"))