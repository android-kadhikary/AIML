class A:
    attributeC = "Class A attribute"

    def __init__(self, attributeA, attributeB,protectedV, privateV):
        self.attributeA = attributeA
        self.attributeB = attributeB
        self._protectedV=protectedV
        self.__privateV=privateV
    def __str__(self):
        return f"A(attributeA={self.attributeA}, attributeB={self.attributeB})"
        
    
    def methodA(self):
        return "Method A called"
    
    def get_privateVariable(self):
        return self.__privateV
    
    # def get___privateV(self):
    #     return self.__privateV


    # def set___privateV(self, privateV):
    #     if privateV == 0:
    #         print("privateV cannot be zero")
    #         raise ValueError("privateV cannot be zero")
    #     self.__privateV=self.__privateV+" updated to "+str(privateV)
    #     #return self.__privateV


object1= A("at1", "at2" , "I am protected variable", "I am private variable")

# print (object1.attributeB)
# print (object1)
# print (object1.methodA())
# print (object1.attributeC)
try:
    print (object1.get_privateVariable())
    print ("__privateV = ",object1._A__privateV) # access with _ClassName__privateV
    print ("__privateV = ",object1.__privateV)
except AttributeError as e:
    print(f"Error: {e}")
print ("_protectedV =" , object1._protectedV)


#print (object1.set___privateV(10))
#print (object1.get___privateV())

class ChildA(A):
    
    def methodA(self):
        return super().methodA() + " overridden in ChildA"
    

childObject= ChildA("child at1", "child at2", "child protected", "child private")
print (childObject)

print (childObject.methodA())
        