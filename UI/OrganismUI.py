from BL.OrganismBL import OrganismBL
from DL.OrganismDL import OrganismDL

class OrganismUI:
    @staticmethod
    def addOrganism():
        name = input("Enter Name: ")
        weight = int(input("Enter Weight (in kg): "))
        species = input("Enter Species (Animal or Bird): ")
        health = input("Enter Health Condition: ")
        price = int(input("Enter Price: "))
        org = OrganismBL(name, weight, species, health, price)
        return org
    
    @staticmethod
    def getNameForHealthUpdate():
        name = input("Enter Name of Animal/Bird whose health you want to update: ")
        return name

    @staticmethod
    def getNameForWeightUpdate():
        name = input("Enter Name of Animal/Bird whose weight you want to update: ")
        return name

    @staticmethod
    def getNameForFodderAllocation():
        name = input("Enter Name of Animal/Bird for fodder allocation: ")
        return name

    @staticmethod
    def getUpdatedHealth():
        health = input("Enter Updated health condition: ")
        return health

    @staticmethod
    def getUpdatedWeight():
        weight = int(input("Enter Updated weight condition: "))
        return weight

    @staticmethod
    def getFodder():
        fodder = int(input("Enter fodder allocation (in kg) "))
        return fodder

    @staticmethod
    def costInputAnimals():
        animalscost = int(input("Enter cost of one kg fodder of animals: "))
        return animalscost
    
    @staticmethod
    def costInputBirds():
        birdscost = int(input("Enter cost of one kg  food of birds: "))
        return birdscost

    @staticmethod
    def showFodderCost(fodder_cost):
        print("The total cost of fodder used is " + str(fodder_cost) + " Rupees. ")

    @staticmethod
    def getNameForDelete():
        name = input("Enter name of the organism you want to delete: ")
        return name

    @staticmethod
    def getNameForPurchase():
        name = input("Enter name of organism you want to purchase: ")
        return name
    
    @staticmethod
    def viewOrganisms():
        print("Name     Weight      Species     Health      Price")
        for i in range (0, len(OrganismDL.org_data)):
            print(OrganismDL.org_data[i].name + "       " + str(OrganismDL.org_data[i].weight) + "      " + OrganismDL.org_data[i].species + "       " + OrganismDL.org_data[i].health + "      " + str(OrganismDL.org_data[i].price) + "\n")