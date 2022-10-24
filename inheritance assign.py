'''class parent:
    def func1(self):
        print("This is function 1")
class parent2(parent):
    def func2(self):
        print("This is function 2")
class child1(parent2):
    def func3(self):
        print("This is function 3")
class child2(parent2):
    def func4(self):
        print("This is function 4")
class child(child1,child2):
    def func5(self):
        print("function 5")'''

class Director:
    def __init__(self,collegename,city):
        self.name=collegename
        self.place=city
    def view(self):
        print(self.name,self.place)
        
        
class HOD(Director):
    def __init__(self,collegename,city):
        Director.__init__(self,collegename,city)
        self.branch="ComputerScience"
    def view(self):
        print(self.name,self.place,self.branch)

class Faculty1(HOD):
    def __init__(self,collegename,city,subject1):
        HOD.__init__(self,collegename,city)
        self.subject1=subject1
    def view(self):
        print(self.name,self.place,self.branch,self.subject1)

class Faculty2(HOD):
    def __init__(self,collegename,city,subject2):
        HOD.__init__(self,collegename,city)
        self.subject2=subject2
    def view(self):
        print(self.name,self.place,self.branch,self.subject2)

class Students(Faculty1,Faculty2):
    def __init__(self,collegename,city,subject1,subject2,section):
        Faculty1.__init__(self,collegename,city,subject1)
        Faculty2.__init__(self,collegename,city,subject2)
        self.section=section
    def view(self):
        print("COLLEGE : ",self.name,"   ",self.place,"\nCOURSE AND BRANCH : ",self.branch,"\nSECTION : ",self.section,"\nSUBJECT TEACHERS : ",self.subject1,"    ",self.subject2)

obj=Students("Ajay Kumar Garg Engineering College","Ghaziabad","B.tech CSE-1","Data Structure","Discrete Mathematics")
obj.view()
        
    
