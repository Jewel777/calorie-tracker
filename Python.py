users = []
food_menu = []

# Function to add a user
def add_user(name, calorie_goal):
    user = {
        'name': name,
        'calorie_goal': calorie_goal,
        'selected_food': []
    }
    users.append(user)
    return "User added!"

# Function to view all users
def view_users():
    return users

# Function to add a food item
def add_food_item(name, calories):
    food_item = {
        'name': name,
        'calories': calories
    }
    food_menu.append(food_item)
    return "Food item added!"

# Function to view the food menu
def view_food_menu():
    return food_menu

# Function to select a food item for a user
def select_food_for_user(user_name, food_name):
    for user in users:
        if user['name'] == user_name:
            for food in food_menu:
                if food['name'] == food_name:
                    user['selected_food'].append(food)
                    return "Food item selected!"
    return "User or food item not found!"

# Function to calculate total calories for a user
def calculate_total_calories(user_name):
    for user in users:
        if user['name'] == user_name:
            total_calories = sum(food['calories'] for food in user['selected_food'])
            return total_calories
    return "User not found!"

# Function to compare total calories with the user's goal
def compare_calories_to_goal(user_name):
    for user in users:
        if user['name'] == user_name:
            total_calories = calculate_total_calories(user_name)
            if total_calories <= user['calorie_goal']:
                return f"Total calories ({total_calories}) are within the goal ({user['calorie_goal']})."
            else:
                return f"Total calories ({total_calories}) exceed the goal ({user['calorie_goal']})."
    return "User not found!"

# Example usage
print(add_user("Dr. Kenan", 2000))             # Add a user
print(add_user("Jewel", 2500))
print(add_user("Dr. Ranjith", 1500))
print(add_user("Dr. Washim", 1900))
print(add_user("Dr. x", 1800))
print(view_users())

print(add_food_item("Burger", 500))
print(add_food_item("Salad", 300))
print(view_food_menu())

print(select_food_for_user("Dr. Kenan", "Burger"))
print(select_food_for_user("Dr. Kenan", "Salad"))
print(select_food_for_user("Dr. Ranjith", "Burger"))
print(select_food_for_user("Dr. Washim", "Salad"))

print(calculate_total_calories("Dr. Kenan"))
print(calculate_total_calories("Dr. Ranjith"))
print(calculate_total_calories("Dr. Wshim"))

print(compare_calories_to_goal("Dr. Kenan"))
print(compare_calories_to_goal("Dr. Ranjith"))
print(compare_calories_to_goal("Dr. Washim"))
