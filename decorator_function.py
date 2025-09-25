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
        print("insert complete work def ")
        print(initial_work())
        function_parameter()
        print(end_work())
        #return "Completed all the work"
    return complete_work

@function3_dec
def iT_work():
    print("Wecome to IT!")
    #return "Wecome to " + name +"!"

#iT_work()

message=function3_dec(iT_work)

print("Message =", message)
message()

