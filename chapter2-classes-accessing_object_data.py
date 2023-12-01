# Hard to track code
class Human:
    def __init__(self, height=5.08):
        self.height = height


def main():
    ramu = Human()
    print(ramu.height)
    ramu.height = 5.11
    print(ramu.height)

# Recode the class
class Human:
    def __init__(self, **kwargs):
        self.variables = kwargs
    def set_manyVariables(self, **kwargs):
        self.variables = kwargs
    def set_variables(self, key, value):
        self.variables[key] = value
    def get_variables(self, key):
        return self.variables.get(key, None)


def main():
    mana = Human(name='Mana')
    print("Object Mana's name:", mana.variables['name'])
    ManaName = mana.variables['name']
    mana.set_variables('class', 'two')
    print(ManaName, "reads at class", mana.get_variables('class'))
    mana.set_manyVariables(school='balika school', height=4.54)
    print(ManaName, "has height of", mana.variables['height'], "and her school's name is", mana.variables['school'])
    babu = Human(name='Babu', student_of='Class Three', reads_at=' Balak School', height=5.21)
    BabuName = babu.variables['name']
    print(BabuName, "he is a student of", babu.variables['student_of'], "and he reads at", babu.variables['reads_at'], "and his height is", babu.variables['height'])


if __name__ == "__main__":
    main()