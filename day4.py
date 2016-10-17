class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        age = initialAge
        
        if age <= 0:
            print("Age is not valid, Setting age to 0")
            age == 0
            
        
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age < 13:
            print("You are young")
            
        elif 12 < age < 18:
            print("You are a teenager")
            
        else:
            print("You are old")
    
    def yearPasses(self):
        # Increment the age of the person in here
        age = age + 1