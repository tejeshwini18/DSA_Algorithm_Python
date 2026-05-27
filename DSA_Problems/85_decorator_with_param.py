import time

def calculate_time(func):
    '''
    This decorator takes the actual function as input.

    Inside that, I’m defining a wrapper function using *args and **kwargs so that it can work with any function irrespective of parameters.

    Then before calling the actual function, I’m storing the start time using time.time().

    After that, I’m executing the original function.

    Once execution is completed, I’m again capturing the end time and calculating the difference to get total execution time.

    Finally, I’m printing the execution time and returning the wrapper function.

    And while using @calculate_time, Python automatically passes the function to the decorator.
    '''
    def wrapper(*args, **kwargs):

        start = time.time()

        func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start)

    return wrapper


@calculate_time
def display():
    for i in range(1000000):
        pass


display()