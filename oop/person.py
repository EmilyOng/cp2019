class Person:
    #parent class (superclass)
    ''' constructor (initializer) '''
    def __init__(self,pid,name,weight,height):
        ''' method '''
        #name,weight,height
        self.pid=pid
        self.name=name
        self.weight=weight
        self.height=height
    ''' accessor (getty) '''
    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight
    def get_height(self):
        return self.height
    ''' modifier (setty) '''
    def set_name(self,new_name):
        self.name=new_name
    def set_weight(self,new_weight):
        self.weight=new_weight
    def set_height(self,new_height):
        self.height=new_height
    ''' utility (helper) '''
    def display(self):
        print("Name:",self.name)
        print("Weight:",self.weight)
        print("Height:",self.height)
class Student(Person):
    #children class (subclass)
    #establish a relationship between parent and child
    ''' constructor '''
    def __init__(self,pid,name,weight,height,classid):
        super().__init__(pid,name,weight,height)
        self.classid=classid
    ''' accesor '''
    def get_class(self):
        return self.classid
    ''' modifier '''
    def set_class(self,new_class):
        self.classid=new_class
    def set_name(self,house):
        self.name=house+self.name
    def display(self):
        super().display()
        print("Class:",self.classid)
class Staff(Person):
    #children class (subclass)
    #establish a relationship between parent and child
    ''' constructor '''
    def __init__(self,pid,name,weight,height,dept):
        super().__init__(pid,name,weight,height)
        self.dept=dept
    ''' accesor '''
    def get_dept(self):
        return self.dept
    ''' modifier '''
    def set_dept(self,new_dept):
        self.dept=new_dept
    def display(self):
        super().display()
        print("Dept:",self.dept)


''' object '''
person_1=Person(1,"Emily",50,160)
person_2=Person(2,"Jane",50,160)
person_2.set_name("Janet")
student_1=Student(1011,"emilyong",50,160,"19Y5C34")
student_1.set_class("19Y6C34")
#overriden method
student_1.set_name("Bennu ")
#child can use inherited methods from parent class
staff_1=Staff(14,"Oop",50,160,"Physics")
school=[]
school.append(staff_1)
school.append(student_1)
#polymorphism
for user in school:
    user.display()

'''
encapsulation: class -> data, method (public, private)
inheritance (code reuse)
polymorphism (code generality)
'''
