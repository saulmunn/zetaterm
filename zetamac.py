import random
import time

def generate_problem():
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    if operation != '/':
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        expression = f"{a} {operation} {b}"
        answer = eval(expression)
        return expression, answer
    else:
        b = random.randint(1, 20)
        c = random.randint(1, 20)
        a = b*c
        expression = f"{a} / {b}"
        answer = eval(expression)
        return expression, answer

def set_settings():
    pass
    # add some settings
    #   - which operations you want to include
    #   - range of numbers
    #   - time duration

def run_test(duration=15):
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
            while True:
                user_answer = input(f"{expression} = ")
                if user_answer.strip().isdigit() or (user_answer.strip().startswith('-') and user_answer.strip()[1:].isdigit()):
                    user_answer = int(user_answer.strip())
                    if user_answer == answer:
                        correct += 1
                        print("[correct]\n")
                        break
                attempts += 1
        except KeyboardInterrupt:
            break
    ending_message(correct, attempts)

def start():
    print("\n\nWelcome to the Zetaterm: Zetamac in the terminal.")
    print("\nThe Arithmetic Game is a fast-paced speed drill where you're given limited amount of time to solve as many arithmetic problems as you can.")
    print("\n\nPress Enter when you're ready to begin.")
    run_test()

def ending_message(correct, attempts):
    print("Time's up!")
    print("You answered", correct, "correctly out of", attempts, "attempted.")
    input("\nPress Enter when you're ready to play again.")
    run_test()



if __name__ == "__main__":
    start()