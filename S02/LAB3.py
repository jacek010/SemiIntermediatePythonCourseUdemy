def display_options(list_of_options: list):
    print("MENU")
    for i in range(len(list_of_options)):
        print(f'[{i + 1}] - {list_of_options[i]}')

    select = input("Please select options one of above or enter to exit:")

    return select


choice = 'x'
choice_options = ['load data', 'export data', 'analyze&predict']
while True:
    choice = display_options(choice_options)
    if not choice:
        print("Exit")
        break

    try:
        choice_num = int(choice) - 1
        if 0 <= choice_num < len(choice_options):
            print(f'You have selected {choice_options[choice_num]}')
        else:
            print("Choose a valid option")
    except:
        print("Please enter number")
