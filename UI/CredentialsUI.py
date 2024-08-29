from BL.CredentialsBL import CredentialsBL

class CredentialsUI:

    @staticmethod
    def TakeInputFromConsole():
        userName = input("Enter Username: ")
        userPassword = input("Enter User Password: ")
        userRole = input("Enter User Role: ")
        user = CredentialsBL(userName, userPassword, userRole)
        return user

    @staticmethod
    def takeInputwithOutRole():
        userName = input("Enter Username:")
        userPassword = input("Enter User Password: ")
        user = CredentialsBL(userName, userPassword)
        return user
    
    @staticmethod
    def addUser():
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        role = input("Enter Role: ")
        user = CredentialsBL(username, password, role)
        return user
