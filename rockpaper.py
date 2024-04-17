import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    
    result_label.config(text=f"Your choice: {user_choice} \n Computer choice: {computer_choice}\n{result}" ,foreground="red",font=("Cambria", 18, "bold"))
    
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    score.config(text=f"Your score: {user_score}\nComputer's score: {computer_score}",font=("Cambria",18,"bold"))

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score.config(text="Your score: 0\nComputer's score: 0",font=("Cambria",18,"bold"))

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock Paper Scissors")

label1=tk.Label(root, text="Rock! Paper! Scissors!", fg="blue", font=("Segoe Script", 25, "bold"))
label1.pack()
instruction_label = tk.Label(root, text="Choose one: rock, paper, or scissors", fg="darkblue", font=("Georgia",18,"bold"))
instruction_label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

choices = ['rock', 'paper', 'scissors']
for choice in choices:
    button = tk.Button(button_frame, text=choice, width=12, command=lambda c=choice: play_game(c), height=1, fg="black",bg="coral",font=("Cambria",15,"bold"))
    button.pack(side=tk.LEFT, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

score = tk.Label(root, text="Your score: 0\nComputer's score: 0", fg="darkorchid4", font=("Cambria", 18, "bold"))
score.pack()

reset = tk.Button(root, text="Reset Scores", command=reset_scores,fg="black",bg="coral", width=12,font=("Cambria",15,"bold"))
reset.pack()

quit_button = tk.Button(root, text="Quit", command=root.destroy,fg="black",bg="coral", width=12,font=("Cambria",15,"bold"))
quit_button.pack(side="bottom",pady=10)

root.mainloop()
