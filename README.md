# Word Search Game

A fun and interactive word search game built with Python! This project features a graphical user interface (GUI) using `tkinter` and robust backend logic to provide an engaging experience. Players take turns guessing words on a dynamically loaded board, with scores and progress tracked in real-time.

## Features

- **Customizable Game**: Load custom word lists and boards to create unique puzzles every time.
- **Interactive GUI**: User-friendly interface for players to take turns guessing words.
- **Dynamic Scoring**: Points awarded based on word length.
- **Visual Feedback**: Words found are crossed out on the board for better gameplay experience.
- **Multiplayer**: Add multiple players and track their scores throughout the game.
- **End-Game Summary**: Announces the winner and displays scores when all words are found.

## How to Play

1. **Load Word List**: Use the "Load Words List" button to upload a `.txt` file with words.
2. **Load Board**: Use the "Load Board File" button to upload a `.txt` file with the board layout.
3. **Add Players**: Add player names and start the game.
4. **Guess Words**: Players take turns entering their guesses.
5. **Score Points**: Correct guesses earn points based on word length.
6. **Win the Game**: The player with the highest score when all words are found wins!

## Setup

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd word-search-game
2. Run the game:
   ```bash
   python word_search_gui.py

### File Structure
- `word_search_logic.py`: Contains the core logic for word validation, board parsing, and scoring.
- `word_search_gui.py`: Implements the graphical user interface for the game.
- `assets/`: Directory for sample word and board files.

### Word and Board File Formats
- Word File: A plain text file (`.txt`) with one word per line, all in uppercase letters.
Board File: A plain text file (`.txt`) representing a grid, where each line corresponds to a row of characters.

#### Example Word File
  ```css
  ANT
  BOX
  SOB
  TO
  ```
#### Example Board File
  ```
  ANTT
  XSOB
  ```
### Scoring System
- Words shorter than 3 characters: 0 points
- Words 3–6 characters: 1 point per character
- Words 7–9 characters: 2 points per character
- Words 10+ characters: 3 points per character
### Screenshots
#### Main Screen
#### Gameplay

### Contributions
Contributions are welcome! If you'd like to contribute, please:
1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request for review.
   
### License
This project is licensed under the [MIT License]().

Enjoy playing the Word Search Game! 🎉
```vbnet

This README provides clear instructions, feature highlights, and helpful details to get started with the project. Would you like help generating example word and board files?
``
