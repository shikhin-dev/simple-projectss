# To-Do-List
# Author: Unknown
# Description: A Simple To-Do-List

import time

def run():
    stop=True
    tasks=[]
    while(stop==True):
        time.sleep(1)
        print("=== TO-DO-LIST ===\n" \
        "1. View Task\n2. Add Task\n" \
        "3. Remove Task\n4. Exit")

        option=int(input("Choose an option:"))


        if option==2:
            newtask=str(input("Enter a new task:"))
            time.sleep(0.5)
            print("Task Added!")
            tasks.append(newtask)
        elif option==1 and len(tasks)!=0:
            for i,j in enumerate(tasks,start=1):
                print(i,'.',j)
        elif option==1 and len(tasks)==0:
            print("No tasks are available!")
        elif option==3 and len(tasks)!=0:
            rmvtask=int(input("Enter the task number to remove:"))
            print("Removed:",tasks[rmvtask-1])
            del tasks[rmvtask-1]
        elif option==3 and len(tasks)==0:
            print("No tasks are available!")
        elif option==4:
            print("Good Bye!")
            stop=False

if(__name__=="__main__"):
    run()