
def find_password(number):
    result = []
    for i in range(1, number):
        for j in range(i+1, number):
            if number % (i + j) == 0:
                result.append((i, j))
    password = ''.join(f"{i}{j}" for i, j in result)
    return (password)

number = int(input('Введите число из первой вставки '), )
password = find_password (number)
print(password)
