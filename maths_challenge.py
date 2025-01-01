import random

from random import randint

#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)

#def math_challenge_factorial():
#    n=randint(1,10)
#    print(f"Math Challenge: Calculate the factorial of {n}." )
    n_guess=int(input("Your answer:"))
#    if n_guess == factorial(n):
#        print("Correct! You win a key.")
#    else:
#        print(f"Wrong! The correct answer was {factorial(n)}.")
#math_challenge_factorial()
a=0
b=0
s=0
def solve_linear_equation():
    global a,b,s
    a=randint(1,10)
    b=randint(1,10)
    s=-b/a
    return a,b,s
#solve_linear_equation()

def math_challenge_equation():
    solve_linear_equation()
    print(f"Maths challenge: Solve the equation {a} x + {b}= 0")
    s_given=float(input("Enter the value of x (rounded to 10^-2) :"))
    if s_given==round(s,2):
        print("Correct! You win a key.")
    else:
        print("Incorrect! You don't win a key.")
#math_challenge_equation()
def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def nearest_prime(n):
    while not is_prime(n):
        n+=1
    return n
def math_challenge_prime():
    n=randint(10,20)
    print(f"Maths challenge: Find the nearest prime number to {n}")
    n_guess=int(input("Enter your answer:"))
    if n_guess==nearest_prime(n):
        print("Correct! You win a key.")
    else:
        print(f"Wrong! The correct answer was {nearest_prime(n)}.")
#math_challenge_prime()
k=0
l=0
m=0
p=0
o=0
def  math_roulette_challenge():
    global k,l,m,p,o
    k=randint(1,20)
    l=randint(1,20)
    m=randint(1,20)
    p=randint(1,20)
    o=randint(1,20)
    print(f"Numbers on the roulette :[ {k},{l},{m},{p},{o} ]")
    operations=["+","-","*"]
    chose=random.choice(operations)
    if chose=="+":
        print(f"Calculate the result by combining these numbers with addition")
        n_result=k+l+m+p+o
        n_guess=int(input("Your answer:"))
        if n_guess==n_result:
            print("Correct! You've won a key.")
        else:
            print("Incorrect! You don't win a key.")
    if chose=="-":
        print(f"Calculate the result by combining these numbers with subtraction")
        n_result=k-l-m-p-o
        n_guess=int(input("Your answer:"))
        if n_guess==n_result:
            print("Correct! You've won a key.")
        else:
            print("Incorrect! You don't win a key.")
    if chose=="*":
        print(f"Calculate the result by combining these numbers with multiplication")
        n_result=k*l*m*p*o
        n_guess=int(input("Your answer:"))
        if n_guess==n_result:
            print("Correct! You've won a key.")
        else:
            print("Incorrect! You don't win a key.")
def math_challenge():
    """Choose randomly a math challenge for the user."""
    challenges = [
        math_roulette_challenge,
        math_challenge_equation,
        math_challenge_prime,
        #math_challenge_factorial
    ]
    return random.choice(challenges)
math_challenge()