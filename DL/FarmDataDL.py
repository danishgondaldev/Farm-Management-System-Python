import os.path
from BL.FarmDataBL import FarmDataBL

class FarmDataDL:

    data = FarmDataBL()

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2], line[3], line[4]

    @staticmethod
    def readDataFromFile(path):
        if (os.path.exists(path)):
            fileVariable = open(path, 'r')
            records = fileVariable.read().split("\n")
            fileVariable.close()
            for line in records:
                eggs, eggs_price, milk, milk_price, farm_sales = CredentialsDL.parseData(line)
                data.eggs = eggs
                data.eggs_price = eggs_price
                data.milk = milk
                data.milk_price = milk_price
                data.farm_sales = farm_sales
            return True
        else:
            return False

    @staticmethod
    def storeFarmDataIntoFile(user, path):
        file = open(path, 'w')
        file.write(data.eggs + "," + data.eggs_price + "," + data.milk  + "," + data.milk_price + "," + data.farm_sales)
        file.close()

    @staticmethod
    def calculateFodderCost(costanimals, costbirds):
        fodderCost = (int(FarmDataDL.data.fodder_animals) * int(costanimals)) + (int(FarmDataDL.data.fodder_birds) * int(costbirds))
        return fodderCost
