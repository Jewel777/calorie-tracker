# calorie-tracker
"A simple Python-based calorie tracker that allows users to manage food intake and compare it against personal calorie goals."
# 🥗 Calorie Tracker

This is a simple Python project that allows users to:

- Add users with personal calorie goals
- Add food items with calorie values
- Select food items for users
- Calculate total calories consumed
- Compare total calories with the user’s daily calorie goal

## 🔧 Features

- User and food item management
- Calorie tracking per user
- Goal comparison messages
- Fully in-memory (no database required)

## 🚀 Getting Started

To run the program:

🧠 Code Breakdown
Global Lists
users = []
food_menu = []

🧠 Code Breakdown
Global Lists
users = []
food_menu = []

You store user data and food items here.

👤 add_user(name, calorie_goal)
Creates a dictionary for a new user with their name, goal, and an empty list for selected foods. Then appends it to the users list.

👁️ view_users()
Returns the list of all user dictionaries.

🍔 add_food_item(name, calories)
Creates a dictionary for a food item and appends it to the food menu.

📜 view_food_menu()
Returns the list of all food items.

🍽️ select_food_for_user(user_name, food_name)
Finds the user by name.


Then, it finds the food item by name.


If both are found, that food will be added to the user’s selected_food list.



🔢 calculate_total_calories(user_name)
Looks up the user by name.


Adds up the calories from all selected food items.



⚖️ compare_calories_to_goal(user_name)
Gets the total calories.


compared to the user's goal.


Returns a message based on whether the user is within or exceeding their calorie goal.



🧪 Example Usage
You’ve demonstrated:
Adding users and food.


Viewing them.


Selecting food.


Calculating totals.


Comparing to the goal.


