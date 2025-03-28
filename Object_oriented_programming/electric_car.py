class ElectricCar(Car):
    '''represents aspect of a car ,specific to electric vehicles'''
    def __init__(self,make,model,year):
        '''initializes attribute from parent class'''
        super().__init__(make,model,year)
        self.battery_power=70
        self.battery_efficiency_factor=0.3
        self.battery=battery()
        
    def describe_battery(self):
        '''print a statemnt describing the cars battery power'''
        print('this car has a '+str(self.battery_power)+'kwh battery capacity')

    def gas_tank(self):
        '''Electric cars don't have gas tanks.'''
        print('this car does not have a gas tank,ask for current_battery_capacity() instead')

    def current_battery_capacity(self,miles_travelled):
        '''calculates the Electric car current battery capacity based
        on the number of miles travelled
        '''
        print('this is not totally efficient,but gives you the remaining\n'
              + 'battery life based on the number of miles the car has travelled'+
            '\n' )
        if (miles_travelled*self.battery_efficiency_factor)>self.battery_power:
            print('maximum mile range of this tesla is 233.33 miles')
        else:    
            current_battery_capacity=self.battery_power-(miles_travelled*self.battery_efficiency_factor)
            battery_percent=(current_battery_capacity/self.battery_power)*100
            print('battery life remaininig '+str(round(battery_percent,2))+'percent')
            
class battery():
    '''a simple atrtempt to model a battery for an electric car'''

    def __init__(self,battery_size=70):
        '''initializees the battery's attributes'''
        self.battery_size=battery_size

    def describe_battery(self):
        '''prints a statement describing the battery size'''
        print('this car has a '+str(self.battery_size)+'_kwh battery')

    def get_range(self):
        '''prints a statement about the range this battery provides'''
        if self.battery_size==70:
            range=240

        elif self.battery_size==85:
            range=270
        message='this car can go approximately '+str(range)
        message+=' milles on a full charge'
        print(message)
