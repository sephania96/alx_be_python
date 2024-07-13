try:
    f = open("explore_dateme.py")
    print("Opening....")
except FileNotFoundError:
    print("File does not exist")