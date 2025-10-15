# Exception Handling
class NewException(Exception):
    print("inside NewException class")

def convert_to_int(s):
    try:
        return int(s)
    except ValueError as e:
        raise NewException("Conversion error") from e
        #raise RuntimeError("Failed to convert input to int")

try:
    int = convert_to_int("abr")
    print ("Converted integer:", int)
except RuntimeError as e:
    print("caught:", e)
#print("original cause",e.__cause__)
except Exception as e:
    print("caught:", e)
else:
    print("Conversion successful:", int)
finally:
    print("Execution completed")    


# raise Exception("This is a custom exception") 
