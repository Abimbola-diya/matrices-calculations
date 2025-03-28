# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:43:56 2024

@author: LENOVO L460
"""

class Car():
    '''a simple statement to represent a car'''
    def __init__(self,make,model,year):
        '''initializes attribute to describe a car'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading='200miles'
        

    def get_descriptive_name(self):
        '''returns a neatly formatted descriptive name'''
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        "prints a statement showing the car's mileage."
        print('This car has '+self.odometer_reading+' on it !')


