#1 ) Inner function
# def parent_function(type,*name):
#     print("This is parent function")
#     def child_function1():
#         print("This is child 1 function greetings to ",name)

#     def child_function2():
#         print(f"This is child 2{name} function")

#     if type=='greetings':
#         child_function1()
#     else:    
#         child_function2()

#2) sending function as parameter to another function  
# parent_function("none")
# def function1():
#     print("This is function1")
#     return "karabi"

# def function2():
#     print("This is function2")
#     return "Riya"

# def function3(function_parameter):
#     print("This is function3")
#     print("name  =",function_parameter())
#     return "hello"

# function3(function2)

#3)returing function from another function
# def awesome(name):
#     print("This is function1")
#     return name, "awesome."

# def beautiful(name):
#     print("This is function2")
#     return "beautiful " + name +"!"

# def function3(function_parameter,name):
#     print("This is function3")
#     # print("name  =",function_parameter())
#     return function_parameter(name)

# print(function3(beautiful,"karabi"))


#4)decoretor function
def initial_work():
    print("initial_work")
    return "awesome! completed initial_work"

def end_work():
    print("The end! continue the next...")
    return "awesome! completed end_work"

def hospital_work(name):
    print("This is function2")
    return "beautiful " + name +"!"


def banking_work(name):
    print("This is function2")
    return "beautiful " + name +"!"



def function3_dec(function_parameter):
    print("This is function3_dec")
    def complete_work(): ### this inner funtion is called closure function or wrapper function
        print(initial_work())
        function_parameter()
        print(end_work())
        #return "Completed all the work"
    return complete_work

@function3_dec
def iT_work():
    print("Wecome to It!")
    #return "Wecome to " + name +"!"

# iT_work()
# print('**********')

message=function3_dec(iT_work)
message()

