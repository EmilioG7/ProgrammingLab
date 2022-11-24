element='ktdy'
flag= True
for n in len.element:
    if element[n] in {'1','2','3','4','5','6','7','8','9','0','.'}: None
    else: flag= False# vedere se nella stringa ci sono lettere
if flag:
    print("{} è un numero".format(element))
else:
    print("{} non è un numero".format(element))