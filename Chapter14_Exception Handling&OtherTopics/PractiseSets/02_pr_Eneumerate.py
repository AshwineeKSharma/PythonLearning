# WAP to print third, fifth and seventh element from the list using eneumerate function.


fruits = ["Apple", "Mango", "Guava", "Grapes", "Orange", "Pineapple",
          "Pear", "Peaches", "Lichi", "Papaya", "Dragon Fruit", "Jack Fruit"]


# for i, item in enumerate(fruits):
#     if (i==2 or i== 4 or i==6):
#             print(i, item)


for i, item in enumerate(fruits):
    
    if (i==2):
            print(f"The 3rd element in the list is : {item}")

    elif (i==4):
            print(f"The 5th element in the list is : {item}")

    elif (i==6):
            print(f"and the 7th element in the list is : {item}")


