 ATM Withdrawal Simulation
This Python script simulates a simple ATM withdrawal session, complete with input validation and user interaction.

📋 Description
The script allows a user to:

Enter their name to begin a withdrawal session.

Input a withdrawal amount.

Get real-time feedback and updated account balance.

Exit the session gracefully.

It includes multiple validations to ensure input correctness, such as:

Rejecting non-numeric inputs.

Disallowing withdrawals of negative values.

Ensuring the amount is a multiple of 100 (as with most ATMs).

Preventing withdrawals that exceed the current balance.

 Features
Continuous prompt until user exits.

Real-time balance updates after each valid withdrawal.

Error handling for invalid input types.

Clear, user-friendly messages for input guidance.

How It Works
The function simulate_withdrawal(balance) takes an initial balance.

The user is prompted to enter their name or type 0 to exit.

The user is repeatedly asked for a withdrawal amount until they:

Enter 0 (exits the session).

Enter an invalid amount (error shown, retry allowed).

Enter a valid amount (balance updates).

When the session ends, the final balance is returned and printed.
