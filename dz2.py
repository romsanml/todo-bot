# Задача 1
# Модифицируйте программу, написанную на занятии так, чтобы выход из нее осуществлялся не только при вводе неизвестной команды, но и при вводе специальной команды exit. Сделайте так, чтобы при вводе этой команды программа выводила на экран текст: "Спасибо за использование! До свидания!"

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    task = input("Введите название задачи: ")
    tasks.append(task)
    print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    run = False
  else: 
    print("Неизвестная команда! До свидания!")
    run = False

# Задача 2
# Давайте усложним нашу программу. Сделайте следующие изменения:
# Заведите 3 списка: today, tomorrow, other (вы можете назвать переменные по-другому).
# Измените блок кода, который выполняет команду add:
# Дополнительно запросите у пользователя дату выполнения задачи.
# В зависимости от введенной даты добавьте задачу в один из списков по следующим правилам:
# Если пользователь ввел "Сегодня", добавьте задачу в список today.
# Если пользователь ввел "Завтра", добавьте задачу в список tomorrow.
# Если пользователь ввел любое другое значение, добавьте задачу в список other.

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

today, tomorrow, other = {}, {}, {}
tasks = [today, tomorrow, other]

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    date = input('Введите дату выполнения задачи: ')
    task = input("Введите название задачи: ")
    if date == 'Сегодня':
      if date in today:
        today[date].append(task)
      else:
        today[date] = []
        today[date].append(task)
    elif date == 'Завтра':
      if date in tomorrow:
        tomorrow[date].append(task)
      else:
        tomorrow[date] = []
        tomorrow[date].append(task)
    else:
      if date in other:
        other[date].append(task)
      else:
        other[date] = []
        other[date].append(task)
    print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    run = False
  else: 
    print("Неизвестная команда! До свидания!")
    run = False

