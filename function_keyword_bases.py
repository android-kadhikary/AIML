def func1(**students):
    for name, score in students.items():
        print(f"Student: {name}, Score: {score}")

func1(Alice=85, Bob=92, Charlie=78)

