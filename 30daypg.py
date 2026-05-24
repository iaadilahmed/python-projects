print("welcome to the habit tracker")
name = input("Your name : ")
print("hello",name)
habits = []
while True:
    print("1. Add habit")
    print("2. Exit")
    print("3. show habits")
    print("4. mark as completed")
    user_choice = input("choose : ").lower()
    if user_choice == "add habit" or user_choice == "1":
        habit = input("Habit name : ")
        habits.append(habit)
        habit_dict = {}
        habit_dict["name"]=[habit]
        print(habit_dict)
        print("Habit : ",habit)
        habits.append(habit_dict)
    elif user_choice == "show habits" or user_choice == "3":
            if len(habits) == 0:
                print("no habit added yet")
            else:
                counter = 1
                for habit in habits:
                    print(counter,habit["name"])
                    if(habit_dict["completed"]== True):
                         print("completed")
                    else:
                         print("not completed")
                    counter += 1
    elif user_choice == "mark as completed" or user_choice == "4":
        if len(habits)== 0:
             print("no habit added")
        if len(habits)>= 1:
             counter = 1
        for habit in habits:
                    print(counter,habit["name"])
                    markhabit = print(int(input("choose habit ex - 1,2 and 3")))
                    if markhabit == 1:
                         print #---------------------------------------------------------------------
                    if(habit_dict["completed"]== True):
                         print("completed")
                    else:
                         print("not completed")
                    counter += 1
                        
    elif user_choice == "exit" or user_choice == "2":
        print("Goodbye")
        break
    else:
        print("invalid choice")

