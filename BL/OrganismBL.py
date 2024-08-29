class OrganismBL:
    name = "Random"
    weight = 0
    species = "Random"
    health = "Random"
    price = 0
    fodder = 0

    def __init__(self, *args):
        if len(args) == 5:
            self.name = args[0]
            self.weight = args[1]
            self.species = args[2]
            self.health = args[3]
            self.price = args[4]
        elif len(args) == 4:
            self.name = args[0]
            self.weight = args[1]
            self.species = args[2]
            self.health = args[3]
    def checkHealth(self):
        if (self.health == "Good"):
            return True
        else:
            return False