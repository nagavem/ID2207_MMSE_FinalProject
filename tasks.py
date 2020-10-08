"""
Contains TASKS that are a allocated by the PM/SM to their subteams
This also contains comments from the subteam
A list of tasks make a form
"""
import json


def createTask(department, subteam, name, details):
    task = {
        "department": department,
        "subteam": subteam,
        "employeeName": name,
        "details": details,
        "plan": "NA",
        "comment": "NA",
        "extraBudget": 0
    }
    return task


def printTaskList(department):
    tasklist = ReadTasksFile()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for task in tasklist:
        if task["department"] == department.lower():
            print("\tDEPARTMENT NAME : ", task["department"])
            print("\tSUBTEAM : ", task["subteam"])
            print("\tNAME : ", task["employeeName"])
            print("\tTASK DESCRIPTION : ", task["details"])
            print("\tPLAN : ", task["plan"])
            print("\tCOMMENTS : ", task["comment"])
            print("\tEXTRA BUDGET : ", task["extraBudget"], "\n---------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def SaveTaskList(tasklist):
    with open('tasks.json', 'w') as fp:
        json.dump(tasklist, fp)


def ReadTasksFile():
    with open('tasks.json', 'r') as fp:
        tasklist = json.load(fp)
        return tasklist

def AddTaskLists(listOfTasks):
    tasklist = ReadTasksFile()
    SaveTaskList(tasklist + listOfTasks)

def UpdateTaskByName(task, index):
    tasklist = ReadTasksFile()
    tasklist.pop(index)
    tasklist.insert(index, task)
    SaveTaskList(tasklist)


def getTaskByName(name):
    tasklist = ReadTasksFile()
    index = next((index for (index, d) in enumerate(tasklist) if d["employeeName"].lower() == name.lower()), None)
    print(index)
    return tasklist[index], index


def printTaskByName(task):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\tDEPARTMENT NAME : ", task["department"])
    print("\tSUBTEAM : ", task["subteam"])
    print("\tNAME : ", task["employeeName"])
    print("\tTASK DESCRIPTION : ", task["details"])
    print("\tPLAN : ", task["plan"])
    print("\tCOMMENTS : ", task["comment"])
    print("\tEXTRA BUDGET : ", task["extraBudget"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
