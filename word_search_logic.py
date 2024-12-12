"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool
    Return True if and only if word is an element of wordlist.
    """
    return word in wordlist


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str
    Return the characters from the row of the board with index row_index as a single string.
    """
    return ''.join(board[row_index])


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str
    Return the characters from the column of the board with index column_index as a single string.
    """
    if column_index < 0 or column_index >= len(board[0]):
        raise IndexError("Invalid column index")
    return ''.join(row[column_index] for row in board if column_index < len(row))


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool
    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.
    """
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.
    """
    max_columns = max(len(row) for row in board)
    for col_index in range(max_columns):
        column_str = ''.join(row[col_index] for row in board if col_index < len(row))
        if word in column_str:
            return True
    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.
    """
    if not board or not board[0]:  # Empty board or no columns
        return False
    return board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word)


def word_score(word):
    """ (str) -> int
    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word
    """
    if not word.isalpha():
        raise ValueError("Invalid word: contains non-alphabetic characters")
    if len(word) < 3:
        return 0
    elif 3 <= len(word) <= 6:
        return len(word)
    elif 7 <= len(word) <= 9:
        return 2 * len(word)
    else:
        return 3 * len(word)


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.
    """
    player_info[1] += word_score(word)

def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.
    """
    return sum(1 for word in words if board_contains_word(board, word))



def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    return [line.strip() for line in words_file]

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    board = []
    for line in board_file:
        stripped_line = line.strip()
        if not stripped_line.isalpha():
            raise ValueError("Invalid board file: Non-alphabetic characters found")
        board.append(list(stripped_line))
    return board