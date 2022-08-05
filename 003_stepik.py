A = list()
first_num = int(input())
A.append(first_num)
second_num = int(input())
A.append(second_num)
third_num = int(input())
A.append(third_num)
fourth_num = int(input())
A.append((fourth_num))

minimal = first_num
for item in A:
    if item < minimal:
        minimal = item
print(minimal)

# до
# 13
# включительно – детство;
# от
# 14
# до
# 24 – молодость;
# от
# 25
# до
# 59 – зрелость;
# от
# 60 – старость.
age = int(input("Введите свой возраст: "))
if age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 50:
    print('зрелость')
else:
    print('старость')

first_num = int(input())

second_num = int(input())

third_num = int(input())

sum = 0

if (first_num > -1):

   sum += first_num

if (second_num > -1):

   sum +=second_num

if (third_num > -1):

   sum += third_num

print(sum)


num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')
