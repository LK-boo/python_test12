def print_params(a=1, b= "строка", c= True ):
    print (a,b,c)
print_params (b=25)
print_params (c=[1,2,3])
values_list = ["Лева", 564, [9,8,4]]
values_dict = {"a": "Лева","b": 564, "c": [9,8,4]}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)