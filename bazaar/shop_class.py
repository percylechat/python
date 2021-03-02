class Shop():
    def __init__(self, money:int, inventory: list, lvl_decoration: int = 0, lvl_bargain:int = 0, lvl_fabrication:int = 0):
        self.money = money
        self.inventory = inventory
        self.lvl_decoration = lvl_decoration
        self.lvl_bargain = lvl_bargain
        self.lvl_fabrication = lvl_fabrication
    def get_money(self):
        return str(self.money)