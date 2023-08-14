![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Saikou Gassama,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!



# Slot Machine Game

Welcome to the Slot Machine Game! This is a simple text-based game where players can bet on lines and try their luck at the slot machine. Have fun exploring the features of the Slot Machine Game and enjoy the thrill of spinning the virtual reels! 

Here is live version of my project![]
## How to Play

1. **Deposit Money:**
   - When you start the game, you'll be prompted to deposit an amount of money.
   - Enter a positive integer greater than 0 to deposit funds into your balance.

2. **Place Your Bets:**
   - You'll be asked to choose the number of lines you want to bet on.
   - Enter a number between 1 and 3 to select the number of lines.

3. **Bet Amount:**
   - Enter the amount you want to bet on each line.
   - The bet amount must be between $1 and $100.

4. **Spin the Slot Machine:**
   - After placing your bets, the game will simulate a spin of the slot machine.
   - The results of the spin will be displayed, showing the symbols on each line.

5. **Check Winnings:**
   - The game will calculate your winnings based on the symbols' combinations.
   - If you win, the amount you win will be added to your balance.

6. **Repeat or Quit:**
   - You can choose to continue playing or quit the game.
   - Press Enter to spin again, or type "q" to quit.

7. **Ending the Game:**
   - When you're done playing, you can exit the game by typing "q" when prompted to spin.


## Features

- **Realistic Slot Machine Simulation:** Experience the excitement of a classic slot machine game with a realistic simulation of spinning reels and symbol combinations.

- **Dynamic Betting:** Choose the number of lines you want to bet on and the amount you want to bet per line, allowing for customizable gameplay.

- **Symbol Combinations:** The game checks for winning combinations across all columns on a single line, and calculates your winnings based on symbol values.

- **Interactive Interface:** The game provides an interactive interface with clear prompts and instructions for each step, making it easy for players to participate.

- **Balance Management:** Players start with a balance and can continue playing until they decide to quit or their balance runs out.

- **User-Friendly:** The game is designed to be user-friendly, guiding players through the steps of placing bets, spinning the slot machine, and checking their winnings.

...

## Data Model

The Slot Machine Game utilizes the following data structures and functions:

### `symbol_count` and `symbol_value`

These dictionaries define the symbols used in the game and their associated counts and values. These values play a crucial role in determining winnings based on symbol combinations.

### `get_slot_machine_spin`

This function generates a random spin result for the slot machine. It accepts the number of rows, columns, and symbols as inputs and returns a list of lists representing the slot machine columns.

### `check_winnings`

The `check_winnings` function calculates the winnings and identifies winning lines in the slot machine based on the provided columns. It evaluates each line for winning combinations consisting of identical symbols across all columns.

### `print_slot_machine`

This function prints the current state of the slot machine columns. It takes a list of lists representing the slot machine columns as input and displays the symbols row by row, column by column.

### `deposit`, `get_number_of_lines`, and `get_bet`

These functions are responsible for gathering player input regarding deposit amount, number of lines to bet on, and bet amount per line, respectively. They ensure valid input from the player and return the appropriate values.

### `spin`

The `spin` function simulates a round of the game. It prompts the player to place a bet, evaluates if the bet is within the available balance, and then generates a spin result. It calculates winnings, displays the outcome, and updates the player's balance.

### `main`

The `main` function orchestrates the overall flow of the game. It handles player interaction, balance management, and repetitive gameplay until the player decides to quit.

...

## Testing

The Slot Machine Game has undergone testing to ensure its functionality and reliability. The following testing strategies were employed:

### Unit Testing

Unit tests were conducted for individual functions within the game to verify that they produce the expected outputs given various inputs. For instance, the `check_winnings` function was tested with different column configurations to validate its ability to identify winning combinations accurately.

### Integration Testing

Integration tests were performed to verify the interaction between different game components. This included testing how the `spin` function interacts with the `get_slot_machine_spin`, `check_winnings`, and other supporting functions. The objective was to ensure seamless coordination between different game mechanics.

### Player Experience Testing

User testing was conducted to evaluate the overall player experience. A diverse group of friends played the game, providing feedback on user interface clarity, ease of use, and overall enjoyment. This feedback was instrumental in refining the user interaction aspects of the game.

### Error Handling and Edge Cases

Extensive testing was conducted to identify and address potential errors, edge cases, and exceptional scenarios. This involved testing for cases such as insufficient balance for a bet, input validation for numeric values, and handling unexpected input gracefully.

### Manual Playtesting

The game was manually playtested by friends and family to simulate real player interactions. This allowed us to identify any potential bugs, discrepancies in winnings calculation, or unexpected behavior during gameplay.


...

## Bugs and Known Issues

Throughout the development and testing process, we have identified and resolved several bugs and known issues in the Slot Machine Game. Below is a list of these issues along with their current status:

### Bug 1: Insufficient Balance Check

**Description:** There was a bug in the `spin` function where the game did not handle insufficient balance correctly. Players could place bets even if their balance was lower than the total bet amount.

**Status:** Resolved in version 1.1. Players are now prevented from placing bets that exceed their available balance.

### Bug 2: Trailing Whitespace

**Description:** The code contained trailing whitespace in some lines, leading to formatting inconsistencies.

**Status:** Resolved in version 1.2. Trailing whitespace has been removed from relevant lines.

### Bug 3: Input Validation

**Description:** The input validation for bet amounts did not handle non-numeric input gracefully, leading to unexpected behavior.

**Status:** Resolved in version 1.2. Improved input validation now prompts users to enter valid numeric values.

### Known Issue: Winning Lines Display

**Description:** In some cases, the display of winning line numbers in the output does not align properly with the game grid.

**Status:** Under investigation. This issue is being actively addressed and will be resolved in an upcoming release.

### Known Issue: Edge Case Testing

**Description:** Some rare edge cases involving specific symbol configurations have not been fully tested for accuracy.

**Status:** Ongoing. Additional testing is being conducted to identify and address any potential edge cases.

We are committed to continually improving the Slot Machine Game and addressing any bugs or issues that arise. If you encounter any problems while playing, please report them to us so we can take the necessary steps to resolve them.

[Rest of the README content]

...


## Prerequisites and Deployment

[... List of prerequisites and deployment steps ...]

...

[Rest of the README content]

...

Enjoy the Slot Machine Game and experience the excitement of playing the virtual slot machine!




## Prerequisites

- You need a Heroku account. If you don't have one, you can sign up at [Heroku](https://www.heroku.com/).
- Install the Gitpod extension for Heroku. This will help streamline the deployment process within Gitpod.

...

[Rest of the README content]

...

Have fun playing the Slot Machine Game and best of luck with your deployment on Heroku using Gitpod!
