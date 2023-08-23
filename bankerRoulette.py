# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

random_name = random.randint(0, len(names) - 1 )
# selected_name = names.pop(random_name)
selected_name = names[random_name]
print(f"{selected_name} is going to buy the meal today!")