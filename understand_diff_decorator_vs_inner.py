#decoretor function
def hospital_work(name):
    print("This is function2")
    return "Best treatment in " + name +"!"


def banking_work(name):
    print("This is function2")
    return "Best saving account on " + name +"!"

def initial_work():
    print("initial_work")
    return "awesome! completed initial_work"

def end_work():
    print("The end! continue the next...")
    return "awesome! completed end_work"

def iT_work(name):
    print("Wecome to ", name, " !")
    return "Company name is " + name +"!"

def function3_decorator(function_parameter,name):
    print("This is function3_decorator")
    def complete_work(): ### this inner funtion is called closure function or wrapper function
        print(initial_work())
        function_parameter(name)
        print(end_work())
        return "Completed all the work"
    return complete_work()

# @function3_dec
# def iT_work():
#     print("Wecome to It!")
#     #return "Wecome to " + name +"!"

# iT_work()
# print('**********')



message=function3_decorator(iT_work,"TCS")
print(message)

