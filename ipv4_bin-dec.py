"""
Funkce pro převod čísel mezi dvojkovou a desítkovou soustavou + funkce pro převod
IPv4 adres mezi dvojkovou a desítkovou soustavou.

"""


def bin_to_dec(binary):
    binary = list(str(binary))
    binary.reverse()
    count = 0
    for n in range(len(binary)):
        count += int(binary[n])*(2**n)
    return count


def dec_to_bin(decimal):
    binary = ""
    decimal = int(decimal)
    while decimal > 0:
        if decimal % 2 == 0:
            binary += "0"
        else:
            binary += "1"
        decimal //= 2
    return binary[::-1]


def ipv4_dec(address):
    address = address.split(".")
    for n in range(len(address)):
        while len(address[n]) < 8:
            address[n] = "0" + address[n]
        address[n] = str(bin_to_dec(address[n]))
    return ".".join(address)


def ipv4_bin(address):
    address = address.split(".")
    for n in range(len(address)):
        address[n] = str(dec_to_bin(address[n]))
        while len(address[n]) < 8:
            address[n] = "0" + address[n]
    return ".".join(address)


