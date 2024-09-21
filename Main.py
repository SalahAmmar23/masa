from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap("")

# Variables
count = 0
turn = True  # True for X's turn, False for O's turn
player_x_score = 0
player_o_score = 0

# Score label
score_label = Label(root, text=f"Player X: {player_x_score}  Player O: {player_o_score}")
score_label.grid(row=3, column=0, columnspan=3)

# Disable all buttons
def disable_all_buttons():
    for b in buttons:
        b.config(state=DISABLED)

# Enable all buttons
def enable_all_buttons():
    for b in buttons:
        b.config(state=NORMAL)

# Check if someone won
def check_if_won():
    winning_combinations = [
        [b1, b2, b3], [b4, b5, b6], [b7, b8, b9],  # rows
        [b1, b4, b7], [b2, b5, b8], [b3, b6, b9],  # columns
        [b1, b5, b9], [b3, b5, b7]  # diagonals
    ]
    for combination in winning_combinations:
        if all(b["text"] == "X" for b in combination):
            for b in combination:
                b.config(bg="light blue")
            messagebox.showinfo("Tic Tac Toe", "Congratulations! Player X wins")
            disable_all_buttons()
            root.after(1000, reset)  # Auto-reset after 2 seconds
            return True
        elif all(b["text"] == "O" for b in combination):
            for b in combination:
                b.config(bg="light green")
            messagebox.showinfo("Tic Tac Toe", "Congratulations! Player O wins")
            disable_all_buttons()
            root.after(1000, reset)  # Auto-reset after 2 seconds
            return True
    return False

# Button clicked function
def b_click(b):
    global turn, count, player_x_score, player_o_score

    if b["text"] == " ":
        if turn:  # X's turn
            b["text"] = "X"
            turn = False
            count += 1
            if check_if_won():
                player_x_score += 1
                score_label.config(text=f"Player X: {player_x_score}  Player O: {player_o_score}")
        else:  # O's turn
            b["text"] = "O"
            turn = True
            count += 1
            if check_if_won():
                player_o_score += 1
                score_label.config(text=f"Player X: {player_x_score}  Player O: {player_o_score}")

        if count == 9 and not check_if_won():
            messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
            disable_all_buttons()
            root.after(1000, reset)  # Auto-reset after 2 seconds

# Start the game
def reset():
    global buttons, b1, b2, b3, b4, b5, b6, b7, b8, b9
    global count, turn
    count = 0
    turn = True  # X starts

    # Create buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # Grid buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    score_label.config(text=f"Player X: {player_x_score}  Player O: {player_o_score}")
    enable_all_buttons()  # Enable buttons when resetting

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()
