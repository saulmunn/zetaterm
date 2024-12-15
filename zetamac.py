import random
import time

def generate_problem():
    operations = ['+', '-', '*', '/']
    op = random.choice(operations)
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    expression = f"{a} {op} {b}"
    answer = eval(expression)
    return expression, answer

def run_test(duration=120):
    print("Welcome to the Zetamac-style mental math test!")
    print("You have", duration, "seconds to solve as many problems as possible.")
    print("Press Enter when you are ready to begin.")
    input()
    start_time = time.time()
    correct = 0
    attempts = 0

    while True:
        elapsed = time.time() - start_time
        if elapsed >= duration:
            break
        expression, answer = generate_problem()
        try:
            user_answer = input(f"{expression} = ")
            if time.time() - start_time > duration:  
                break
            if user_answer.strip().isdigit() or (user_answer.strip().startswith('-') and user_answer.strip()[1:].isdigit()):
                user_answer = int(user_answer.strip())
                if user_answer == answer:
                    correct += 1
            attempts += 1
        except KeyboardInterrupt:
            break

    print("Time's up!")
    print("You answered", correct, "correctly out of", attempts, "attempted.")

if __name__ == "__main__":
    run_test()