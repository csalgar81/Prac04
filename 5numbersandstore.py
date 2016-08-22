numbers = []
for i in range (0,4+1):
    input_number = int(input("Enter number "))
    numbers.append(input_number)
for i in range (0,4+1):
    print ("Number: {}".format(numbers[i]))
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))

