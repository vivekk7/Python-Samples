import datetime
name = raw_input("Enter your name: ")
age = raw_input("\nEnter your age:")
current_year = datetime.datetime.now()
new_year = (100 - int(age)) + int(current_year.year)
print "%s, you will turn 100 in the year %d" % (name,new_year)