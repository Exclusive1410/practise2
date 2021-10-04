Credit_card = [0,1,2,3];
Credit_card[0] = 4,1,3,4;
Credit_card[1] = 7,8,3,2;
Credit_card[2] = 9,0,2,5;
Credit_card[3] = 4,5,1,9;
print(Credit_card[3]);

n = input("Введите трехзначное число: ")
n = int(n)

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10
n = n // 10

print("Сумма цифр числа:", d1 + d2 + d3)