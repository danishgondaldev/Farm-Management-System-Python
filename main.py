from DL.CredentialsDL import CredentialsDL
from DL.FarmDataDL import FarmDataDL
from DL.OrganismDL import OrganismDL
from BL.CredentialsBL import CredentialsBL
from BL.FarmDataBL import FarmDataBL
from BL.OrganismBL import OrganismBL
from UI.CredentialsUI import CredentialsUI
from UI.ExtraFunctionsUI import ExtraFunctionsUI
from UI.OrganismUI import OrganismUI
import os
from time import sleep

def main():
    pathCredentials = "users.txt"
    pathOrganism = "inventory.txt"
    CredentialsDL.readDataFromFile(pathCredentials)
    OrganismDL.readOrganismData(pathOrganism)
    option = 0
    adminoption = 0
    customeroption = 0
    while (option != 3):
        os.system("cls")
        ExtraFunctionsUI.header()
        option = ExtraFunctionsUI.menu()
        if (option == 1):
            os.system("cls")
            ExtraFunctionsUI.header()
            user = CredentialsUI.takeInputwithOutRole()
            user = CredentialsDL.SignIn(user)
            if (user != None):
                if (user.isAdmin()):
                    while (adminoption != 8):
                        os.system("cls")
                        ExtraFunctionsUI.header()
                        adminoption = ExtraFunctionsUI.AdminMenu()
                        os.system("cls")
                        ExtraFunctionsUI.header()
                        if (adminoption == 1):
                            user = CredentialsUI.addUser()
                            CredentialsDL.addUserIntoList(user)
                            CredentialsDL.storeUserIntoFile(user, pathCredentials)
                        if (adminoption == 2):
                            org = OrganismUI.addOrganism()
                            OrganismDL.addOrganismToList(org)
                        if (adminoption == 3):
                            OrganismUI.viewOrganisms()
                            name = OrganismUI.getNameForHealthUpdate()
                            index = OrganismDL.chkName(name)
                            if (index > 0):
                                updatedHealth = OrganismUI.getUpdatedHealth()
                                OrganismDL.updateHealth(updatedHealth, index)
                                OrganismDL.saveOrganismUpdate()
                            else:
                                ExtraFunctionsUI.nameNotFound()
                                sleep(3)
                        if (adminoption == 4):
                            OrganismUI.viewOrganisms()
                            name = OrganismUI.getNameForWeightUpdate()
                            index = OrganismDL.chkName(name)
                            if (index > 0):
                                updatedWeight = int(OrganismUI.getUpdatedWeight())
                                OrganismDL.updateWeight(updatedWeight, index)
                                OrganismDL.saveOrganismUpdate()
                            else:
                                ExtraFunctionsUI.nameNotFound()
                                sleep(3)
                        if (adminoption == 5):
                            OrganismUI.viewOrganisms()
                            name = OrganismUI.getNameForFodderAllocation()
                            index = OrganismDL.chkName(name)
                            if (index > 0):
                                allocatedFodder = int(OrganismUI.getFodder())
                                OrganismDL.allocateFodder(allocatedFodder, index)
                                OrganismDL.saveOrganismUpdate()
                            else:
                                ExtraFunctionsUI.nameNotFound()
                                sleep(3)
                        if (adminoption == 6):
                            cost_animals = OrganismUI.costInputAnimals()
                            cost_birds = OrganismUI.costInputBirds()
                            fodder_cost = FarmDataDL.calculateFodderCost(cost_animals, cost_birds)
                            OrganismUI.showFodderCost(fodder_cost)
                            sleep(3)
                        if (adminoption == 7):
                            OrganismUI.viewOrganisms()
                            name = OrganismUI.getNameForDelete()
                            index = OrganismDL.chkName(name)
                            if (index > 0):
                                OrganismDL.deleteOrganism(index)
                                OrganismDL.saveOrganismUpdate()
                            else:
                                ExtraFunctionsUI.nameNotFound()
                                sleep(3)
                else:
                    while(customeroption != 2):
                        os.system("cls")
                        ExtraFunctionsUI.header()
                        customeroption = ExtraFunctionsUI.CustomerMenu()
                        os.system("cls")
                        ExtraFunctionsUI.header()
                        if (customeroption == 1):
                            OrganismUI.viewOrganisms()
                            name = OrganismUI.getNameForPurchase()
                            index = OrganismDL.chkName(name)
                            if (index > 0) :
                                OrganismDL.deleteOrganism(index)
                                OrganismDL.saveOrganismUpdate()
                            else:
                                ExtraFunctionsUI.nameNotFound()
                                sleep(3)
                sleep(3)
        elif (option == 2):
            os.system("cls")
            ExtraFunctionsUI.header()
            user = CredentialsUI.TakeInputFromConsole()
            CredentialsDL.addUserIntoList(user)
            CredentialsDL.storeUserIntoFile(user, pathCredentials)
if __name__ == "__main__":
    main()