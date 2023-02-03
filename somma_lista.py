
my_list=[1,2,3]

def sum_list(lista):
    if len(lista)==0:
        return None
    sum = 0
    for item in lista:
        sum=sum+item
    return sum

print("somma = {}".format(sum_list(my_list)))