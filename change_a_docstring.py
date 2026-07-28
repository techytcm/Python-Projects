def hello():
    """Old message."""
    print("Hello")

print(hello.__doc__)

hello.__doc__ = "Print a friendly greeting."

print(hello.__doc__)