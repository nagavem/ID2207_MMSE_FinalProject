"""
IDENTIFY ROLE
THIS IS ROLE SPECIFIC MENU THAT WILL BE DISPLAYED AFTER LOGIN
"""

import eventReq
import tasks
import extraBudget
import extraStaff


def custServiceMenu():
    print("What would you like to do?")
    print("1. Create a Customer Event Request and send to Senior Customer Service Officer \n2. Exit")
    choice = int(input("Enter choice : "))
    print(choice)
    if choice == 1:
        print("Please enter event details below")
        custName = input("Customer Name : ")
        ID = input("Event Request ID : ")
        eventStartDate = input("Event Start Date  : ")
        eventEndDate = input("Event End Date : ")
        eventDescription = input("Event Details : ")
        budget = input("Budget in SEK : ")
        eventReq.createEventRequest(custName, eventStartDate, eventEndDate, eventDescription, budget, ID)
        eventReq.printEventReq()
        print("Event Successfully Created!")
    else:
        print("Thank You!")


def seniorCustManagerMenu():
    print("What would you like to do?")
    print("1. Review Event Request \n2. Exit")
    choice = int(input("Enter choice : "))
    print(choice)
    if choice == 1:
        print("Below is the customer event request :")
        eventReq.printEventReq()
        print("\nHow would you like to proceed with the event request review?")
        status = eventReq.getEventRequestStatus()
        if status!="APPROVED":
            nextchoice = int(input("1. Approve and forward to Finance Manager for feedback \n2. Disapprove \n3.Exit \n"))
            if nextchoice == 1:
                eventReq.UpdateEventRequest("SCSApproval", "YES")
            elif nextchoice == 2:
                eventReq.UpdateEventRequest("SCSApproval", "NO")
                eventReq.UpdateEventRequest("status", "REJECTED")
                print("EVENT REJECTED! ")
                # eventReq.eventRequest.clear()
            else:
                print("Thank You!")
        else:
            print("The event request is approved!")
            print("Please setup a meeting with the client and other stakeholders for detailed planning...")
    else:
        print("Thank You!")


def financeManagerMenu():
    print("What would you like to do?")
    print("1. Review a Event Request \n2.Review Extra Budget Requests\n3. Exit")
    choice = int(input("Enter choice : "))
    if choice == 1:
        print("Below is the customer event request :")
        eventReq.printEventReq()
        print("\nHow would you like to proceed with the event request review?")
        nextchoice = int(input("1. Enter feedback and forward to Administrative Manager \n2.Exit\n"))
        if nextchoice == 1:
            feedback = input("Please enter your feedback : ")
            eventReq.UpdateEventRequest("FMFeedback", feedback)
        else:
            print("Thank You!")
    elif choice == 2:
        print("Below are the extra Budget requests")
        extraBudget.printBudgetList("service")
        extraBudget.printBudgetList("production")
        nextchoice = input("\nPlease enter the ID of the request you would to approve. Else, press N : ").lower()
        if nextchoice != "n":
            budget, index = extraBudget.getBudgetByID(nextchoice)
            budget["approved"] = 1
            extraBudget.UpdateBudgetApproval(budget, index)
            extraBudget.printBudgetList("service")
            extraBudget.printBudgetList("production")

    else:
        print("Thank You!")


def adminManagerMenu():
    print("What would you like to do?")
    print("1. Review a Customer Event Request \n2. Exit")
    choice = int(input("Enter choice : "))
    print(choice)
    if choice == 1:
        print("Below is the customer event request :")
        eventReq.printEventReq()
        print("\nHow would you like to proceed with the event request review?")
        nextchoice = int(input("1.Approve Event Request \n2.Reject Event Request \n3.Exit\n"))
        if nextchoice == 1:
            eventReq.UpdateEventRequest("AMapproval", "YES")
            eventReq.UpdateEventRequest("status", "APPROVED")
            eventReq.printEventReq()
            print("EVENT APPROVED! ")
        elif nextchoice == 2:
            eventReq.UpdateEventRequest("AMapproval", "NO")
            eventReq.UpdateEventRequest("status", "REJECTED")
            eventReq.printEventReq()
            print("EVENT REJECTED! ")
            # eventReq.eventRequest.clear()
        else:
            print("Thank You!")
    else:
        print("Thank You!")


def seniorHRManagerMenu():
    print("What would you like to do?")
    print("1. Review Extra Staff Requests\n2. Exit")
    choice = int(input("Enter choice : "))
    if choice == 1:
        print("Below are the extra Staff requests")
        extraStaff.printStaffList("service")
        extraStaff.printStaffList("production")
        nextchoice = input("\nPlease enter the ID of the request you would to approve. Else, press N : ").lower()
        if nextchoice != "n":
            staff, index = extraStaff.getStaffByID(nextchoice)
            staff["approved"] = 1
            extraStaff.UpdateStaffApproval(staff, index)
            extraStaff.printStaffList("service")
            extraStaff.printStaffList("production")
        else:
            print("Thank You")
    else:
        print("Thank You!")



