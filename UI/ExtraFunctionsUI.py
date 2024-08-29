class ExtraFunctionsUI:

    @staticmethod
    def menu():
        print("1. SignIn to the system")
        print("2. SignUp (for new users) ")
        print("Enter Option")
        option = int(input())
        return option
    
    @staticmethod
    def header():
        print("*************************************************************************")
        print("*                         FARM MANAGEMENT SYSTEM                        *")
        print("*************************************************************************")

    @staticmethod
    def AdminMenu():
        print("Press 1 to Add User")
        print("Press 2 to Add a New Organism")
        print("Press 3 to Update health of an Exisitng Organism ")
        print("Press 4 to Update weight of an Exisitng Organism ")
        print("Press 5 to Allocate fodder to an Organism ")
        print("Press 6 to Calculate cost of fodder of Farm")
        print("Press 7 to Delete an Exisitng Organism")
        print("Press 8 to Exit ")
        option = int(input("Enter Option "))
        return option

    @staticmethod
    def CustomerMenu():
        print("Press 1 to buy an organism ")
        print("Press 2 to Exit ")
        option = int(input("Enter Option: "))
        return option
    
    
    @staticmethod
    def nameNotFound():
        print("The organism with this name does not exist in system!!! ")