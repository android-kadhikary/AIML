# A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

def function3_decorator(function_parameter):
    print("This is function3_decorator")
    def complete_work(): ### this inner funtion is called closure function or wrapper function
        print("initial_work()")
        function_parameter()
        print("end_work()")
        return "Completed all the work"
    return complete_work

@function3_decorator
def iT_work():
    print("Wecome to It!")
    #return "Wecome to " + name +"!"

iT_work()
print('**********')