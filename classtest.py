class Dog():
    """A simple attempt to model a dog"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title()+" is now sitting.")

    def sit_over(self):
        """simulate rolling over in response to a command"""
        print(self.name.title()+" rolled over!")
dog=Dog('samt',2)
tommy=Dog('tommy',4)
dog.sit()
dog.sit_over()
tommy.sit()
