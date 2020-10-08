from random import randint
#
word = str(input('Digite a frase/palavra transfóbica: '))
nw = word.replace('da', 'de').replace('do', 'de').replace('a', 'e')
nw = nw.replace('o', 'e').replace('ca', 'que').replace('co', 'que')
if("ce" in nw):
    nw = nw.replace("ce", "que")
elif("le" in nw):
    r = randint(0, 1)
    if r > 0:
        nw = nw.replace("le", "lu")
    else:
        nw = nw.replace("le", "lo")
nw = nw.replace("ge", "gui")
#
print(f"\n\n\nA frase certa é: {nw}")


"""Esse programa não tem o intúito de ferir ou denegrir qualquer causa
   Foi feito apenas como brincadeira usufruindo da minha própria liberdade

   Programa opensource, qualquer alteração é bem vinda!

   Agradeço a atenção: Dannyboy
"""
