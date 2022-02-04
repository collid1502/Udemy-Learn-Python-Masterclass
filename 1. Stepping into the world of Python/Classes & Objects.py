#####################################################################
####                       Classes & Objects                     ####
#####################################################################


# lets say im writing a programme and i want to model a particualr student, so i can create a "student data type"- aka a class.

class Student:
    
    def __init__(self, name, major, gpa, is_on_probation):       #This is an initialse function to map out what info we should have on the student data type
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation 
        
        
student1 = Student("Jim","Business",3.1,False) ;   #  a Student is thus created - aka an object 
student2 = Student("Pam","Art",2.5,True) ;

print(student1.name) ;  #prints out the student name 

print(student2.gpa) ; 


