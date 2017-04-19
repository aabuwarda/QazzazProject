import fileinput
#----start code
#--------------------------------------start Manage Or Waiter options
def MangerOrWaiter():
    print("Welcome to ABC Restaurant\n1- Manger\n2 -Waiter\n3- EXIT\n")
    MOW_input = input("Select your Role (1-3): ")
    if MOW_input=="1":
        MangerOptions()
    elif MOW_input=="2":
        Waiter()
    elif MOW_input=="3":
        sureExit=input("press ENTER to exit ,Enter n to back.")
        if sureExit=="n":
            MangerOrWaiter()
        else:
            exit()
    else:
        print("Error input ,Enter 1 or 2 or 3")
        MangerOrWaiter()
#--------------------------------------End Manage Or Waiter options

#---------------------------------------------Start Manger Options
def MangerOptions():
    print("========================\nManger Options\n========================\n1- Manage Waiters\n2- Manage Food Menu\n3- Veiw Orders\n4- BACK\n")
    MO_input = input("Select Option (1-4): ")
    if MO_input=="1":
        ManageWaiter()
    elif MO_input=="2":
        ManageFood()
    elif MO_input=="3":
        print("order")
        print("====================\n"
              "Waiter : " + "AhmedQazzaz\n"
              "Food : " + "(2)" + "Kabab" + "-" + "2"
              "\n(1)" + "CocaCola" + "(20)\n"
              "Price : " + "370")
    elif MO_input=="4":
        MangerOrWaiter()
    else:
        print("Error input")
        MangerOptions()
#---------------------------------------------End Manger Options

#---------------------------------------------Start Manage Waiter-----------------------------------------------------#
def ManageWaiter():
    print("========================\nManage Waiter\n========================\n1- Add New Waiter\n2- Edit Existing Waiter\n3- Delete Waiter\n4- BACK\n")
    MW_input = input("Enter your choice: ")
    if MW_input=="1":
#-----------------------Start Add New waiter
        print("## New Waiter ##")
        def AddNewWaiter():
         line=input("Enter New Waiter name: ")
         waiters = set()
         if line not in waiters:
             fwaiters = open('waiters.txt', 'a')
             fwaiters.write(line + '\n')
             waiters.add(line)
             fwaiters.close()
             print(line,"successfully added !")
             print("1-add more")
             print("2-BACK")
             AddWaiterOption = input(":")
             if AddWaiterOption == "1":
                 AddNewWaiter()
             elif AddWaiterOption == "2":
                 ManageWaiter()
        AddNewWaiter()
# -----------------------End Add New waiter
    elif MW_input=="2":
# -----------------------Start Edit Existing waiter
        print("###Edit Existing Waiter###")
        def EditNewWaiter():
            printWaiters()
            fwaiters = open('waiters.txt', 'a')
            WaiterToSearch = input("Enter the Waiter you want to Edit: ")
            WaiterToReplace = input("Enter the New Waiter: ")
            path = 'waiters.txt'
            tempFile = open(path, 'r+')
            for line in fileinput.input(path):
                if WaiterToSearch in line:
                    print(WaiterToSearch, ' successfully replaced to', WaiterToReplace)
                tempFile.write(line.replace(WaiterToSearch, WaiterToReplace))
            tempFile.close()
            print("1-Edit more")
            print("2-BACK")
            EditWaiterOption = input(":")
            if EditWaiterOption == "1":
                EditNewWaiter()
            elif EditWaiterOption == "2":
                ManageWaiter()
            else:
                ManageWaiter()
        EditNewWaiter()
# -----------------------End Edit Existing waiter
    elif MW_input=="3":
# -----------------------start delete waiter
        print("###Delete Waiter###")
        def delWaiters():
            printWaiters()
            delWaiter = input("Enter Waiter name to delete:")
            if delWaiter != "" and " ":
             with open('waiters.txt', 'r') as infile:
                 newlist = [i for i in infile.read().split() if i != delWaiter]
             with open('waiters.txt', 'w') as outfile:
                 outfile.write("\n".join(newlist))
             print(delWaiter, "successfully deleted!")
             infile.close()
             outfile.close()
             print("1-delete more")
             print("2-BACK")
             delWaitersOption = input(":")
             if delWaitersOption == "1":
                 delWaiters()
             elif delWaitersOption == "2":
                 ManageWaiter()
            else:
                print("Error input")
                delWaiters()

        delWaiters()
