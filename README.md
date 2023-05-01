# Calculator Program

This program allows the user to perform basic arithmetic operations on two numbers. The user is prompted to enter two numbers, and then select an operation (addition, subtraction, multiplication, or division) to perform on the numbers.

## Usage

1. Run the program.
2. Enter the first number.
3. Enter the second number.
4. Select the operation to perform.
5. The program will output the result of the selected operation.

## Example

```shell
Welcome to My Calculator
Enter Your First Number: 10
Enter Your Second Number: 5
Select operation
1. Add
2. Multiply
3. Divide
4. Subtract
Enter Your Choice(1/2/3/4): 2
10 * 5 = 50
```

## Code Explanation

1. The program prompts the user to enter two numbers using the '**input()**' function and stores them in the '**num_1**' and '**num_2**' variables.
2. The program performs the four basic arithmetic operations on the numbers and stores the results in the '**add**', '**mul**', '**div**', and '**sub**' variables.
3. The program outputs a menu of operation choices using the '**print()**' function.
4. The program prompts the user to enter a choice using the '**input()**' function and stores it in the '**b**' variable.
5. The program uses conditional statements ('**if**', '**elif**', '**else**') to determine which operation to perform based on the user's choice, and outputs the result using the '**print()**' function.
6. If the user enters an invalid choice, the program outputs an error message using the '**print()**' function.