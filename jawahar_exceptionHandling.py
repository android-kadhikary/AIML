def convert_to_int(s):
try:
return int(s)
except ValueError as e:
raise RuntimeError("Failed to convert input to int")

try:
convert_to_int("abc")
except RuntimeError as e:
print("caught:", e)
print("original cause",e.__cause__)