# -----------------------End delete waiter
    elif MW_input=="4":
        MangerOptions()
    else:
        print("Error input")
        ManageWaiter()
#---------------------------------------------End Manage Waiter-----------------------------------------------------#

#---------------------------------------------Start Manage Food-----------------------------------------------------#
def ManageFood():
    print("========================\nManage Food\n========================\n1- Manage Menus\n2- Manage Food\n3- BACK\n")
    MF_input = input("Enter your choice: ")
    if MF_input == "1":
        ManageMenus()
    elif MF_input == "2":
        ManageFoodMenu()
    elif MF_input == "3":
        MangerOptions()
    else:
        print("Error input")
        ManageFood()
#---------------------------------------------End Manage Food-----------------------------------------------------#

#---------------------------------------------Start Manage Menus-----------------------------------------------------#
def ManageMenus():
    print("========================\nManage Menus\n========================\n1- Add New Menus\n2- Edit Existing Menus\n3- Delete Menus\n4- BACK\n")
    MM_input = input("Enter your choice: ")
    if MM_input == "1":
        print("add New Menus")
        def AddNewMenus():
         typech = 97
         while (typech < 123):
           line=input("Enter New Menus name: ")
           Menus = set()
           if line not in Menus:
             fMenus = open('menus.txt', 'a')
             fMenus.write(line + '\n')
             print(typech)
             Menus.add(line)
             fMenus.close()
             print(line,"successfully added !")
             typech = typech + 1
             print(typech)
             print("1-add more")
             print("2-BACK")
             AddWaiterOption = input(":")
             if AddWaiterOption == "1":
                 AddNewMenus()
             elif AddWaiterOption == "2":
                 ManageFood()
        AddNewMenus()
    elif MM_input == "2":
        print("Edit Existing Menus")
        def EditNewMenus():
            printMenu()
            fMenus = open('menus.txt', 'a')
            print("Enter the Waiter you want to Edit: ")
            MenusToSearch = input("> ")
            print("Enter the New Waiter: ")
            MenusToReplace = input("> ")
            path = 'menus.txt'
            tempFile = open(path, 'r+')
            for line in fileinput.input(path):
                if MenusToSearch in line:
                    print(MenusToSearch, ' successfully replaced to', MenusToReplace)
                else:
                    print("Error, try again!")
                    EditNewMenus()
                tempFile.write(line.replace(MenusToSearch, MenusToReplace))

            tempFile.close()
            print("1-Edit more")
            print("2-BACK")
            EditMenusOption = input(":")
            if EditMenusOption == "1":
                EditNewMenus()
            elif EditMenusOption == "2":
                ManageFood()
            else:
                print("Error input, Try again")
                ManageMenus()
        EditNewMenus()

    elif MM_input == "3":
        print("Delete Menus")
        def delMenus():
            printMenu()
            delMenus = input("Enter Menus name to delete:")
            if delMenus != "" and " ":
                with open('menus.txt', 'r') as infile:
                    newlist = [i for i in infile.read().split() if i != delMenus]
                with open('menus.txt', 'w') as outfile:
                    outfile.write("\n".join(newlist))
                print(delMenus, "successfully deleted!")
                infile.close()
                outfile.close()
                print("1-delete more")
                print("2-BACK")
                delMenusOption = input(":")
                if delMenusOption == "1":
                    delMenus()
                elif delMenusOption == "2":
                    ManageMenus()
                else:
                    print("Error input, Try again")
                    ManageMenus()
            else:
                print("Error input")
                delMenus()
        delMenus()

    elif MM_input =="4":
        ManageFood()
    else:
        print("Error input")
        ManageMenus()
#---------------------------------------------End Manage Menus-----------------------------------------------------#

