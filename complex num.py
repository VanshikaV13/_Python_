#Assignment 2
#make a data structure to store complex number.

class Number:
    def __init__(self,real,imaginary):
        self.real=real
        self.img=imaginary
    def __str__(self):     #a special method, like __init__ ,
                            #that is supposed to return a string representation of an object.
        
        if type(self.real)==int and type(self.img)==int :
            return ("%i + %i i"%(self.real,self.img))       #string formatting
        elif type(self.real)==int and type(self.img)==float :
            return ("%i + %0.2f i"%(self.real,self.img))
        elif type(self.real)==float and type(self.img)==int :
            return ("%0.2f + %i i"%(self.real,self.img))
        elif type(self.real)==float and type(self.img)==float:
            return ("%0.2f + %0.2f i"%(self.real,self.img))
        

obj=Number(12,5)
print(obj)


obj=Number(0.5,-1)
print(obj)


'''print(self.real," + ",self.img,"i")
print(self.real," - ",self.img*(-1),"i")'''


