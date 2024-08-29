import os.path
from array import *
from BL.OrganismBL import OrganismBL
from DL.FarmDataDL import FarmDataDL

class OrganismDL:
    org_data = []
    org_data_increasing = []
    org_data_decreasing = []

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2], line[3], line[4]

    @staticmethod
    def readOrganismData(path):
        if (os.path.exists(path)):
            fileVariable = open(path, 'r')
            records = fileVariable.read().split("\n")
            fileVariable.close()
            for line in records:
                tempData = OrganismDL.parseData(line)
                name = tempData[0]
                weight = int(tempData[1])
                species = tempData[2]
                health = tempData[3]
                price = int(tempData[4])
                user = OrganismBL(name, weight, species, health, price)
                OrganismDL.org_data.append(user)
            return True
        else:
            return False
    
    @staticmethod
    def addOrganismToList(organism):
        temp = OrganismBL()
        temp.name = organism.name
        temp.species = organism.species
        temp.health = organism.health
        temp.weight = int(organism.weight)
        temp.price = int(organism.price)
        OrganismDL.org_data.append(temp)
        OrganismDL.saveOrganismUpdate()
    
    @staticmethod
    def chkName(organism):
        for i in  OrganismDL.org_data:
            if (i.name == organism.name) :
                return False
        return True
    
    @staticmethod
    def saveOrganismUpdate():
        path = "inventory.txt"
        temp = 0
        file = open(path, 'w')
        for i in range (0, len(OrganismDL.org_data)):
            if (i == 0):
                file.write(OrganismDL.org_data[i].name + "," + str(OrganismDL.org_data[i].weight) + "," + OrganismDL.org_data[i].species + "," + OrganismDL.org_data[i].health + ",")
                if (int(OrganismDL.org_data[i].price) > 0):
                    file.write(str(OrganismDL.org_data[i].price))
                else:
                    file.write(str(temp))
            else:
                file.write("\n" + OrganismDL.org_data[i].name + "," + str(OrganismDL.org_data[i].weight) + "," + OrganismDL.org_data[i].species + "," + OrganismDL.org_data[i].health + ",")
                if (int(OrganismDL.org_data[i].price) > 0):
                    file.write(str(OrganismDL.org_data[i].price))
                else:
                    file.write(str(temp))
        file.close()
    
    @staticmethod
    def chkName(name):
        for i in range (0, len(OrganismDL.org_data)):
            if name == OrganismDL.org_data[i].name:
                return i
        return -1


    @staticmethod
    def sortingIncreasing():
        OrganismDL.org_data_increasing = sorted(OrganismDL.org_data, key = lambda x : (x.weight))
    
    @staticmethod
    def updateHealth(updatedHealth, index):
        OrganismDL.org_data[index].health = updatedHealth
    
    @staticmethod
    def updateWeight(updatedWeight, index):
        OrganismDL.org_data[index].weight = updatedWeight
    
    @staticmethod
    def allocateFodder(allocatedFodder, index):
        OrganismDL.org_data[index].fodder = allocatedFodder
        if (OrganismDL.org_data[index].species == "Animal"):
            FarmDataDL.data.fodder_animals = OrganismDL.org_data[index].fodder
        else:
            FarmDataDL.data.fodder_birds = OrganismDL.org_data[index].fodder 

    @staticmethod
    def deleteOrganism(index):
        OrganismDL.org_data.remove(OrganismDL.org_data[index])
        


