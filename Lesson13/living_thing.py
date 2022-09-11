class LivingThing:
    def __init__(self, habit):
        self.habit = habit


class Animal(LivingThing):
    def __init__(self, is_carnivore):
        super.__init__()
        self.is_canivore = is_carnivore


class Plant(LivingThing):
    def __init__(self):
        super.__init__()


class Flower(Plant):
    def __init__(self, colour):
        super.__init__()
        self.colour = colour


class Tree(Plant):
    def __init__(self, branch_num):
        super.__init__()
        self.branch_num = branch_num


class Caribou(Animal):
    def __init__(self):
        super.__init__()


class Wolf(Animal):
    def __init__(self, pack_leader):
        super.__init__()
        self.pack_leader = pack_leader


class Dandelion(Flower):
    def __init__(self):
        super.__init__()


class Rose(Flower):
    def __init__(self):
        super.__init__()


class Maple(Tree):
    def __init__(self):
        super.__init__()