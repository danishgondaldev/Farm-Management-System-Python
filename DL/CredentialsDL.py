import os.path
from BL.CredentialsBL import CredentialsBL

class CredentialsDL:
    usersList = []

    @staticmethod
    def addUserIntoList(user):
        CredentialsDL.usersList.append(user)

    @staticmethod
    def SignIn(user):
        for storedUser in CredentialsDL.usersList:
            if(storedUser.userName == user.userName and storedUser.userPassword == user.userPassword):
                return storedUser
        return None

    @staticmethod
    def chkName(user):
        for storedUser in CredentialsDL.usersList:
            if(storedUser.userName == user.userName):
                return False
        return True

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2]

    @staticmethod
    def readDataFromFile(path):
        if (os.path.exists(path)):
            fileVariable = open(path, 'r')
            records = fileVariable.read().split("\n")
            fileVariable.close()
            for line in records:
                userName, userPassword, userRole = CredentialsDL.parseData(line)
                user = CredentialsBL(userName, userPassword, userRole)
                CredentialsDL.addUserIntoList(user)
            return True
        else:
            return False

    @staticmethod
    def storeUserIntoFile(user, path):
        file = open(path, 'a')
        file.write("\n" + user.userName + "," + user.userPassword + "," + user.userRole)
        file.close()