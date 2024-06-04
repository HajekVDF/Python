"""
Funkce, která zjistí, zda slovo převedené do morseova kódu je 
palindrom (kód je stejný při čtení zleva doprava a zprava doleva).
"""

def is_morse_palindrome(word):
    morse = {
        "A":".-",
        "B":"-...",
        "C":"-.-.",
        "D":"-..",
        "E":".",
        "F":"..-.",
        "G":"--.",
        "H":"....",
        "I":"..",
        "J":".---",
        "K":"-.-",
        "L":".-..",
        "M":"--",
        "N":"-.",
        "O":"---",
        "P":".--.",
        "Q":"--.-",
        "R":".-.",
        "S":"...",
        "T":"-",
        "U":"..-",
        "V":"...-",
        "W":".--",
        "X":"-..-",
        "Y":"-.--",
        "Z":"--..",
        "1":".----",
        "2":"..---",
        "3":"...--",
        "4":"....-",
        "5":".....",
        "6":"-....",
        "7":"--...",
        "8":"---..",
        "9":"----.",
        "0":"-----"
    }

    converted = ""
    for letter in word:
        converted += morse[letter]
    if converted == converted[::-1]:
        return True
    else:
        return False


inputs_list = ["5", "9K73K1", "9FL1", "Q05PP50Y", "YVV4Q7TVR", "TW1YQ9GT"]

for word in inputs_list:
    print(is_morse_palindrome(word))

