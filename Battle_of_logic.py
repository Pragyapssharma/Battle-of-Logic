import tkinter as tk
import random

# Define the questions and answers
questions = [
    {"question": "What is the next number in the sequence: 2, 4, 8, 16, ?", "answer": "32"},
    {"question": "If 3 cats catch 3 mice in 3 minutes, how many cats are needed to catch 100 mice in 100 minutes?", "answer": "3"},
    {"question": "Which number is missing: 5, 10, ?, 20, 25", "answer": "15"},
    {"question": "John is older than Alice, but younger than Sam. Who is the youngest?", "answer": "Alice"},
    {"question": "A farmer has 10 cows. If he sells 4 and buys 6, how many cows does he have now?", "answer": "12"}
]

# Initialize player health
player_health = 100
enemy_health = 100

# Function to check the answer
def check_answer():
    global player_health, enemy_health
    answer = answer_entry.get()

    if answer == current_question["answer"]:
        result_label.config(text="Correct! You dealt 10 damage!", fg="green")
        enemy_health -= 10
    else:
        result_label.config(text="Wrong! You lost 5 health!", fg="red")
        player_health -= 5

    update_health()
    next_question()

# Function to update health bars
def update_health():
    player_health_label.config(text=f"Player Health: {player_health}")
    enemy_health_label.config(text=f"Enemy Health: {enemy_health}")

    if player_health <= 0:
        result_label.config(text="Game Over! You lost!", fg="red")
        submit_button.config(state="disabled")
    elif enemy_health <= 0:
        result_label.config(text="Congratulations! You won!", fg="green")
        submit_button.config(state="disabled")

# Function to load a new question
def next_question():
    global current_question
    current_question = random.choice(questions)
    question_label.config(text=current_question["question"])
    answer_entry.delete(0, tk.END)

# UI Setup
root = tk.Tk()
root.title("Battle of Logic")

question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=10)

answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit Answer", font=("Arial", 14), command=check_answer)
submit_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

player_health_label = tk.Label(root, text=f"Player Health: {player_health}", font=("Arial", 14))
player_health_label.pack()

enemy_health_label = tk.Label(root, text=f"Enemy Health: {enemy_health}", font=("Arial", 14))
enemy_health_label.pack()

next_question()  # Start the game with a question

root.mainloop()