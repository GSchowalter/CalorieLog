#Prompts and generates a daily calorie log stored in an external file
import Entry
import datetime

FILE = 'CalorieLog.txt'
f = open(FILE, 'a')

def daily_entry():
    start_message = '\033[1;32;40mHope you had a good day!\nStay positive and tell me what you ate today\n'

    #Write the date
    date = datetime.datetime.now()
    f.write(date.strftime("%x\n"))

    total = 0

    print(start_message)

    while(True):

        #Prompt the user for meal and calories
        item = input("\033[1;35;40mEnter the meal or item: ")
        calories = input("Enter the amount of calories: ")

        #Add calories to total
        total += int(calories)

        #Make log
        entry = Entry.Meal(item, calories).entry
        f.write("\t" + entry)

        #Keep going?
        answer = input("All done today?(y/n): ")
        if answer.upper() == 'Y':
            break

    print('\n\033[1;36;40mTotal daily calories: {}'.format(total))
    print('See you tomorrow!')

daily_entry();