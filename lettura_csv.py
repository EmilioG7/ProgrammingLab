def sum_csv(file_name):
    my_file=open(file_name, 'r')
    somma=0
    for line in my_file:
        element=line.split(',')
        if element[0]!='date':
            somma+=element[1]
    return somma

a = sum_csv('shampoo_sales.txt')
print("somma = {}".format(a))

def sum_csv(file_name):
    my_file=open(file_name, 'r')
    somma=0
    for line in my_file:
        element=line.split(',')
        flag= True
        for n in element[1]
            if element[1][n] in {1,2,3,4,5,6,7,8,9,0,.}
            else flag= False# vedere se nella stringa ci sono lettere
    my_file.close()
    return somma