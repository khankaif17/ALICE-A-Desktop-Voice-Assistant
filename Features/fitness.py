import tkinter as tk 
# Create the window.
root = tk.Tk()

# Set window title.
root.title("A.L.I.C.E Fitness Planner")

# Set window size.
root.geometry("400x400")
# Create labels for age, gender, fitness goal, fitness level, height and weight.
age_label = tk.Label(root, text="Age:")
age_label.grid(row=0, column=0)
gender_label = tk.Label(root, text="Gender (male/female):")
gender_label.grid(row=1, column=0)
fitness_goal_label = tk.Label(root, text="Fitness Goal (weight_loss/muscle_gain):")
fitness_goal_label.grid(row=2, column=0)
fitness_level_label = tk.Label(root, text="Fitness Level (beginner/intermediate/advanced):")
fitness_level_label.grid(row=3, column=0)
height_label = tk.Label(root, text="Height (in cm):")
height_label.grid(row=4, column=0)
weight_label = tk.Label(root, text="Weight (in kg):")
weight_label.grid(row=5, column=0)

# Create entries for age, gender, fitness goal, fitness level, height and weight.
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1)
gender_entry = tk.Entry(root)
gender_entry.grid(row=1, column=1)
fitness_entry = tk.Entry(root)
fitness_entry.grid(row=2, column=1)
fitness_level_entry = tk.Entry(root)
fitness_level_entry.grid(row=3, column=1)
height_entry = tk.Entry(root)
height_entry.grid(row=4, column=1)
weight_entry = tk.Entry(root)
weight_entry.grid(row=5, column=1)



# Function to suggest diet and exercise.
def submit():
    # Get the values from thecomplete entries.
    age = int(age_entry.get())
    gender = gender_entry.get()
    fitness_goal = fitness_entry.get()
    fitness_level = fitness_level_entry.get()
    height = int(height_entry.get())
    weight = int(weight_entry.get())

    # Suggest diet and exercise plan based on age, gender and fitness goal.
    if age > 18 and gender == 'male' and fitness_goal == 'weight_loss':
        diet_plan = 'Low-carb diet'
        exercise_plan = 'Cardio, strength training and HIIT'
    elif age > 18 and gender == 'male' and fitness_goal == 'muscle_gain':
        diet_plan = 'High-protein, calorie-dense diet'
        exercise_plan = 'Strength training and HIIT'
    elif age > 18 and gender == 'female' and fitness_goal == 'weight_loss':
        diet_plan = 'Low-calorie, low-carb diet'
        exercise_plan = 'Cardio and strength training'
    elif age > 18 and gender == 'female' and fitness_goal == 'muscle_gain':
        diet_plan = 'High-protein, calorie-dense diet'
        exercise_plan = 'Strength training and HIIT'
    elif age <= 18 and gender == 'male' and fitness_goal == 'weight_loss':
        diet_plan = 'Low-calorie, low-carb diet with plenty of fruits and vegetables'
        if fitness_level == 'beginner':
            exercise_plan = 'more Cardio and light strength training'
        elif fitness_level == 'intermediate':
            exercise_plan = 'more Cardio and moderate strength training'
        elif fitness_level == 'advanced':
            exercise_plan = 'more Cardio and heavy strength training'
        else:
            exercise_plan = 'more Cardio and moderate strength training'
    elif age <= 18 and gender == 'male' and fitness_goal == 'muscle_gain':
        diet_plan = 'High-protein, calorie-dense diet with plenty of fruits and vegetables'
        if fitness_level == 'beginner':
            exercise_plan = 'More strength training and light HIIT'
        elif fitness_level == 'intermediate':
            exercise_plan = 'More strength training and moderate HIIT'
        elif fitness_level == 'advanced':
            exercise_plan = 'More strength training and heavy HIIT'
        else:
            exercise_plan = 'More strength training and moderate HIIT'
    elif age <= 18 and gender == 'female' and fitness_goal == 'weight_loss':
        diet_plan = 'Low-calorie, low-carb diet with plenty of fruits and vegetables'
        if fitness_level == 'beginner':
            exercise_plan = 'More cardio and light strength training'
        elif fitness_level == 'intermediate':
            exercise_plan = 'More cardio and moderate strength training'
        elif fitness_level == 'advanced':
            exercise_plan = 'More cardio and heavy strength training'
        else:
            exercise_plan = 'More cardio and light strength training'
    elif age <= 18 and gender == 'female' and fitness_goal == 'muscle_gain':
        diet_plan = 'Highcomplete-protein, calorie-dense diet with plenty of fruits and vegetables'
        if fitness_level == 'beginner':
            exercise_plan = 'More strength training and light HIIT'
        elif fitness_level == 'intermediate':
            exercise_plan = 'More strength training and moderate HIIT'
        elif fitness_level == 'advanced':
            exercise_plan = 'More strength training and heavy HIIT'
        else:
            exercise_plan = 'More strength training and moderate HIIT'
    else:
        diet_plan = 'Balanced diet with plenty of fruits and vegetables'
        if fitness_level == 'beginner':
            exercise_plan = 'Moderate intensity cardio and light strength training'
        elif fitness_level == 'intermediate':
            exercise_plan = 'Moderate intensity cardio and moderate strength training'
        elif fitness_level == 'advanced':
            exercise_plan = 'High intensity cardio and heavy strength training'
        else:
            exercise_plan = 'Moderate intensity cardio and strength training'

    # Suggest recipes based on height, weight and fitness goal.
    if height > 180 and weight > 80 and fitness_goal == 'weight_loss':
        recipes = 'Grilled fish with steamed vegetables, oatmeal with fruits'
    elif height > 180 and weight > 80 and fitness_goal == 'muscle_gain':
        recipes = 'Grilled chicken with roasted potatoes, quinoa with nuts'
    elif height <= 180 and weight <= 80 and fitness_goal == 'weight_loss':
        recipes = 'Salad with tuna, quinoa with fruits'
    elif height <= 180 and weight <= 80 and fitness_goal == 'muscle_gain':
        recipes = 'Grilled steak with roasted vegetables, oatmeal with nuts'
    else:
        recipes = 'Grilled fish with steamed vegetables, quinoa with nuts'

    # Display the suggested diet, exercise plan and recipes.
    diet_label = tk.Label(root, text="Suggested Diet Plan: " + diet_plan)
    diet_label.grid(row=7, column=0)
    exercise_label = tk.Label(root, text="Suggested Exercise Plan: " + exercise_plan)
    exercise_label.grid(row=8, column=0)
    recipes_label = tk.Label(root, text="Suggested Recipes: " + recipes)
    recipes_label.grid(row=9, column=0)
    
    
# Create button to submit information.
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=6, column=1)

# Start the tkinter event loop.
root.mainloop()