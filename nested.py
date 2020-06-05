# first_name = "Ally"
# last_name = "Brannon"
# if first_name == "Ally":
#     print("My name is Ally")
#     if len(last_name) > 6:
#         print("My last name is %s" % last_name)
#     elif last_name == "Brannon":
#         print("I told you my last name!")
#     else:
#         print("I don't know the answer!")

my_num = 10
my_second_num = 5

while my_num > 0:
    print(my_num)
    my_num -= 2
    while my_second_num <= 20:
        print("second num %s" % my_second_num)
        my_second_num += 5
    my_second_num = 5

print("this prints now!")
