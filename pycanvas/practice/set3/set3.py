class Car:
    def __init__(self, is_suv, num_wheels, color, gas_in_gallons):
        """
        Initialize a Car object.
        
        Args:
            is_suv (bool): True if the car is an SUV, False if it's a sedan
            num_wheels (int): Number of wheels the car has
            color (str): Color of the car
            gas_in_gallons (float): Current amount of gas in gallons
        """
        self.is_suv = is_suv
        self.num_wheels = num_wheels
        self.color = color
        self.gas_in_gallons = gas_in_gallons

class Person:
    def __init__(self, has_jetpack, has_fuel, eye_color, weight):
        """
        Initialize a Person object.
        
        Args:
            has_jetpack (bool): True if person has a jetpack
            has_fuel (bool): True if person has fuel for jetpack
            eye_color (str): Color of person's eyes
            weight (float): Person's weight in pounds
        """
        self.has_jetpack = has_jetpack
        self.has_fuel = has_fuel
        self.eye_color = eye_color
        self.weight = weight

def can_drive(pers, car):
    """
    Check if a person can drive a car.
    Only people with blue eyes who weigh less than 200 pounds can drive cars.
    
    Args:
        pers (Person): The person to check
        car (Car): The car they want to drive
        
    Returns:
        bool: True if person can drive, False otherwise
    """
    # TODO: Implement this function
    pass


def get_all_suvs(cars):
    """
    Get all SUVs from a list of cars.
    
    Args:
        cars (list): List of Car objects
        
    Returns:
        list: List containing only the SUV cars
    """
    # TODO: Implement this function
    pass


def add_wheels_of_sedans(cars):
    """
    Add up the total number of wheels for all sedans in the car list.
    
    Args:
        cars (list): List of Car objects
        
    Returns:
        int: Total number of wheels for all sedans
    """
    # TODO: Implement this function
    pass


def can_fly(pers):
    """
    Check if a person can fly.
    A person can fly if they have both a jetpack and fuel.
    
    Args:
        pers (Person): The person to check
        
    Returns:
        bool: True if person can fly, False otherwise
    """
    # TODO: Implement this function
    pass


def needs_to_get_gas(car, gallons_needed):
    """
    Check if a car needs to get gas for a trip.
    
    Args:
        car (Car): The car to check
        gallons_needed (float): Gallons needed for the trip
        
    Returns:
        bool: True if car needs more gas, False if it has enough
    """
    # TODO: Implement this function
    pass


def count_cars_by_color(cars, color):
    """
    Count how many cars have a specific color.
    
    Args:
        cars (list): List of Car objects
        color (str): Color to count
        
    Returns:
        int: Number of cars with that color
    """
    # TODO: Implement this function
    pass


def get_heaviest_person(people):
    """
    Find the heaviest person from a list of people.
    
    Args:
        people (list): List of Person objects
        
    Returns:
        Person: The person with the highest weight, or None if list is empty
    """
    # TODO: Implement this function
    pass


def refuel_car(car, gallons_to_add):
    """
    Add gas to a car's tank.
    
    Args:
        car (Car): The car to refuel
        gallons_to_add (float): Amount of gas to add
        
    Returns:
        float: New total gallons in the car
    """
    # TODO: Implement this function
    pass
