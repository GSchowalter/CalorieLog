class Meal:
    def __init__(self, item, calories):
        self.item = item
        self.calories = calories
        self.entry = self.toString()

    def toString(self):
        str = '{}:\t{}\n'.format(self.item, self.calories)
        return str