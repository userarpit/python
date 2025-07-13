try:
    # Code that might raise an exception
    result = 10 / 0
except ValueError:
    # Handle the exception
    print("Cannot divide by zero")
else: # if no exception is raised
    
    # Code to execute if no exception occurs
    print("Calculation successful")
finally:
    # Code that always executes
    print("Execution complete")