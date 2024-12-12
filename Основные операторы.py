def access(x):
    password = ''
    for i in range(1,x):
        for j in range(2,x):
            if j <= i:
                continue
            if x %(i+j) == 0:
                password += str (i) + str(j)
    return password
n = int(input('Введите целое число от 3 до 20:'))
result = access(n)
print ('Пароль:',result)