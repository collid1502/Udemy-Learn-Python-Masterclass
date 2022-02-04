#####################################################################
####                     Class Functions                         ####
#####################################################################


class Student:

    def __init__(self, name, major, gpa,
                 is_on_probation):  # This is an initialse function to map out what info we should have on the student data type
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
    def on_honor_roll(self):    # defines a function to calculate whether student is on the honor roll or not 
        if self.gpa >= 3.5:
            return True
        else:
            return False
    
    

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, False)



print(student1.on_honor_roll())      # returns if on honor roll or not

