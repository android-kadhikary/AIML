# string1=(" I am learing python:")
# word="python"
# def find_the_word_in_string(string1,word):
#     if word in string1:
#         return True
#     else:
#         return False
    

# available=find_the_word_in_string(string1,word)
# if available:
#     print("python is available")
# else:
#     print("python is not available")
    
# def revstr(st):
#     return st[ : :-1]

import re


text = "AppleApple,Orange,apple,aPple,Banana"

# Split by "apple" regardless of case, using re.IGNORECASE (or re.I)
result = re.split(r'apple', text, flags=re.IGNORECASE)

print(result)