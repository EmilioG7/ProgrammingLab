def sum_list(my_list):
    if len(my_list)==0:
        return None
    sum=0
    for element in my_list:
        sum=sum+element
    return sum

lista={1,2,3,4,5,6}
print("somma = {}" .format(sum_list(lista)))
