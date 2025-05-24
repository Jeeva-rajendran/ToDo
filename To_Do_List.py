class ToDoList:
    def __init__(self):         
        self.DoList={}
        while True:
           
            serial=int(input("Enter the serial number:"))
            work=input("Enter the work of your To Do list:")
            self.DoList[serial]=work

            choice=input("You want to add more!(y/n):")
            choice=choice.lower()

            if choice=="y" or choice=="yes":
                continue
            elif choice=="n" or choice=="no":
                break
            else:
                print("invalid input")
    
   
    
    @staticmethod           #display the menu what are the things you can do with the to list.
    def display():
        print("1. View To Do List\n2. Mark Completed task\n3. Make changes with the list\n4.Extend list\n")
    
    def view_list(self):                #display to do list
        print(f"Here's your To Do List:{self.DoList}")

    
           
    def complete_task(self):            #remove completed task
        """Display stored To-Do List"""
        print(self.view_list())
        print("Note:If you completed the task,That task will be removed from your to do list\nFor mark complete")
        while True:
    
            change=int(input("Enter the serial number:"))
    
            if change in self.DoList:
                self.DoList.pop(change)
            else:
                print("Sorry!!Not found")
            
            choice=input("You want to mark more!(y/n):")
            choice=choice.lower()

            if choice=="y" or choice=="yes":
                continue
            elif choice=="n" or choice=="no":
                break
            else:
                print("invalid input")
        print("Marked Successfully")
    
    
            
    def update_list(self):              #update existing value
        print("For make changes in your to do list:")
        
        while True:
            change=int(input("Enter the serial number:"))
            update_value=input("Enter the value you want to update:")
            if change in self.DoList:
                self.DoList[change]=update_value
            else:
                print("Invalid serial number!!")
            
            choice=input("You want to update more!(y/n):")
            choice=choice.lower()

            if choice=="y" or choice=="yes":
                continue
            elif choice=="n" or choice=="no":
                break
            else:
                print("invalid input")
        print(f"Successfully updated")
    
    
    def extend_list(self):          #extend list
        print(f"Here's your To do list{self.view_list}")
        nums=int(input("Enter how many task you want to add:"))
        for i in range(nums):
            serial=int(input("Enter the serial number:"))
            value=input("Enter the task:")
            ToDoList[serial] = value 
        print("Successfully Added")      

if __name__=="__main__":

    def instruction():              #Display the instruction to create a todo list.
        
        print("For store your TODO list. \nFirst : Enter the serial number. \nSecond : Enter the work you want to add on the specific serial number.")
    
    instruction()
    
    obj=ToDoList()
    obj.display()

    while True:
        user_choice=input("Enter your choice (1/2/3/4):")
        if user_choice=="1":      #inside while loop
            obj.view_list()
        elif user_choice=="2":
            obj.complete_task()
        elif user_choice=="3":
            obj.update_list()
        elif user_choice=="4":
            obj.extend_list()
        else:
            print("Invalid input!!!")
        choice=input("You want to Excute more!(y/n):")
        choice=choice.lower()

        if choice=="y" or choice=="yes":
            continue
        elif choice=="n" or choice=="no":
            break
        else:
            print("invalid input")


