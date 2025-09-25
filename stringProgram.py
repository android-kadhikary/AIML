str1= 'Hello'
str2 = "karabi"
list1= ["people", "are", "good"]
lower_case_string = "in lower case"
print (str1.lower())
print (lower_case_string.capitalize())
print (lower_case_string.title())
name="abc"
print("name")
join_string=" see ".join(list1)
list2= ["apple", "kiwi", "mango"]
addWord=" and "

print (addWord.join(list2))
print(join_string)

# Checking if all characters are printable
text=' hello dear friend '
is_printable = text.isprintable()  # True
print(is_printable)
# Checking if all characters are whitespace
text="      "
is_space = text.isspace()  # False
print("is_space",is_space)
# Checking if the string is a valid identifier
is_identifier = text.isidentifier()  # False
print("len()","len()".isidentifier())  # Output: True
print("def","def".isidentifier())   # Output: True
print("_private_var".isidentifier()) # Output: True
print("123invalid".isidentifier())   # Output: False (starts with a digit)
print("with space".isidentifier())   # Output: False (contains a space)
print("invalid!".isidentifier())    # Output: False (contains a special character)
print("class".isidentifier())

name= "karabi"
age=43
classname='python'
formated_string="Name: %s, Age: %d"%(name, age)
print (formated_string)
formated_string1="Name: {}, Age: {}, Class Nama: {}".format(name,age,classname)
print (formated_string1)