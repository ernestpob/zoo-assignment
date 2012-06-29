from zooassign import*

###                     CLASS LIVING BEINGS
class LIVING_BEINGS(Zoo):
    def __init__(self,zoo,name,age,gender):
        ZOO.__init__(self,zoo.name,zoo.location)     #inherited from ZOO Class
        self.age = age                  # age is integer
        self.gender = gender        # gender is string

    def Print_Details(self):
        pass
class Humans
    def __init__(self,livingbeing,status)
        self.status = status
###                     CLASS VISITOR

class Visitor(Humans):
    def __init__(self,human,name,ticket_number):
        LIVING_BEING.__init__(self,human.name,human.age,human.gender)
        self.ticket_number = ticket_number

    def Take_Photo(self,Animals):
        pass
    
    def Print_Details(self):
        pass
###                     CLASS EMPLOYEE
class Employee(Humans):
    def __init__(self,human,name,position,department,salary):
        LIVING_BEING.__init__(self,human.name,human.age,human.gender)
        self.position = position
        self.department = department
        self.salary = salary

    def Print_Details(self):
        pass

###                     CLASS ANIMALS
class Animals(LIVING_BEING):
    def __init__(self,animal,population):
        LIVING_BEING.__init__(self,animal.name,animal.age,animal.gender)
        self.population = population

    def Make_Noise(self):
        pass

    def Print_Details(self):
        pass



