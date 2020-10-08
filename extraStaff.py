"""
THIS CONTAINS XTRA STAFF REQUEST
"""
import json
import os


def createExtraStaff(department, jobTitle, expYears, description, ID):
    extraStaff = {
        "department": department,
        "jobTitle": jobTitle,
        "expYears": expYears,
        "description": description,
        "ID": ID,
        "approved": 0
    }
    return extraStaff


def SaveStaffList(stafflist):
    with open('extraStaff.json', 'w') as fp:
        json.dump(stafflist, fp)


def ReadStaffFile():
    if os.stat('extraStaff.json').st_size != 0:
        with open('extraStaff.json', 'r') as fp:
            staffList = json.load(fp)
    else:
        staffList = []
    return staffList


def AddStaffists(listOfStaff):
    print("listOfStaff : ", listOfStaff)
    staffList = ReadStaffFile()
    SaveStaffList(staffList + listOfStaff)


def UpdateStaffApproval(staff, index):
    staffList = ReadStaffFile()
    staffList.pop(index)
    staffList.insert(index, staff)
    SaveStaffList(staffList)


def getStaffByID(ID):
    staffList = ReadStaffFile()
    index = next((index for (index, d) in enumerate(staffList) if d["ID"] == ID), None)
    print(index)
    return staffList[index], index


def printStaffList(department):
    staffList = ReadStaffFile()
    print("stafflist : in print: ", staffList)
    if staffList:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for item in staffList:
            if item["department"] == department.lower():
                print("\tDEPARTMENT NAME : ", item["department"])
                print("\tJOB TITLE : ", item["jobTitle"])
                print("\tEXPERIENCE YEARS : ", item["expYears"])
                print("\tJOB DESCRIPTION : ", item["description"])
                print("\tID : ", item["ID"])
                print("\tAPPROVED : ", item["approved"])
                print("---------------------------------------------------")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
