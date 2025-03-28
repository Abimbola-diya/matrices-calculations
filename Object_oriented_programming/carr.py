class Car():
    '''a simple statement to represent a car'''
    def __init__(self,make,model,year):
        '''initializes attribute to describe a car'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=200
        self.fuel_guage=25

    def get_descriptive_name(self):
        '''returns a neatly formatted descriptive name'''
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        "prints a statement showing the car's mileage."
        print('This car has '+str(self.odometer_reading)+'-miles on it !')
        
    def update_odometer_reading(self,mileage):
        '''updates the odometer reading to the most reccent mileage
        rejects the change if it attempts to roll back the odometer reading
        to a value less than previous mileage value
        '''
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer! ")
            

    def increment_odometer(self,mileage):
        '''add the given mileage to the previous odometer reading
        it rejects odometer reading if the added mileage is a negative number
        '''
        if  self.odometer_reading>(self.odometer_reading+mileage):
            print("odometer doesn't accept negative values")
        else:
            self.odometer_reading+=mileage

    def gas_tank(self):
        '''tells you the fuel level of your car tank'''
        print('the remaining fuel left is '+str(self.fuel_guage)+'-litres')


