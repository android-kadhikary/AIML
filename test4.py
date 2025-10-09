try:
        print(5/0)

    # Catching both ValueError and ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
        print(f"An expected issue occurred: {type(e).__name__} - {e}")
        