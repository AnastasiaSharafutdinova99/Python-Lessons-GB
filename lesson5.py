import json

# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#    Об окончании ввода данных будет свидетельствовать пустая строка.

user_file = open('user_file.txt', 'w+')
while True:
    input_str = (input('Введите данные: '))
    if not input_str:
        break
    else:
        user_file.write(input_str + '\n')
    user_file.seek(0)
    user_info = user_file.read()

print(user_info)
user_file.close()


# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
#    выполнить подсчёт строк и слов в каждой строке.

file = open('test_file.txt', 'r')
test_file = file.readlines()
i = 0
print(f'Количество строк в файле: {len(test_file)}')
for line in test_file:
    words = test_file[i].split()
    i += 1
    print(f'Слов в строке {i}: {len(words)}')
file.close()


# 3. Создать текстовый файл (не программно).
#    Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
#    Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
#    Выполнить подсчёт средней величины дохода сотрудников.

employee_file = open('empoyee_salary.txt', 'r', encoding='utf-8')
salary_list = []
employee_list = []
employee_salary = employee_file.read()
employee_salary_list = employee_salary.split()
i = 0
j = 0
c = 0
k = 0
while i <= len(employee_salary_list) - 1:
    if i % 2 != 0:
        salary_list.append(float(employee_salary_list[i]))
    i  += 1
while j <= len(employee_salary_list) - 1:
    if j % 2 == 0:
        employee_list.append(employee_salary_list[j])
    j  += 1
print('Оклад меньше 20 тысяч у следующих сотрудников:')
while c <= len(salary_list) - 1:
    if salary_list[c] < 20000:
        print(employee_list[c])
    c += 1
average_income = 0
for k in range(len(salary_list)):
    average_income += salary_list[k]
average_income_all = average_income / len(salary_list)
print(f'Средний доход сотрудников: {average_income_all:.3f}')
employee_file.close()


# 4. Создать (не программно) текстовый файл со следующим содержимым:
#    One — 1
#    Two — 2
#    Three — 3
#    Four — 4
#    Напишите программу, открывающую файл на чтение и считывающую построчно данные.
#    При этом английские числительные должны заменяться на русские.
#    Новый блок строк должен записываться в новый текстовый файл.

num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
num_file = open('numbers_file.txt', 'r', encoding='utf-8')
while True:
    numbers_file = num_file.readline()
    new_num = numbers_file.split()
    if not numbers_file:
        break
    else:
        for i in range(len(new_num)):
            if i == 0:
                new_num[0] = num_dict.get(new_num[0])
        new_numbers = new_num[0] + ' ' + new_num[1] + ' ' + new_num[2] + '\n'
        print(new_numbers, end='')
        ru_numbers = open('ru_numbers_file.txt', 'a', encoding='utf-8')
        for j in range(len(new_numbers)):
            ru_numbers.write(new_numbers[j])
        ru_numbers.close()
num_file.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#    Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

summ_file = open('input_numbers.txt', 'a', encoding='utf-8')
numbers = list(map(int, input('Введите числа: ').split()))
summ = 0
for i in range(len(numbers)):
    summ += numbers[i]
    summ_file.write(f'{numbers[i]}')
    if i != len(numbers) - 1:
        summ_file.write(' + ')
summ_file.write(f' = {str(summ)} \n')
print(f'Сумма введённых чисел = {summ}')
summ_file.close()


# 6. Сформировать (не программно) текстовый файл.
#    В нём каждая строка должна описывать учебный предмет и наличие лекционных,
#    практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
#    Необязательно, чтобы для каждого предмета были все типы занятий.
#    Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#    Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#    Физика: 30(л) — 10(лаб)
#    Физкультура: — 30(пр) —
#    Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

f_lessons = open('lessons_file.txt', 'r', encoding='utf-8')
lessons = f_lessons.readlines()
lessons_dict = {}
for i in range(len(lessons)):
    lessons_split = lessons[i].split()
    del_str = '—'
    for el in lessons_split:
        if del_str in lessons_split:
            lessons_split.remove(del_str)
    count_lesson_list = []
    for j in range(1, len(lessons_split)):
        count_lesson = lessons_split[j].split('(')
        count_lesson_list.append(int(count_lesson[0]))
    el_summ = 0
    for element in count_lesson_list:
        el_summ += element
    lessons_dict[lessons_split[0]] = el_summ
print(lessons_dict)
f_lessons.close()


# 7. Создать вручную и заполнить несколькими строками текстовый файл,
#    в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
#    Пример строки файла: firm_1 ООО 10000 5000.
#
#    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#    Если фирма получила убытки, в расчёт средней прибыли её не включать.
#    Далее реализовать список.
#    Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#    Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
#    Итоговый список сохранить в виде json-объекта в соответствующий файл.
#    Пример json-объекта:
#    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#    Подсказка: использовать менеджер контекста.

company_file = open('company_data.txt', 'r', encoding='utf-8')
lines_count = 0
average_profit = 0
profit_company_count = 0
companies_dict = {}
while True:
    company_info = company_file.readline()
    lines_count += 1
    if not company_info:
        break
    company_info_list = company_info.split()
    company_profit = int(company_info_list[2]) - int(company_info_list[3])
    print(f'Прибыль компании {company_info_list[0]} составила {company_profit}')
    if company_profit > 0:
        average_profit += company_profit
        profit_company_count += 1
    companies_dict[company_info_list[0]] = company_profit
companies_average_profit = average_profit / profit_company_count
companies_average_profit = float('{:.3f}'.format(companies_average_profit))
print(f'Средняя прибыль составила {companies_average_profit}')
average_profit_dict = {'average profit' : companies_average_profit}
companies_profit_list = [companies_dict, average_profit_dict]
print(companies_profit_list)
company_file.close()

with open('company_data.json', 'w', encoding='utf-8') as json_company_file:
    json.dump(companies_profit_list, json_company_file)