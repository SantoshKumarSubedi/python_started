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
class Car():
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car"""
        self.make=make;
        self.model=model;
        self.year=year;
        self.odometer_reading=0
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading+=miles


    def get_descriptive_name(self):
        """return a neatly formatted discriptive name."""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(400)
my_new_car.read_odometer()
my_new_car.update_odometer(20)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