#---------------------------------------------Start Manage Food Menus-----------------------------------------------------#
def ManageFoodMenu():
    print("1- Add New Food\n2- Edit Existing Food\n3- Delete Food\n4- BACK\n")
    MFM_input = input("Enter your choice: ")
    if MFM_input == "1":
        print("## Add New Food ##")
        def AddNewFood():
            print("Menu :")
            with open("menus.txt") as menufile:
                for menus in menufile:
                    (key, val) = menus.split()
                    menudect[str(key)] = val
                    print(str(key) + "." + menudect[str(key)])
            Foodname = input("Enter Food name: ")
            foodprice= input("Enter Food Price: ")
            Food = set()
            if Foodname not in Food:
                fFood = open('food.txt', 'a')
                fFood.write(Foodname +" "+foodprice+ '\n')
                Food.add(Foodname +" "+foodprice+ '\n')
                fFood.close()
                print(Foodname, "successfully added !")
                print("1-add more")
                print("2-BACK")
                AddFoodOption = input(":")
                if AddFoodOption == "1":
                    AddNewFood()
                elif AddFoodOption == "2":
                    ManageFood()
                else:
                    print("Error input, try again")
                    ManageFood()

        AddNewFood()

    elif MFM_input == "2":
        print("edit Existing Food")
        def EditNewFood():
            printFood()
            fFood = open('food.txt', 'a')
            FoodToSearch = input("Enter the Food you want to Edit: ")
            FoodToReplace = input("Enter the New Food: ")
            path = 'food.txt'
            tempFile = open(path, 'r+')
            for line in fileinput.input(path):
                if FoodToSearch in line:
                    print(FoodToSearch, ' successfully replaced to', FoodToReplace)
                tempFile.write(line.replace(FoodToSearch, FoodToReplace))
            tempFile.close()
            print("1-Edit more")
            print("2-BACK")
            EditFoodOption = input(":")
            if EditFoodOption == "1":
                EditNewFood()
            elif EditFoodOption == "2":
                ManageFood()
        EditNewFood()
    elif MFM_input == "3":
        print("Delete Food")
        def delFood():
            printFood()
            delFood = input("Enter Menus name to delete:")
            if delFood != "" and " ":
                with open('food.txt', 'r') as infile:
                    newlist = [i for i in infile.read().split() if i != delFood()]
                with open('food.txt', 'w') as outfile:
                    outfile.write("\n".join(newlist))
                print(delFood, "successfully deleted!")
                infile.close()
                outfile.close()
                print("1-delete more")
                print("2-BACK")
                delFoodOption = input(":")
                if delFoodOption == "1":
                    delFood()
                elif delFoodOption == "2":
                    ManageFood()
            else:
                print("Error input")
                delFood()
        delFood()
    elif MFM_input == "4":
        ManageFood()
    else:
        print("Error input")

#---------------------------------------------End Manage Food Menus-----------------------------------------------------#
#---------------------------------------------Start Waiter--------------------------------------------------------------#
def Waiter():
    waiter_username=input("Enter username: ")
    if waiter_username in open('waiters.txt').read():
        print("Waiter Options "+"(",waiter_username,")")
    else:
        print("Username doesn't exist\ntry again!")
        Waiter()
# ---------------------------------------------End Waiter--------------------------------------------------------------#

#----------------------read a File and convert to list and dect
#---------------------------
def printMenu():
 menudect = {}
 with open("menus.txt") as menufile:
     for menus in menufile:
        (mkey, mval) = menus.split()
        menudect[str(mkey)] = mval
        print(str(mkey) + "." + menudect[str(mkey)])
def printFood():
 fooddect = {}
 with open("food.txt") as menufile:
     for menus in menufile:
        (fkey, fval) = menus.split()
        fooddect[str(fkey)] = fval
        print(fkey + " : " + fooddect[str(fkey)])
def printWaiters():
 waiterlist = []
 with open("waiters.txt") as waiterfile:
     for waiterf in waiterfile:
        (waiternames) = waiterf.split()
        waiterlist += waiternames
     for waiterlists in waiterlist:
         print(waiterlists)

#-----------------------------------------------------------------
MangerOrWaiter()







