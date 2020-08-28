#Prompts and generates a daily calorie log stored in an external file
import Entry

FILE = 'CalorieLog.txt'
f = open(FILE, 'a')

l = Entry.Meal('bagel', 500)
entry = l.entry

f.write(entry)

