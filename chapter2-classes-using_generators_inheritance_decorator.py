class InclusiveRange:
    def __init__(self, *args):
        numberOfArguments = len(args)
        if numberOfArguments < 1:
            raise TypeError('At least one argument is required.')
        elif numberOfArguments == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numberOfArguments == 2:
            (self.start, stop) = args
            self.step = 1
        elif numberOfArguments == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError("Maximum three arguments.You gave {} ".format(numberOfArguments))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


def main_generators():
    ranges = InclusiveRange(5, 210, 10)
    for x in ranges:
        print(x, end=' ')


# inheritance
class AllUsers:
    def __int__(self):
        pass

    def Register(self):
        print("Please Register")

    def Login(self):
        print("Welcome Member.")


class Admin(AllUsers):
    def __init__(self):
        pass

    def Register(self):
        print("Admins need not register")

    def Login(self):
        print("Welcome Admin")


class Members(AllUsers):
    def __init__(self):
        pass


def main_inheritance():
    admin = Admin()
    admin.Register()
    admin.Login()
    member = Members()
    member.Register()
    member.Login()


# decorators
class Dog:
    def __init__(self, **kwargs):
        self.properties = kwargs

    @property
    def Color(self):
        return self.properties.get('color', None)

    @Color.setter
    def Color(self, color):
        self.properties['color'] = color

    @Color.deleter
    def Color(self):
        del self.properties['color']


def main():
    lucky = Dog()# now we are going to use the decorator function as a normal property
    lucky.Color = 'black and yellow'
    print(lucky.Color)


if __name__ == "__main__":
    main()