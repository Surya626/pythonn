
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items=len(names)
random_num=random.randint(0,num_items-1)

bill_payer =names[random_num]

print(bill_payer + " is going to buy the meal today!")