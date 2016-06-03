"""Phantasy Star Online (1) ID calculator
https://github.com/audricd/PSOidCalc
Tested on Windows 10 with Python 3.5.1
"""
import os

fullcharname = input(str("Type in desired character name:"))  # grabs character name
# charnamelen = len(fullcharname) TODO while for len exceeds character limiter

charnums = (fullcharname.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                                 'abcdefghijklmnopqrstuvwxyz'
                                                 '1234567890'
                                                 '`~!@#$%^&*()-_=+\|[{]};:\'\",<.>/? ',
                                                 '56789012345678901234567890'
                                                 '78901234567890123456789012'
                                                 '9012345678'
                                                 '963456748201551325133498644062732')))  # translation for char id

separado = [int(i) for i in str(charnums)]  # separates each character
suma = sum(separado)  # sums each character value
sumastr = str(suma)  # converts sum to string
lastdig = (sumastr[-1])  # grabs the last digit of the sum

# translate last digit to game id
if lastdig == "0":
    print(fullcharname + " will generate a Viridia ID"),
elif lastdig == "1":
    print(fullcharname + " will generate a Greenill ID"),
elif lastdig == "2":
    print(fullcharname + " will generate a Skyly ID"),
elif lastdig == "3":
    print(fullcharname + " will generate a Bluefull ID"),
elif lastdig == "4":
    print(fullcharname + " will generate a Purplenum ID"),
elif lastdig == "5":
    print(fullcharname + " will generate a Pinkal ID"),
elif lastdig == "6":
    print(fullcharname + " will generate a Redria ID"),
elif lastdig == "7":
    print(fullcharname + " will generate a Oran ID"),
elif lastdig == "8":
    print(fullcharname + " will generate a Yellowboze ID"),
elif lastdig == "9":
    print(fullcharname + " will generate a Whitill ID")
else:
    print("error")

os.system("pause")  # prevents the window from closing
