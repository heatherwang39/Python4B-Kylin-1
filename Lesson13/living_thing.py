class LivingThing:
    def __init__(self, habit):
        self.habit = habit


class Animal(LivingThing):
    def __init__(self, habit, is_carnivore):
        self.is_canivore = is_carnivore
        super.__init__(habit)


class Plant(LivingThing):
    def __init__(self, habit):
        super.__init__(habit)


class Flower(Plant):
    def __init__(self, colour, habit):
        self.colour = colour
        super.__init__(habit)


class Tree(Plant):
    def __init__(self, branch_num, habit):
        self.branch_num = branch_num
        super.__init__(habit)


class Caribou(Animal):
    def __init__(self, habit, is_carnivore):
        super.__init__(habit, is_carnivore)


class Wolf(Animal):
    def __init__(self, habit, is_carnivore, pack_leader):
        self.pack_leader = pack_leader
        super.__init__(habit, is_carnivore)


class Dandelion(Flower):
    def __init__(self, colour, habit):
        super.__init__(colour, habit)


class Rose(Flower):
    def __init__(self, colour, habit):
        super.__init__(colour, habit)


class Maple(Tree):
    def __init__(self, branch_num, habit):
        super.__init__(branch_num, habit)