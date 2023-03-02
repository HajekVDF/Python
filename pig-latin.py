"""
Funkce pro překlad vět do základní prasečí latiny + dokumentace.
"""


def pig_word(word):                         # Funkce, která překládá slovo na vstupu do prasečí latiny
    split_word = list(word)                 # Uložení word do pole split_word
    split_word.append(split_word[0])        # Vložení (zkopírování) první hodnoty z pole na konec pole
    split_word.pop(0)                       # Smazání první hodnoty z pole
    return "".join(split_word)+"ay"         # Výstup + převod pole na string a přičtení "ay" ke stringu

def pig_word_two(word):                     # Funkce má stejný výstup jako funkce pig_word - má pouze jiný postup
    return word[1:] + word[0] + "ay"        # Výstup + převod slova pomocí indexace řetězců

def pig_latin(sentence):
    split_sentence = sentence.split()       # Rozdělení věty na slova, která se uloží do pole split_sentence
    for n in range(len(split_sentence)):    # Cyklus pro převod jednotlivých slov pomocí již vytvořené funkce pig_word
        split_sentence[n] = pig_word(split_sentence[n])
    return " ".join(split_sentence)         # Výstup + převod pole na string
