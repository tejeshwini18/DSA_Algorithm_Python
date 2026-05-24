class ContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with ContextManager() as context:
    print("Inside the context")

print("Outside the context")

print(context)
