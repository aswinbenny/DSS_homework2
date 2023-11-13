import random

def random_integer(min, max):
    """
    generate a random integer
    """
    return random.randint(min, max)

def random_operation():
    """
    generate a random mathematical operation
    """
    return random.choice(['+', '-', '*'])

def operation(no_1, no_2, operator):
    """
    perform the mathematical operation based on operator
    """
    operation = f"{no_1} {operator} {no_2}"
    if operator == '+': answer = no_1 + no_2
    elif operator == '-': answer = no_1 - no_2
    else: answer = no_1 * no_2
    return operation, answer

def math_quiz():
    sum = 0
    no_of_operations = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(no_of_operations):
        no_1 = random_integer(1, 10); no_2 = random_integer(1, 5); operator = random_operation()
        PROBLEM, ANSWER = operation(no_1, no_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            sum = sum + 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {sum}/{no_of_operations}")

if __name__ == "__main__":
    math_quiz()

