import csv

finish = False

def getCategoriesList() -> list:
    with open('categories.csv', 'r') as categoriesFile:
        catList = categoriesFile.readlines()
        return [cat.strip() for cat in catList]


def categoryValid(catToValidate: str) -> bool:
    if catToValidate in getCategoriesList():
        return True
    else:
        return False


def getTasksAsArray() -> []:
    with open('tasks.csv', 'r') as tasksFile:
        tasksList = tasksFile.readlines()
        tasksListStripped = [task.strip() for task in tasksList]
        return tasksListStripped


def displayTasks(tasksList=getTasksAsArray()):
    for task in tasksList:
        print(task)


def displaySortingMenu():
    print('Sort by:')
    print('1. Task - ASC')
    print('2. Task - DESC')
    print('3. Date - ASC')
    print('4. Date - DESC')
    print('5. Person - ASC')
    print('6. Person - DESC')
    print('7. Category - ASC')
    print('8. Category - DESC')
    print('9. Back')
    print('10. Exit')
    selectedOption = input('Your sorting option: ')
    unsortedTasksList = getTasksAsArray()
    while selectedOption != 10:
        match selectedOption:
            case '1':
                displayTasks(sorted(unsortedTasksList, key=lambda x: x[0]))
                displayActionMenu()
                break
            case '2':
                displayTasks(sorted(unsortedTasksList, key=lambda x: x[0], reverse=True))
                displayActionMenu()
                break
            case '3':
                displayTasks(sorted(unsortedTasksList, key=lambda x: x[1]))
                displayActionMenu()
                break
            case '4':
                displayTasks(sorted(unsortedTasksList, key=lambda x: x[1], reverse=True))
                displayActionMenu()
                break
            case '5':
                displayTasks(sorted(unsortedTasksList, key=lambda x: x[2]))
                displayActionMenu()
                break
            case '6':
                displayTasks(sorted(unsortedTasksList, key=lambda x: x[2], reverse=True))
                displayActionMenu()
                break
            case '7':
                displayTasks(sorted(unsortedTasksList, key=lambda x: x[3]))
                displayActionMenu()
                break
            case '8':
                displayTasks(sorted(unsortedTasksList, key=lambda x: x[3], reverse=True))
                displayActionMenu()
                break
            case '9':
                displayActionMenu()
                break
            case _:
                print('Invalid option. Please try again.')



def displayActionMenu():
    print('Action Menu:')
    print('1. Display tasks')
    print('2. Sort tasks')
    print('3. Add new task')
    print('4. Edit task')
    print('5. Delete task')
    print('6. Exit')

    user_input = input('What would you like to do: ')
    while user_input != 6:
        match user_input:
            case '1':
                displayTasks()
                displayActionMenu()
                break
            case '2':
                displaySortingMenu()
                break
            # case '3':
            #     addTask()
            #     break
            # case '4':
            #     editTask()
            #     break
            # case '5':
            #     deleteTask()
            #     break
            # case '6':
            #     break
            case _:
                print('Invalid option. Please try again.')


def getTasksData():
    with open('categories.csv', 'a', newline='') as categories_csv:
        csv_writer = csv.writer(categories_csv, delimiter=',')
        categories = input('Add categories, comma separated:')
        for category in categories.split(','):
            csv_writer.writerow([category])

    with open('tasks.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        row = []
        while True:
            user_input = input('Add task: ')
            if user_input == 'q':
                break
            row.append(user_input)
            user_input = input('Add to-do date: ')
            if user_input == 'q':
                break
            row.append(user_input)
            user_input = input('Add person: ')
            if user_input == 'q':
                break
            row.append(user_input)
            user_input = input('Add category: ')
            if user_input == 'q':
                break
            while not categoryValid(user_input):
                user_input = input('Category not in the the Categories list. Please add another category: ')
                if user_input == 'q':
                    break
            row.append(user_input)
            csv_writer.writerow(row)
            row.clear()
            if user_input == 'q':
                break
getTasksData()
displayActionMenu()
