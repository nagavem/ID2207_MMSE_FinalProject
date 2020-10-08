# THIS IS AN EVENT REQUEST - PERSISTENT DATA

import json

"""eventRequest = {
    "ID": 1,
    "clientName": "Nakita",
    "eventStartDate": "10th April 2020",
    "eventEndDate": "12th April 2020",
    "description": "Two day conference for SCANIA",
    "budget": "50000 SEK",
    "SCSApproval": "NA",
    "FMFeedback": "NA",
    "AMapproval": "NA",
    "status": "OPEN"
}
"""


def createEventRequest(clientName, eventStartDate, eventEndDate, description, budget, ID):
    eventReq = {
        "ID": ID,
        "clientName": clientName,
        "eventStartDate": eventStartDate,
        "eventEndDate": eventEndDate,
        "description": description,
        "budget": budget,
        "SCSApproval": "NA",
        "FMFeedback": "NA",
        "AMapproval": "NA",
        "status": "OPEN"
    }
    SaveEventRequestFile(eventReq)
    return


def printEventReq():
    eventReq = ReadEventRequestFile()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\tCUSTOMER NAME : ", eventReq["clientName"])
    print("\tCUSTOMER ID : ", eventReq["ID"])
    print("\tEVENT START DATE : ", eventReq["eventStartDate"])
    print("\tEVENT END DATE : ", eventReq["eventEndDate"])
    print("\tEVENT DETAILS : ", eventReq["description"])
    print("\tEVENT BUDGET : ", eventReq["budget"])
    print("\tSENIOR CUSTOMER SERVICE >> APPROVAL : ", eventReq["SCSApproval"])
    print("\tFINANCE MANAGER >> FEEDBACK : ", eventReq["FMFeedback"])
    print("\tADMINISTRATIVE MANAGER >> APPROVAL : ", eventReq["AMapproval"])
    print("\tSTATUS : ", eventReq["status"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def SaveEventRequestFile(eventRequest):
    with open('eventReq.json', 'w') as fp:
        json.dump(eventRequest, fp)


def ReadEventRequestFile():
    with open('eventReq.json', 'r') as fp:
        eventRequestDict = json.load(fp)
        return eventRequestDict


def UpdateEventRequest(key, value):
    eventRequest = ReadEventRequestFile()
    eventRequest[key] = value
    SaveEventRequestFile(eventRequest)


def getEventRequestStatus():
    eventRequest = ReadEventRequestFile()
    return eventRequest["status"]
