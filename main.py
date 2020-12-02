numbers = input("Введите числа : ")
sum_1 = sum(map(int, numbers.split(' ')))
print("Сумма введенных чисел = ", sum_1)
numberss = input("Введите числа : ")
def summ_numbers(numberss, sum_1):
    summ = sum(map(int, numberss.split(' ')))
    summ_all = summ + sum_1
    print("Сумма всех введнных чисел равна = ", summ_all)

summ_numbers(numberss, sum_1)

#Comment
#hello





