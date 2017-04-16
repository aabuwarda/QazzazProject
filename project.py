import os
import sys
import fileinput
def MangerOrWaiter():
    print("Welcome to ABC Restaurant\n1- Manger\n2 -Waiter\n3- EXIT\n")
    MOW_input = int(input("Select your Role (1-3): "))
    if MOW_input < 0 or MOW_input > 3:
        print("Error input")
    elif MOW_input==1:
        MangerOptions()
    elif MOW_input==2:
        Waiter()
    elif MOW_input==3:
        exit()
    else:
        print("Error input")

def MangerOptions():
    print("========================\nManger Options\n========================\n1- Manage Waiters\n2- Manage Food Menu\n3- Veiw Orders\n4- BACK\n")
    MO_input = int(input("Select Option (1-4): "))
    if MO_input < 0 or MO_input > 4:
        print("Error input")
    elif MO_input==1:
        ManageWaiter()
    elif MO_input==2:
        ManageFood()
    elif MO_input==3:
        print("order")
        print("====================\n"
              "Waiter : " + "AhmedQazzaz\n"
              "Food : " + "(2)" + "Kabab" + "-" + "2"
              "\n(1)" + "CocaCola" + "(20)\n"
              "Price : " + "370")
    elif MO_input==4:
        MangerOrWaiter()
    else:
        print("Error input")
#---------------------------------------------Start Manage Waiter-----------------------------------------------------#
def ManageWaiter():
    print("========================\nManage Waiter\n========================\n1- Add New Waiter\n2- Edit Existing Waiter\n3- Delete Waiter\n4- BACK\n")
    MW_input = int(input("Enter your choice: "))
    if MW_input < 0 or MW_input > 4:
        print("Error input")
    elif MW_input==1:
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

    elif MW_input==2:
        print("###Edit Existing Waiter###")
        def EditNewWaiter():
            fwaiters = open('waiters.txt', 'a')
            print("Enter the Waiter you want to Edit: ")
            WaiterToSearch = input("> ")

            print("Enter the New Waiter: ")
            WaiterToReplace = input("> ")
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
        EditNewWaiter()

    elif MW_input==3:
        print("###Delete Waiter###")
        def delWaiters():
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
    elif MW_input==4:
        MangerOptions()
    else:
        print("Error input")
#---------------------------------------------End Manage Waiter-----------------------------------------------------#

#---------------------------------------------Start Manage Food-----------------------------------------------------#
def ManageFood():
    print("========================\nManage Food\n========================\n1- Manage Menus\n2- Manage Food\n3- BACK\n")
    MF_input = int(input("Enter your choice: "))
    if MF_input < 0 or MF_input > 3:
        print("Error input")
    elif MF_input == 1:
        ManageMenus()
    elif MF_input == 2:
        ManageFoodMenu()
    elif MF_input == 3:
        MangerOptions()
    else:
        print("Error input")
#---------------------------------------------End Manage Food-----------------------------------------------------#

#---------------------------------------------Start Manage Menus-----------------------------------------------------#
def ManageMenus():
    print("========================\nManage Menus\n========================\n1- Add New Menus\n2- Edit Existing Menus\n3- Delete Menus\n4- BACK\n")
    MM_input = int(input("Enter your choice: "))
    if MM_input < 0 or MM_input > 4:
        print("Error input")
        ManageMenus()
    elif MM_input == 1:
        print("add New Menus")
    elif MM_input == 2:
        print("Delete Menus")
    elif MM_input == 3:
        print("Delete Menus")
    elif MM_input ==4:
        ManageFood()
    else:
        print("Error input")
        ManageMenus()
#---------------------------------------------End Manage Menus-----------------------------------------------------#

#---------------------------------------------Start Manage Food Menus-----------------------------------------------------#
def ManageFoodMenu():
    print("1- Add New Food\n2- Edit Existing Food\n3- Delete Food\n4- BACK\n")
    MFM_input = int(input("Enter your choice: "))
    if MFM_input < 0 or MFM_input > 4:
        print("Error input")
    elif MFM_input == 1:
        print("Add New Food")

    elif MFM_input == 2:
        print("edit Existing Food")
    elif MFM_input == 3:
        print("Delete Food")
    elif MFM_input == 4:
        ManageFood()
    else:
        print("Error input")
#---------------------------------------------End Manage Food Menus-----------------------------------------------------#
def Waiter():
    print("Soon -- Waiter")
    waiter_username=input("Enter username: ")
    if waiter_username in open('waiters.txt').read():
        print("Waiter Options "+"(",waiter_username,")")
    else:
        print("Username doesn't exist")
        Waiter()

MangerOrWaiter()









