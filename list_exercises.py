# Create a list of numbers, print their sum.

num_list = [17, 37, 40, 9, 29, 38]

# num_sum = 0

# for number in num_list:
#     num_sum += number

print("Here is my list", num_list)
# print("This is the sum of the list: ", num_sum)

# Create a list of numbers, print the largest of the numbers.

# largest = num_list[0]
# for number in num_list:
#     if number > largest:
#         largest = number

# print("This is the largest number: ", largest)

# Create a list of numbers, print the smallest of the numbers.

# smallest = num_list[0]
# for number in num_list:
#     if number < smallest:
#         smallest = number

# print("This is the smallest number: ", smallest)

# Create a list of numbers, print each number in the list that is even.

for even_num in num_list:
    if even_num % 2 == 0:
        print(even_num)
