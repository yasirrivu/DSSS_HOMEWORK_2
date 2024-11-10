import random


def Random_Int(min, max):
    """Returns a random integer between min and max.
    Args:
        min (int): The minimuum value of the range.
        max (int): The maximum value of the range.
    
    Returns:
        int: A random integer between min and max.
    Example:
        >>> Random_Int(1,10)
        7
        >>> Random_Int(5,9)
        6

    """
    
    return random.randint(min, max)


def Random_Operator():
    """Returns a random operator from +, - or *.
    
    Returns:
        str: A random operator from +, - or *.
    
    Example:
        >>> Random_Operator()
        '+'
        >>> Random_Operator()
        *

    """
    return random.choice(['+', '-', '*'])


def Perform_Operation(int1, int2, operator):
    """Performs arithmatic operations and returns problem statements and answers.
    Args:
        int1 (int): 1st integer operand.
        int2 (int): 2nd integer operand.
        operator (str): Arithmatic operator. One of (+, -, *).

    Returns:
        tuple: A tuple containing:
            -str: The problem statement.
            -int: The calculated answer.
    
    Example:
        >>> Perform_Operation(5, 3, '+')
        ('5 + 3', 8)
        >>> Perform_Operation(8, 6, '-')
        ('8 - 6', 2

    """
    #generate the problem statement
    problem = f"{int1} {operator} {int2}"
    #calculates the answer
    if operator == '+': answer = int1 + int2
    elif operator == '-': answer = int1 - int2
    else: answer = int1 * int2
    #returns problem statement and answer
    return problem, answer


def math_quiz():
    """Runs an interactive math quiz game with random arithmetic problems.

   The game presents the user with 3 arithmetic problems, each containing:
   - Two random integers (first number: 1-10, second number: 1-5)
   - A random operator (+, -, or *)
   The user must input the correct answer to earn points.

   Returns:
       None

   Game Flow:
       1. Displays welcome message
       2. For each question:
           - Generates random numbers and operator
           - Shows the problem
           - Takes user input (validates for integer)
           - Checks answer and updates score
       3. Shows final score

   Example:
       >>> math_quiz()
       Welcome to the Math Quiz Game!
       You will be presented with math problems, and you need to provide the correct answers.

       Question: 7 * 3
       Your answer: 21
       Correct! You earned a point.

       Game over! Your score is: 1/3
   """
    
    score = 0
    counter = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
   
    for n in range(counter):
        #pick a random interger number from 1 to 10
        int1 = Random_Int(1, 10)
        #pick a random interger number from 1 to 10
        int2 = Random_Int(1, 5)
        #pick a random operator from ('+', '-', '*')
        operator = Random_Operator()

        PROBLEM, ANSWER = Perform_Operation(int1, int2, operator)
        print(f"\nQuestion: {PROBLEM}")

        #try-except to catch invalid user input
        while True:
            try:
                useranswer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        #Checks if user's answer is correct
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{counter}")

if __name__ == "__main__":
    math_quiz()
