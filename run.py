import random
print("Welcome to the Slot Machine Game!")


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3


symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
    Calculate the winnings and winning lines in the slot machine.
    based on the provided columns.

    function checks for winning combinations on each line of the slot machine.
    A winning combination consists of identical symbols.
    Across all columns on a single line.

    Args:
        columns (list): List of lists representing the slot machine columns.
        lines (int): Number of lines bet on.
        bet (int): Bet amount per line.
        values (dict): Dictionary containing symbol values.

    Returns:
        winnings (int): Total winnings from winning combinations.
        winning_lines (list): List of line numbers with winning combinations.
    """
    winnings = 0
    winning_lines = []
    # Iterate through each line
    for line in range(lines):
        symbol = columns[0][line]   
        # Check if all symbols on the same line are identical
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random spin result for the slot machine.

    Args:
    - rows (int): Number of rows in the slot machine grid.
    - cols (int): Number of columns in the slot machine grid.
    - symbols (dict): Dictionary of symbols and their counts.

    Returns:
    - columns (list): List of lists representing the slot machine columns.
    """
    all_symbols = []
    # Populate all_symbols with symbols based on their counts
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    # Generate column data for each column
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        # Generate row data for each row in the column
        for _ in range(rows):
            value = random.choice(current_symbols)
            # Ensure unique symbols
            current_symbols.remove(value) 
            column.append(value)

        # Add column to columns list
        columns.append(column) 

    return columns


def print_slot_machine(columns):
    """
    Print the current state of the slot machine.

    Args:
    - columns (list): List of lists representing the slot machine columns.
    """
    # Iterate through each row
    for row in range(len(columns[0])):
        # Print symbols for each column in the row
        for i, column in enumerate(columns):
            end_character = " | " if i != len(columns) - 1 else ""
            print(column[row], end=end_character)           
        # Print a newline after each row
        print()  


def deposit():
    """
    Prompt the player to deposit money.

    Returns an integer of the deposited amount by the player.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number!")

    return amount


def get_number_of_lines():
    """
    Prompt the user to input the number of lines they want to bet on.

    Returns:
    - lines (int): The number of lines the user wants to bet on.
    """
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1-{MAX_LINES} )? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    """
    Prompt the user to input the bet amount for each line.

    Returns:
    - bet (int): The bet amount for each line.
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number!")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Not have enough balance, your current balance is: ${balance}  ")
        else: 
            break    

    print(f"Betting €{bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    """
    The main function to run the slot machine game.
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin. (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
