"""

THIS IS WHERE EVENT REQUEST IS CREATED FOR THE FIRST TIME, TILL IT IS APPROVED BY ALL THE STAKEHOLDERS

"""


import employees
import welcome
import eventReq
import menu as menuActions

successfulLogin, name = welcome.welcome()
print(successfulLogin)
print(name)

if successfulLogin == 1:
    roleName = employees.getRole(name)
    if roleName != "subTeam":
        menuName = roleName + "Menu"
        menuActions.performMenuActions(menuName)
    else:
        menuActions.subTeamMenu(name)



