i=0
number = int(input("Enter the size of the pattern: "))
while i <= number - 1:
        for j in range(number):
                print("*", end=" ")
        print()
        i+=1
