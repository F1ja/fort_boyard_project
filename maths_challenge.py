import random
from random import randint

# Global variables for the equation challenge
a = 0
b = 0
s = 0

def solve_linear_equation():
    """
    Generates a random linear equation in the form ax + b = 0.
    Returns the values of a, b, and the solution s.
    """
    global a, b, s
    a = randint(1, 10)
    b = randint(1, 10)
    s = -b / a
    return a, b, s

def math_challenge_equation():
    """
    Math challenge: Solve a randomly generated linear equation of the form ax + b = 0.
    Prompts the user to enter the solution rounded to 2 decimal places.
    """
    solve_linear_equation()
    print(f"Maths challenge: Solve the equation {a}x + {b} = 0")
    s_given = float(input("Enter the value of x (rounded to 10^-2 ex: if answer is 2.956, enter 2.96): "))
    if s_given == round(s, 2):
        print("Correct! You win a key.")
        return True
    else:
        print("Incorrect! You don't win a key.")
        return False

def is_prime(n):
    """
    Checks whether a given number n is prime.
    Returns True if n is prime, False otherwise.
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    """
    Finds the nearest prime number greater than or equal to n.
    Returns the nearest prime.
    """
    while not is_prime(n):
        n += 1
    return n

def math_challenge_prime():
    """
    Math challenge: Find the nearest prime number greater than or equal to a random number (10 to 20).
    Prompts the user to enter their guess.
    """
    n = randint(10, 20)
    print(f"Maths challenge: Find the nearest prime number to {n} (greater or equal to n)")
    n_guess = int(input("Enter your answer: "))
    if n_guess == nearest_prime(n):
        print("Correct! You win a key.")
        return True
    else:
        print(f"Wrong! The correct answer was {nearest_prime(n)}.")
        return False

def math_roulette_challenge():
    """
    Math challenge: Solve a random operation (addition, subtraction, multiplication)
    on a set of randomly generated numbers.
    Prompts the user to calculate the result based on the chosen operation.
    """
    k = randint(1, 20)
    l = randint(1, 20)
    m = randint(1, 20)
    p = randint(1, 20)
    o = randint(1, 20)
    print(f"Numbers on the roulette: [ {k}, {l}, {m}, {p}, {o} ]")
    operations = ["+", "-", "*"]
    chosen_operation = random.choice(operations)

    if chosen_operation == "+":
        print("Calculate the result by combining these numbers with addition")
        n_result = k + l + m + p + o
        n_guess = int(input("Your answer: "))
        if n_guess == n_result:
            print("Correct! You've won a key.")
            return True
        else:
            print("Incorrect! You don't win a key.")
            return False
    elif chosen_operation == "-":
        print("Calculate the result by combining these numbers with subtraction")
        n_result = k - l - m - p - o
        n_guess = int(input("Your answer: "))
        if n_guess == n_result:
            print("Correct! You've won a key.")
            return True
        else:
            print("Incorrect! You don't win a key.")
            return False
    elif chosen_operation == "*":
        print("Calculate the result by combining these numbers with multiplication")
        n_result = k * l * m * p * o
        n_guess = int(input("Your answer: "))
        if n_guess == n_result:
            print("Correct! You've won a key.")
            return True
        else:
            print("Incorrect! You don't win a key.")
            return False

def math_challenge():
    """
    Randomly selects and executes one of the math challenges.
    Challenges include solving equations, finding primes, and performing arithmetic operations.
    """
    challenges = [
        math_roulette_challenge,
        math_challenge_equation,
        math_challenge_prime
    ]
    selected_challenge = random.choice(challenges)
    return selected_challenge()

# Start the math challenge
#math_challenge()