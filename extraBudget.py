"""
THIS CONTAINS XTRA BUDEGT REQUEST
"""
import json
import os

def createExtraBudget(department, amount, description, ID):
    extraBudget = {
        "department": department,
        "amount": amount,
        "description": description,
        "ID": ID,
        "approved": 0
    }
    return extraBudget


def SaveBudgetList(budgetlist):
    with open('extraBudget.json', 'w') as fp:
        json.dump(budgetlist, fp)


def ReadBudgetFile():
    if os.stat('extraBudget.json').st_size != 0:
        with open('extraBudget.json', 'r') as fp:
            budgetList = json.load(fp)
    else:
        budgetList = []
    return budgetList


def AddBudgetists(listOfBudgets):
    budgetList = ReadBudgetFile()
    SaveBudgetList(budgetList + listOfBudgets)


def UpdateBudgetApproval(budget, index):
    budgetList = ReadBudgetFile()
    budgetList.pop(index)
    budgetList.insert(index, budget)
    SaveBudgetList(budgetList)


def getBudgetByID(ID):
    budgetList = ReadBudgetFile()
    index = next((index for (index, d) in enumerate(budgetList) if d["ID"] == ID), None)
    print(index)
    return budgetList[index], index


def printBudgetList(department):
    budgetList = ReadBudgetFile()
    if budgetList:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for item in budgetList:
            if item["department"] == department.lower():
                print("\tDEPARTMENT NAME : ", item["department"])
                print("\tAMOUNT : ", item["amount"])
                print("\tDESCRIPTION : ", item["description"])
                print("\tID : ", item["ID"])
                print("\tAPPROVED : ", item["approved"])
                print("---------------------------------------------------")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
