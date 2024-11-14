fev_food = []


while True:
    print("\nThis is a program that manage my favorite food\n")
    print("0: Exit")
    print("1: Add food")
    print("2: Remove food")
    print("3: View all foods")
    

    option = int(input("\nSellect an option to perform something: "))
    if 0<=option<=3:

        if option == 0 :
            print("\nThank you for using the program ")
            break

        elif option == 1 :
            food = input("\nEnter your food name: ")
            fev_food.append(food)

        elif option == 2 :

            print("\n1: Remove 1 item from the list")
            print("2: Remove all item from the list\n")
            
            option = int(input("Sellect an option to perform something: "))

            if option == 1 :
                
                food = input("\nEnter the name of the food that you want to remove: ")
                if food in fev_food:
                    fev_food.remove(food)

                else:
                    print("\nYour food item is not in the list \n")  

            elif option == 2 :
                print("\nAre you sure that you want to clear the list?")
                print("1: Yes")
                print("2: No")

                option = int(input("\nSellect an option to perform something: "))

                if option == 1:

                    if fev_food == []:
                        print("\nYou already have an empty list of favorite foods")

                    else:
                        fev_food.clear()
                        print(fev_food)
                        print("Your list is cleared successfully ")

                else:
                    print("\nYour list is not removed yet\n ")

        elif option == 3 :
            
            if fev_food:
                print("\nYour favorite food list is : ")

                for index , food in enumerate (fev_food , start=1):
                    print(f"{index} : {food}\n")

            else:
                print("\nYour favorite food list is empty\n")
        
        else:
            print("Nothing\n")
    
    else:
        print("Invalid input! Please try again. ")

