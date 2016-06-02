"""Phantasy Star Online (1) ID calculator"""


fullcharname = input(str("Character name:"))
charnamelen = len(fullcharname)

charnums = (fullcharname.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
                                           '`~!@#$%^&*()-_=+\|[{]};:\'\",<.>/? ',
                                           '567890123456789012345678907890123456789012345678'

                                           '90129012345678963456748201551325133498644062732')))

separado = [int(i) for i in str(charnums)]
suma = sum(separado)
sumastr = str(suma)
lastdig = (sumastr[-1])

if lastdig == "0":
    print (fullcharname +" will generate a Virdia ID"),
elif lastdig == "1":
    print (fullcharname +" will generate a Greenile ID"),
elif lastdig == "2":
    print (fullcharname +" will generate a Skyly ID"),
elif lastdig == "3":
    print (fullcharname +" will generate a Bluefull ID"),
elif lastdig == "4":
    print (fullcharname +" will generate a Purplenum ID"),
elif lastdig == "5":
    print (fullcharname +" will generate a Pinkal ID"),
elif lastdig == "6":
    print (fullcharname +" will generate a Redria ID"),
elif lastdig == "7":
    print(fullcharname +" will generate a Oran ID"),
elif lastdig == "8":
    print(fullcharname +" will generate a Yellowboze ID"),
elif lastdig == "9":
    print(fullcharname +" will generate a Whitill ID")
else:
    print("error")
