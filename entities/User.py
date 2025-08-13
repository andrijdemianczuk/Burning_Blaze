class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email