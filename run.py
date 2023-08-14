

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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

    print(f"Betting €{bet} on {lines} lines. total bet is equal to: ${total_bet}")
   

if __name__ == "__main__":
    main()