def productionManagerMenu():
    print("Below is the customer event request :")
    eventReq.printEventReq()
    status = eventReq.getEventRequestStatus()
    if status != "APPROVED":
        print("Event is not approved yet. Please check later")
    else:
        print("\nHow would you like to proceed with the event request ?")
        nextchoice = int(input("1. Create/Review requests for Extra Staff \n2. Create/Review Task Application \n3. Create/Review requests for Extra Budget\n4. Exit\n"))
        if nextchoice == 1:
            print("EXTRA STAFF NEEDED")
            extraStaff.printStaffList("production")
            thenchoice = int(input("Would you like to request for extra staff?\n1. Yes\n2. No\n"))
            if thenchoice == 1:
                department = input("Department(Production/Service) : ").lower()
                jobTitle = input("Job Title : ")
                expYears = input("Experience Years : ")
                description = input("Job Description : ")
                ID = input("ID : ")
                staff = [extraStaff.createExtraStaff(department, jobTitle, expYears, description, ID)]
                extraStaff.AddStaffists(staff)
                extraStaff.printStaffList("production")
            else:
                print("Thank You")
        elif nextchoice == 2:
                tasklist = []
                thenchoice = 1
                while thenchoice == 1:
                    print("Enter Task Details below")
                    department = input("Department(Production/Service) : ").lower()
                    subteam = input("Subteam : ")
                    name = input("Employee Name : ")
                    details = input("Task Description : ")
                    task = tasks.createTask(department, subteam, name, details)
                    print(task)
                    tasklist.append(task)
                    thenchoice = int(input("Would you like to create more task allocations?\n1. Yes\n2. No\n"))

                print(tasklist)
                tasks.AddTaskLists(tasklist)
                tasks.printTaskList("production")

        elif nextchoice == 3:
            print("EXTRA BUDGET")
            extraBudget.printBudgetList("production")
            thenchoice = int(input("Would you like to request for extra budget?\n1. Yes\n2. No\n"))
            if thenchoice == 1:
                department = input("Department(Production/Service) : ").lower()
                amount = input("Amount : ")
                description = input("Description/Reason : ")
                ID = input("ID : ")
                budget = [extraBudget.createExtraBudget(department, amount, description, ID)]
                extraBudget.AddBudgetists(budget)
                extraBudget.printBudgetList("production")
            else:
                print("Thank You")
        else:
            print("Thank You!")


def serviceManagerMenu():
    print("Below is the customer event request :")
    eventReq.printEventReq()
    status = eventReq.getEventRequestStatus()
    if status != "APPROVED":
        print("Event is not approved yet. Please check later")
    else:
        print("\nHow would you like to proceed with the event request ?")
        nextchoice = int(input("1. Create/Review requests for Extra Staff \n2. Create/Review Task Application \n3. Create\Review requests for Extra Budget\n4. Exit\n"))
        if nextchoice == 1:
            print("EXTRA STAFF NEEDED")
            extraStaff.printStaffList("service")
            thenchoice = int(input("Would you like to request for extra staff?\n1. Yes\n2. No\n"))
            if thenchoice == 1:
                department = input("Department(Production/Service) : ").lower()
                jobTitle = input("Job Title : ")
                expYears = input("Experience Years : ")
                description = input("Job Description : ")
                ID = input("ID : ")
                staff = [extraStaff.createExtraStaff(department, jobTitle,expYears, description, ID)]
                print("STAFF IN MAIN CODE : ", staff)
                extraStaff.AddStaffists(staff)
                extraStaff.printStaffList("service")
            else:
                print("Thank You")
        elif nextchoice == 2:
            thenchoice = int(input("Would you like to create task allocations?\n1. Yes\n2. No\n"))
            if thenchoice == 1:
                tasklist = []
                while thenchoice == 1:
                    print("Enter Task Details below")
                    department = input("Department(Production/Service) : ").lower()
                    subteam = input("Subteam : ")
                    name = input("Employee Name : ")
                    details = input("Task Description : ")
                    task = tasks.createTask(department, subteam, name, details)
                    tasklist.append(task)
                    thenchoice = int(input("Would you like to create more task allocations?\n1. Yes\n2. No\n"))
                tasks.SaveTaskList(tasklist)
                tasks.printTaskList("service")
            else:
                tasks.printTaskList("service")

        elif nextchoice == 3:
                print("EXTRA BUDGET")
                extraBudget.printBudgetList("service")
                thenchoice = int(input("Would you like to request for extra budget?\n1. Yes\n2. No\n"))
                if thenchoice == 1:
                    department = input("Department(Production/Service) : ").lower()
                    amount = input("Amount : ")
                    description = input("Description/Reason : ")
                    ID = input("ID : ")
                    budget = [extraBudget.createExtraBudget(department, amount, description, ID)]
                    extraBudget.AddBudgetists(budget)
                    extraBudget.printBudgetList("service")
                else:
                    print("Thank You")
        else:
            print("Thank You!")


def subTeamMenu(username):
    print("Below is you task List")
    task, index = tasks.getTaskByName(username)
    tasks.printTaskByName(task)
    print("\nHow would you like to proceed with the task ?")
    choice = int(input("1. Add plan, comments and extra budget if needed \n2. Exit\n"))
    if choice == 1:
        print("Enter Task Details below")
        task["plan"] = input("Plan : ")
        task["comment"] = input("Comments : ")
        task["extraBudget"] = input("Extra Budget : ")
        tasks.UpdateTaskByName(task, index)
        tasks.printTaskByName(task)
    else:
        print("Thank You!")


def hrAssistantMenu():
    print("hrAssistantMenu")


def marketingAssistantMenu():
    print("marketingAssistantMenu")


def marketingOfficerMenu():
    print("marketingOfficerMenu")


def accountantMenu():
    print("accountantMenu")


roleMenus = [custServiceMenu, seniorCustManagerMenu, hrAssistantMenu, seniorHRManagerMenu, marketingAssistantMenu,
             marketingOfficerMenu, adminManagerMenu, accountantMenu, financeManagerMenu, productionManagerMenu,
             serviceManagerMenu, subTeamMenu]


def performMenuActions(menuName):
    [menu() for menu in roleMenus if menuName == menu.__name__]
    return

