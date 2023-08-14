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
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Print the current state of the slot machine.

    Args:
    - columns (list): List of lists representing the slot machine columns.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            end_character = " | " if i != len(columns) - 1 else ""
            print(column[row], end=end_character)

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


def main():
    """
    The main function to run the slot machine game.
    """
    balance = deposit()
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
   

if __name__ == "__main__":
    main()
