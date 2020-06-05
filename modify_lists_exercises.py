# Create a program that asks for several numbers from a user and then adds them up. You must use a List.

# After the user enters a number it prints all the numbers the user has entered and ask for another number to be entered.
# Let the user know if they enter 0 it will do the addition. Then when they push enter it does the addition and prints the results.
# (Challenge) You cannot use an if statement.
# (Extra Challange)The only variables allow are "number", "numbers", and "result" (IE only 3 variables allowed and they are all named those specific things)
# (Extra Extra) do not have the List print with the 0 at the end of the list.


number = None
numbers_list = []
result = 0
while number != 0:
    try:
        number = int(
            input("Please give me a number to add (Pressing 0 will do the addition)\n"))
    except ValueError:
        print("You must give a number!")
        number = None

    else:
        while number:
            numbers_list.append(number)
            print(numbers_list)
            break

# for number in numbers_list:
#     result += number1
# print(result)

result = sum(numbers_list)
print(result)
