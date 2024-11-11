#Object Oriented Program
#It always classes and objects/instances
# A class always has properties/attributes
#Objects come from a class
#An object takes on the properties of a class
#methods are items of the class

# Syntax of OOP
# Creating a class
#Cohort class and class name start with an upper case
#class Cohort:
#name
#description
#start_date
#end_date

# with in the cohort class, 
# Add a constructor for the cohort class(Read about constructors)
# Add a method to the class that prints the cohort name and the total number of students
#Create a new instance/object of the cohort class.


#Constructor to initialize attributesof the cohort
class Cohort:
    def __init__(self, name, description, start_date, end_date, total_students):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_students = total_students

#Method to print the cohort"s name and total number of students
def print_details(self):
    print(f'Cohort Name:{self.name}')
    print(f'Total number of students:{self.total_students}')

#Creating a new instance/object of the cohort class
cohort1 = Cohort(
    name="OOP in python",
    description="Its always classes and objects/instances",
    start_date="2024-08-20",
    end_date="2026-12-10",
    total_students=80)
cohort1.print_details()