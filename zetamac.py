import random
import time

game_duration = 120


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


def set_settings(): # the "settings" menubar
        
    #function that lets the user set the duration of each game
    def set_duration():
        global game_duration
        desired_duration = int(input("\nHow long do you want the game to last? Type your answer in seconds, then hit Enter: ").strip())
        print(f"Games will now last {desired_duration} seconds.\n")
        next_action = input("Hit \"p\" to play the game, or \"s\" to keep fiddling around with settings.\n")
        game_duration = desired_duration
        if next_action == "s":
            set_settings()
        elif next_action == "p":
            run_test()
    
    
    #function that asks the user which settings they want to change
    def desired_settings():
        desired_settings_change = input("\n\n===\n\nWhich settings do you want to change?\n\n\"d\" — duration of the game\n\"p\" — stop messing around with settings and play the game\n\n")
        if desired_settings_change == "d":
            set_duration()
        elif desired_settings_change == "p":
            run_test()

    desired_settings()

    # add some settings
    #   [ ] which operations you want to include
    #   [ ] range of numbers
    #   [x] time duration



def run_test():
    print(f"\n\n=== {game_duration} second game ===\n\n")
    start_time = time.time()
    correct = 0
    attempts = 0
    while True:
        elapsed = time.time() - start_time
        if elapsed >= game_duration:
            break
        expression, answer = generate_problem()
        try:
            while True:
                user_answer = input(f"{expression} = ")
                if user_answer.strip().isdigit() or (user_answer.strip().startswith('-') and user_answer.strip()[1:].isdigit()):
                    user_answer = int(user_answer.strip())
                    if user_answer == answer:
                        correct += 1
                        print("correct!\n")
                        break
                    elif elapsed >= game_duration:
                        break
                attempts += 1
        except KeyboardInterrupt:
            break
    ending_message(correct, attempts)

def start():
    print("\n\n===\n\nWelcome to the Zetaterm: Zetamac in the terminal.")
    print(f"\nThe Arithmetic Game is a fast-paced speed drill where you're given {game_duration} seconds to solve as many arithmetic problems as you can.")
    next_step = input("\n\nPress \"p\" to play, or \"s\" to adjust the settings.\n")
    if next_step.strip() == "p":
        run_test()
    elif next_step.strip() == "s":
        set_settings()
    else:
        print("Oops, that wasn't a readable command. Try again.")
        start()


def ending_message(correct, attempts):
    print("Time's up!")
    print(f"You answered {correct} correctly out of {attempts} attempted.\n\{correct} POINTS!")
    next_action = input("\nPress \"p\" to play again, or \"s\" to edit the settings.\n")
    if next_action == 'p':
        run_test()
    elif next_action == 's':
        set_settings()


if __name__ == "__main__":
    start()