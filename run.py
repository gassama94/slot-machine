import os
import random
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_colored_bold(text, color_code):
    bold_code = "\033[1m"  # ANSI escape code for bold text
    reset_code = "\033[0m"  # ANSI escape code to reset formatting
    print(f"{bold_code}{color_code}{text}{reset_code}")


WELCOME_MESSAGE = (
    Fore.BLUE
    + " | 🎰 Welcome to the Slot Machine Game! 🎰 |\n"
    + Style.RESET_ALL
)


GAME_EXPLAINATION = (
    "This is a simple game where you can bet on 1 to 3 lines.\n"
    "Win by getting identical symbols across a line.\n"
    "If you get any line, we are going to multiply your bet\n"
    "with the value of the line and add it to your balance."

)
print_colored_bold(WELCOME_MESSAGE, Fore.YELLOW)
print(GAME_EXPLAINATION)
print()
print_colored_bold("Enjoy the thrill of spinning!", Fore.YELLOW)

input("Press Enter to start the game...")
clear_screen()


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
        rows (int): Number of rows in the slot machine grid.
        cols (int): Number of columns in the slot machine grid.
        symbols (dict): Dictionary of symbols and their counts.

    Returns:
        columns (list): List of lists representing the slot machine columns.
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
            try:
                value = random.choice(current_symbols)
                # Ensure unique symbols
                current_symbols.remove(value)
                column.append(value)
            except IndexError:
                print("Error: Not enough unique symbols available.")
                return None

        # Add column to columns list
        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Print the current state of the slot machine.

    Args:
        columns (list): List of lists representing the slot machine columns.
    """
    try:
        # Iterate through each row
        for row in range(len(columns[0])):
            # Print symbols for each column in the row
            for i, column in enumerate(columns):
                end_character = " | " if i != len(columns) - 1 else ""
                symbol = column[row]
                if symbol == "A":
                    colored_symbol = Fore.RED + symbol
                elif symbol == "B":
                    colored_symbol = Fore.GREEN + symbol
                elif symbol == "C":
                    colored_symbol = Fore.BLUE + symbol
                elif symbol == "D":
                    colored_symbol = Fore.YELLOW + symbol
                else:
                    colored_symbol = symbol
                print(colored_symbol, end=end_character)

            # Print a newline after each row
            print(Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Error printing the slot machine:" + Style.RESET_ALL)


def deposit():
    """
    Prompt the player to deposit money.

    Returns an integer of the deposited amount by the player.
    """
    while True:
        amount = input(
            Fore.YELLOW + "What would you like to deposit? $\n"
            + Style.RESET_ALL)
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(
                    Fore.RED +
                    "Amount must be greater than 0."
                    + Style.RESET_ALL)
        else:
            print(Fore.RED + "Please enter a number!" + Style.RESET_ALL)

    return amount


def get_number_of_lines():
    """
    Prompt the user to input the number of lines they want to bet on.

    Returns:
        lines (int): The number of lines the user wants to bet on.
    """
    while True:
        print_colored_bold(
                f"Enter the number of lines to bet on (1-{MAX_LINES})?",
                Fore.YELLOW)
        lines = input()
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print_colored_bold(
                    "Enter a valid number of lines.", Fore.RED)
        else:
            print_colored_bold("Please enter a number.", Fore.RED)

    return lines


def get_bet():
    """
    Prompt the user to input the bet amount for each line.

    Returns:
        bet (int): The bet amount for each line.
    """
    while True:
        print_colored_bold(
                "What would you like to bet on each line? $",
                Fore.YELLOW)
        amount = input()
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print_colored_bold(
                    f"Amount must be ${MIN_BET} - ${MAX_BET}.", Fore.RED)
        else:
            print_colored_bold("Please enter a number!", Fore.RED)

    return amount


def spin(balance):
    """
    Play a round of the slot machine game.

    This function allows the player to place a bet and spin the slot machine.
    It calculates the total winnings, checks for winning combinations, and
    updates the player's balance accordingly.

    Args:
        balance (int): The current balance of the player.

    Returns:
        net_winnings (int): The net result of the game (winnings - total bet).
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficent funds, your current balance is: ${balance}")
        else:
            break

    print(f"Betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    """
    The main function to run the slot machine game.
    """
    balance = deposit()
    while True:
        print_colored_bold(f"Current balance is ${balance}", Fore.YELLOW)
        answer = input("Press anything to spin. (q to quit)\n")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()
