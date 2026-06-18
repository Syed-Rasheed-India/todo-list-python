

task=[]

def add_task():
    new_dict = {}
    task_name=input("Enter your task : ")
    # status = input("Enter your status : ")
    new_dict["task"]=task_name
    new_dict["status"]="not completed"
    task.append(new_dict)
    print("Task is added")
def remove_task():
    task_name = input("Enter the removing task : ")
    for I in task:
        for (taskName,status) in I.items():
            if taskName==task_name:
                task.remove(i)
    print("Task is removed")

    print("Remaining tasks are:")
    print(task)

def marking_task():
    task_name = input("Enter the marking task : ")
    status = input("Are You Completed Your Task : ")
    for I in task:
        for (taskName,s) in I.items():
            if taskName==task_name:
                I['status']=status

    print("Marking task is completed")
def view_task():
    for I in task:
        for (taskName, s) in I.items():
            print(taskName,s)
while True:
    print("Todo-List")
    print("Let's Make Dream Comes True")

    task_list=["Add task","Remove task","Marking Task","View All Task"]

    j=1
    for i in task_list:
        print(j,i)
        j=j+1

    choices = int(input("Enter your choice:"))

    if choices==1:
        add_task()
    elif choices==2:
        remove_task()
    elif choices==3:
        marking_task()
    elif choices==4:
        view_task()
    else:
        print("Invalid Choice")
        exit()
