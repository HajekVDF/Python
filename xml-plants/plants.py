import xml.etree.ElementTree as ET #import knihovny pro práci s XML soubory

#Načtení XML souboru
tree = ET.parse('C:/path/plants.xml') #Absolutní cesta ke XML souboru
root = tree.getroot()

#Najde všechny rostliny s cenou pod 3 dollary a vypíše běžný název, latinský název a cenu rostliny
for element in root.findall("PLANT"):
    price = float(element.find("PRICE").text[1:])
    if price <= 3:
        print(element.find("COMMON").text, element.find("BOTANICAL").text, element.find("PRICE").text)