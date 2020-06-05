
# Create a program that prints the ingredients of your 3 favorite foods.
# The ingredients must be in a list inside of the foods list
# Before each food print "Food # X has the following ingredients". Where X is the index of the food.
# (Challange) You can only use the for in operation.
# (Extra Challenge) Make it a quiz game of guess the food based on its ingredients. Add more food items if needed.


favorite_foods_list = [
    ["tortilla chips", "beans",
     "fajitas", "cheese", "sour cream", "salsa"], ["noodles", "spaghetti sauce", "parmesan cheese"], ["mint chocolate chip ice cream", "waffle cone"]
]
slogan = "Food %s has the following ingredients:"

x = 0
# while x < len(favorite_foods_list):
#     print("Food #%s has the following ingredients: " % x)
#     for i in favorite_foods_list[x]:
#         print(" %s" % i)
#     x += 1

for food in favorite_foods_list:
    print("Food #%s has the following ingredients: " % x)
    for i in food:
        print(" %s" % i)
    x += 1
