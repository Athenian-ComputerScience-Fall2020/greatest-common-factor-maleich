# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def find_gcf(x,y):   # Do not change function name!
        for i in range (x + 1, 0, -1):
        if x % i == 0:
            if y % i == 0:
                gcf = i
                break
            else:
                continue
    return gcf


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print(find_gcf(6,9))

    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

