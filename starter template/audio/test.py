# class human(object):
#     def __init__(self,name):
#         self.name=name
         
#     def eat():
#         print("eat human")    
             
# class mammal (object):   
#     def __init__(self,name):
#         self.name=name
 
 
           
# class Employee(human,mammal):
#     def __init__(self):
#         super(Employee,self).__init__()
#         print("that is it ")

# Employee()   



# def sum(a,b):
#     t=a*b
#     print(t)

# def sum(a,b,c):
#     t=a*b*c
#     print(t)

# # sum(2,5,3) 

# class humman :
#     def __int__(self,age):
#         self.age=age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,age):
#         if age>0:
#             self.__age=age
#         if age<=0:
#             self.__age=0
                               
# man =humman()
# man.age=-23
# print(man.age)                               
                  
class human :
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "hi my name is " +self.name
        
man  = human("Ahmed")
print(man)
man2 =human("kareem")                                     