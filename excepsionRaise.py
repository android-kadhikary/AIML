def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")# raise exception, as python has no checked exception
    print(f"Age is {age}")
try:
    check_age(-5)
except ValueError as e:
    print(e)
