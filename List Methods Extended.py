#Michael Hein

#Functions
newlist = []
def addTask():
    task = input("What task do you want to add to your list?(please keep it in lowercase letters)")
    newlist.extend(task) 
    print("You have added " + task + " to your list")
    ans = input("Would you like to add another task to your list? yes(y) or no(n)")
    if ans == "y":
        addTask()
    else:
        program()
def removeTask():
    task = input("What task do you want to remove from your list?(please keep it in lowercase)")
    x = newlist.index(task)
    newlist.pop(x)
    print("You have removed " + task + " from your list")
    ans = input("Would you like to remove another task to your list? yes(y) or no(n)")
    if ans == "y":
        removeTask()
    else:
        program()
def viewList():
    print(newlist)
    ans = input("Would you like to view your list again? yes(y) or no(n)")
    if ans == "y":
        viewList()
    else:
        program()
#We Need fix the following function
def markTask():
    task = input("What task do you want to mark as finished on your list?")
    x = newlist.index(task)
    newlist.pop(x)
    y = task + " [X]"
    newlist.append(y)
    print("You have marked " + task + " as finish on your list")
    ans = input("Would you like to mark another task as finished on your list? yes(y) or no(n)")
    if ans == "y":
        removeTask()
    else:
        program()
def program():
    option = input("What would like to do?\nAdd a task (add)\nremove a taks (remove)\nView your to-do list(view)\nMark item as finished(mark)\nExit the program(exit)\nRemove all tasks(Gone)\nSort albhabetically(Alphabetasize)\nPrint number of Items on list(Count)")
    if option == "add":
        addTask()
    if option == "remove":
        removeTask()
    if option == "view":
        viewList()
    if option == "mark":
        markTask()
    if option == "exit":
        exit()
    if option == "Gone":
        ToDo.clear
        print("To-Do List Cleared")
    if option == "Alphabetasize":
        ToDo.sort()
        print("You're list is now sorted:" + str(ToDo))
    if option == "Count":
        print(len(ToDo)) 

#Main
program()