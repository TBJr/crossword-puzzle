import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import word_search_logic


class WordSearchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Search Game")

        # Initialize variables
        self.words = []
        self.board = []
        self.found_words = []
        self.players = []
        self.player_index = 0
        self.time_remaining = tk.IntVar(value=30)  # Default timer value
        self.difficulty = tk.StringVar(value="Medium")  # Default difficulty level

        # Game state variables
        self.remaining_words = tk.StringVar()
        self.current_player = tk.StringVar()
        self.guess_word = tk.StringVar()

        # Create GUI layout
        self.create_widgets()

    def create_widgets(self):
        # Difficulty selection
        tk.Label(self.root, text="Select Difficulty:").grid(row=0, column=0, padx=10, pady=10)
        difficulty_menu = tk.OptionMenu(self.root, self.difficulty, "Easy", "Medium", "Hard")
        difficulty_menu.grid(row=0, column=1, padx=10, pady=10)

        # File selection buttons
        tk.Button(self.root, text="Load Words List", command=self.load_words_file).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Load Board File", command=self.load_board_file).grid(row=1, column=1, padx=10, pady=10)

        # Players input
        tk.Button(self.root, text="Add Players", command=self.add_players).grid(row=1, column=2, padx=10, pady=10)

        # Display board
        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Timer display
        tk.Label(self.root, text="Time Remaining:").grid(row=3, column=0, pady=10)
        tk.Label(self.root, textvariable=self.time_remaining).grid(row=3, column=1, pady=10)

        # Word guess input
        tk.Label(self.root, text="Enter your guess:").grid(row=4, column=0, pady=10)
        tk.Entry(self.root, textvariable=self.guess_word).grid(row=4, column=1, pady=10)
        tk.Button(self.root, text="Submit Guess", command=self.submit_guess).grid(row=4, column=2, pady=10)

        # Player info and score
        self.info_frame = tk.Frame(self.root)
        self.info_frame.grid(row=5, column=0, columnspan=3, pady=10)

        tk.Label(self.info_frame, text="Current Player:").grid(row=0, column=0)
        tk.Label(self.info_frame, textvariable=self.current_player).grid(row=0, column=1)

        tk.Label(self.info_frame, text="Words Remaining:").grid(row=1, column=0)
        tk.Label(self.info_frame, textvariable=self.remaining_words).grid(row=1, column=1)

        # Found words
        tk.Label(self.root, text="Found Words:").grid(row=6, column=0, pady=10)
        self.found_words_text = tk.Text(self.root, height=10, width=50, state=tk.DISABLED)
        self.found_words_text.grid(row=6, column=1, columnspan=2)

    def load_words_file(self):
        file_path = filedialog.askopenfilename(title="Select Words List File")
        if file_path:
            with open(file_path, 'r') as words_file:
                self.words = word_search_logic.read_words(words_file)
            messagebox.showinfo("Words List Loaded", "Successfully loaded the words list!")

    def load_board_file(self):
        file_path = filedialog.askopenfilename(title="Select Board File")
        if file_path:
            with open(file_path, 'r') as board_file:
                self.board = word_search_logic.read_board(board_file)
            self.adjust_board_to_difficulty()
            self.display_board()
            messagebox.showinfo("Board Loaded", "Successfully loaded the board!")

    def adjust_board_to_difficulty(self):
        """Adjust the board size and word list based on the selected difficulty."""
        difficulty = self.difficulty.get()
        if difficulty == "Easy":
            self.time_remaining.set(45)  # Easy: Longer timer
            self.words = [word for word in self.words if len(word) >= 5]
        elif difficulty == "Medium":
            self.time_remaining.set(30)  # Medium: Standard timer
            self.words = [word for word in self.words if 4 <= len(word) <= 6]
        elif difficulty == "Hard":
            self.time_remaining.set(15)  # Hard: Short timer
            self.words = [word for word in self.words if len(word) <= 5]

    def display_board(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        # Create a 2D representation of found letters
        crossed_out = [[False] * len(row) for row in self.board]

        # Mark letters in found words as crossed out
        for word in self.found_words:
            for row_idx, row in enumerate(self.board):
                row_str = ''.join(row)
                if word in row_str:
                    start_idx = row_str.index(word)
                    for i in range(len(word)):
                        crossed_out[row_idx][start_idx + i] = True
                for col_idx in range(len(self.board[0])):
                    col_str = ''.join(row[col_idx] for row in self.board if col_idx < len(row))
                    if word in col_str:
                        start_idx = col_str.index(word)
                        for i in range(len(word)):
                            crossed_out[start_idx + i][col_idx] = True

        # Render the board with crossed-out letters for found words
        for row_idx, row in enumerate(self.board):
            for col_idx, char in enumerate(row):
                if crossed_out[row_idx][col_idx]:
                    label = tk.Label(
                        self.board_frame,
                        text=char,
                        width=3,
                        height=2,
                        relief="solid",
                        fg="gray"  # Change text color to indicate strikethrough
                    )
                    label.grid(row=row_idx, column=col_idx)
                else:
                    label = tk.Label(self.board_frame, text=char, width=3, height=2, relief="solid")
                    label.grid(row=row_idx, column=col_idx)

    def add_players(self):
        num_players = tk.simpledialog.askinteger("Add Players", "Enter number of players:")
        if num_players:
            for i in range(num_players):
                player_name = tk.simpledialog.askstring("Player Name", f"Enter name for player {i + 1}:")
                if player_name:
                    self.players.append([player_name, 0])
            self.start_game()

    def start_game(self):
        if not self.board or not self.words:
            messagebox.showerror("Error", "Please load the board and words list first.")
            return

        self.found_words = []
        self.remaining_words.set(len(self.words))
        self.update_current_player()
        self.start_timer()
        messagebox.showinfo("Game Started", "Game has started! Players take turns guessing words.")

    def start_timer(self):
        """Start the timer for the current player's turn."""
        if self.time_remaining.get() > 0:
            self.time_remaining.set(self.time_remaining.get() - 1)
            self.root.after(1000, self.start_timer)
        else:
            messagebox.showinfo("Time's Up!", f"{self.current_player.get()}'s turn is over!")
            self.next_turn()

    def next_turn(self):
        """Switch to the next player's turn."""
        self.player_index = (self.player_index + 1) % len(self.players)
        self.update_current_player()
        self.time_remaining.set(30)  # Reset timer
        self.start_timer()
        
    def update_current_player(self):
        if self.players:
            self.current_player.set(self.players[self.player_index][0])

    def submit_guess(self):
        guess = self.guess_word.get().strip().upper()
        if not guess:
            return

        if guess in self.found_words:
            messagebox.showinfo("Already Found", f"The word '{guess}' has already been found!")
        elif word_search_logic.is_valid_word(self.words, guess) and word_search_logic.board_contains_word(self.board, guess):
            messagebox.showinfo("Correct Guess", f"The word '{guess}' is correct!")
            self.found_words.append(guess)

            # Update the found words text widget with strikethrough
            self.found_words_text.config(state=tk.NORMAL)
            self.found_words_text.insert(tk.END, f"{guess}\n")
            self.found_words_text.tag_add(guess, "end-2l", "end-1c")
            self.found_words_text.tag_config(guess, overstrike=True)
            self.found_words_text.config(state=tk.DISABLED)

            # Refresh the board to reflect found words
            self.display_board()

            word_search_logic.update_score(self.players[self.player_index], guess)
        else:
            messagebox.showinfo("Incorrect Guess", f"The word '{guess}' is not valid or not on the board.")

        self.guess_word.set("")
        self.remaining_words.set(len(self.words) - len(self.found_words))
        if len(self.found_words) == len(self.words):
            self.end_game()
        else:
            self.player_index = (self.player_index + 1) % len(self.players)
            self.update_current_player()

    def end_game(self):
        winner = max(self.players, key=lambda p: p[1])
        messagebox.showinfo("Game Over", f"Game over! The winner is {winner[0]} with {winner[1]} points!")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = WordSearchGame(root)
    root.mainloop()