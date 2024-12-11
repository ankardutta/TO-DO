name=input("Enter Your Name")
print(f"Hello, {name} Welcome Back")

DoList=[]
ListCount= int(input("HOw many tasks you want to list here"))
for i in range (1, ListCount+1):
    task=input(f"Enter task-{i}")
    DoList.append(task)
print(f"Your today's task are \n {DoList}")

while True:
    Order=int(input("Enter which task You want to perform \n1-ADD \n2-UPDATE \n3-DELETE, \n4-SHOW \n5-EXIT"))
    if(Order==1):
        newtask=input("What new task you want to perform")
        DoList.append(newtask)
        print(f"New task {newtask} has been added")
        print(f"Your recent tasks are {DoList}")
    elif Order==2:
        Task_to_update= input("Enter your task, that you want to update")
        if Task_to_update in DoList:
            UpdatedTask= input("Write the new updated task that you want to perform")
            Index= DoList.index(Task_to_update)
            DoList[Index]=UpdatedTask
            print(f"Your recent tasks are {DoList}")
    elif Order==3:
        Task_to_Delete= input("which task you want to delete")
        if Task_to_Delete in DoList:
            Index=DoList.index(Task_to_Delete)
            del DoList[Index]
            print(f"Your recent tasks are {DoList}")
    elif Order==4:
        print(f"Your recent tasks are {DoList}")
    elif Order==5:
        print("You're Quiting")
        break
    else:
        print("You have entered Invalid Input")

# -- Subhankar Dutta