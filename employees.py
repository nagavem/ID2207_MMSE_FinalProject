# Create ROLE ARRAYS
# IDENTIFY ROLES FROM NAMES

custService = ["sarah", "sam", "judy", "carine"]
seniorCustManager = ["janet"]
hrAssistant = ["maria"]
seniorHRManager = ["simon"]
marketingAssistant = ["emma"]
marketingOfficer = ["david"]
adminManager = ["mike"]
accountant = ["fredrik", "sophia"]
financeManager = ["alice"]
productionManager = ["jack"]
serviceManager = ["natalie"]
photographerSubTeam = ["tobias", "magdalena"]
chefSubTeam = ["helen", "diana", "chris", "daniel", "marilyn"]

dictEmp = {
    "custService" : custService,
    "seniorCustManager" : seniorCustManager,
    "hrAssistant" : hrAssistant,
    "seniorHRManager" :seniorHRManager,
    "marketingAssistant" : marketingAssistant,
    "marketingOfficer": marketingOfficer,
    "adminManager" : adminManager,
    "accountant" : accountant,
    "financeManager" : financeManager,
    "productionManager" : productionManager,
    "serviceManager" : serviceManager,
    "subTeam": photographerSubTeam + chefSubTeam
}


allEmployees = sum(dictEmp.values(), [])


def getRole(username):
    role = ""
    for role, name in dictEmp.items():
        if username in name:
            print(role)
            break
    return role
