import sys
import os.path


def getTextFile():

    usrInput = input("Enter text file name: ")

    if not os.path.exists("emp.txt"):
        print("emp.txt not found!")
    else:
        try:
            with open(usrInput, 'r') as f:
                content = f.readlines()
                return content
        except FileExistsError():
            print("Error reading file!")


def printFile(content):
    for line in content:
        print(line.strip('\n'))


def createMenu(titleStr, optList):

    menu = titleStr + "\n"
    for i in range(len(optList)):
        menu += str(i+1) + ") " + optList[i] + "\n"
    return menu


def getValidChoice(menuStr, numOptions):
    while True:
        choice = input(menuStr)
        if choice.isdigit() and int(choice) in range(1, numOptions+1):
            return int(choice)
        else:
            print("Invalid choice!")


def printReport(empDict):
    print("\nEmployee Report")
    print("ID\tName")
    print("-"*10)
    for k,  v in empDict.items():
        print(k + "\t" + v)


def addEmployee(empDict):
    empID = input("Enter employee ID: ")
    empName = input("Enter employee name: ")
    empDict[empID] = empName


def delEmp(empDict):
    empID = input("Enter employee ID: ")
    if empID in empDict:
        del empDict[empID]
    else:
        print("Employee not found!")


def changeEmp(empDict):
    empID = input("Enter employee ID: ")
    empName = input("Enter employee name: ")
    empDict[empID] = empName


def main():
    empDict = {}
    content = getTextFile()
    for line in content:
        empDict[line.split(',')[0]] = line.split(',')[1]
    printReport(empDict)
    while True:
        choiceDict = {"Employee Menu": [
            "Add Employee", "Delete Employee", "Update Employee", "View Employee", "Exit"]}

        for k, v in choiceDict.items():
            menu = getValidChoice(createMenu(k, v), len(v))
            if menu == 1:
                addEmployee(empDict)
                printReport(empDict)
            elif menu == 2:
                delEmp(empDict)
                printReport(empDict)
            elif menu == 3:
                changeEmp(empDict)
                printReport(empDict)
            elif menu == 4:
                printReport(empDict)
            else:
                sys.exit()


if __name__ == "__main__":
    main()
