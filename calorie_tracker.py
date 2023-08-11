from dataclasses import dataclass   # As we just need individual fields
import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 2500           # kcal
PROTEIN_GOAL = 80                   # grams
FAT_GOAL = 80                       # grams
CARBS_GOAL = 350                    # grams

today = []

@dataclass                          # Automatically generates methods for data storage class
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int 

def plot_macronutrients_distribution(ax):
    protein_sum = sum(food.protein for food in today)
    fats_sum = sum(food.fat for food in today)
    carbs_sum = sum(food.carbs for food in today)
    
    labels = ['Proteins', 'Fats', 'Carbs']
    sizes = [protein_sum, fats_sum, carbs_sum]
    
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Macronutrients Distribution")

def plot_macronutrients_progress(ax):
    protein_sum = sum(food.protein for food in today)
    fats_sum = sum(food.fat for food in today)
    carbs_sum = sum(food.carbs for food in today)
    
    ax.bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4, label="Calories Eaten")
    ax.bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4, label="Calorie Goal")
    ax.legend()
    ax.set_title("Macronutrients Progress")

def plot_calories_goal_progress(ax):
    calorie_sum = sum(food.calories for food in today)
    remaining_calories = CALORIE_GOAL_LIMIT - calorie_sum
    
    labels = ["Calories", "Remaining"]
    sizes = [calorie_sum, remaining_calories]
    
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Calories Goal Progress")

def plot_progress_over_time(ax):
    cumulative_calories = np.cumsum([food.calories for food in today])
    ax.plot(list(range(len(today))), cumulative_calories, label="Calories Eaten")
    ax.plot(list(range(len(today))), [CALORIE_GOAL_LIMIT] * len(today), label="Calorie Goal")
    ax.legend()
    ax.set_title("Progress Over Time")

# Main program loop
while True:
    print("""
    (1) Add a new food
    (2) Visualize progress
    (q) Quit
    """)

    choice = input("Choose an option: ")

    if choice == '1':
        print("Adding a new food!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        proteins = int(input("Proteins: "))
        fats = int(input("Fats: "))
        carbs = int(input("Carbs: "))
        food = Food(name, calories, proteins, fats, carbs)
        today.append(food)
        print("Succesfully added!")

    elif choice == '2':
        fig, axs = plt.subplots(2, 2)

        plot_macronutrients_distribution(axs[0, 0])
        plot_macronutrients_progress(axs[0, 1])
        plot_calories_goal_progress(axs[1, 0])
        plot_progress_over_time(axs[1, 1])
        
        fig.tight_layout()
        plt.show()

    elif choice == 'q':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice!")