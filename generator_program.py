# def echo():
#     value = yield
#     print (value)
#     yield
# generator = echo()
# next(generator)
# generator.send('Karabi')
# generator.close()
def count_up_to(n):
    i=0
    while i<=n:
        yield i
        i+=1
            
print(next(count_up_to(2))) # calling the function from initial part
counter=count_up_to(2)      # calling the function from initial part
print(next(counter))
print(next(counter))
print(next(counter))
counter.close