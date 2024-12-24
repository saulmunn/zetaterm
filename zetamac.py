import random
import time

game_duration = 120


def generate_problem():
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    if operation == '/':
        b = random.randint(2, 12)
        c = random.randint(2, 100)
        a = b*c
        expression = f"{a} / {b}"
        answer = eval(expression)
        return expression, answer
    elif operation == "+" or operation == "-":
        a = random.randint(2, 100)
        b = random.randint(2, 100)
        expression = f"{a} {operation} {b}"
        answer = eval(expression)
        return expression, answer
    elif operation == "*":
        a = random.randint(2, 12)
        b = random.randint(2, 100)
        expression = f"{a} {operation} {b}"
        answer = eval(expression)
        return expression, answer



def set_settings(): # the "settings" menubar
        
    #function that lets the user set the duration of each game
    def set_duration():
        global game_duration
        desired_duration = int(input("\nHow long do you want the game to last? Type your answer in seconds, then hit Enter: ").strip())
        game_duration = desired_duration
        print(f"Games will now last {desired_duration} seconds.\n")
        ready_to_play_q("Hit \"p\" to play, or \"s\" to fiddle around with the settings.")
    

    
    #function that asks the user which settings they want to change
    def desired_settings():
        desired_settings_change = input(f"\n\n===\n\nWhich settings do you want to change?\n\n\"d\" — duration of the game (currently {game_duration} seconds)\n\"p\" — stop messing around with settings and play the game ({game_duration} seconds)\n\n")
        if desired_settings_change == "d":
            set_duration()
        elif desired_settings_change == "p":
            run_test()

    desired_settings()

    # add some settings
    #   [ ] which operations you want to include
    #   [ ] range of numbers
    #   [x] time duration

#function that asks the user if they're ready to play
def ready_to_play_q(message):
    print(f"Current settings:\n- Game duration: {game_duration} seconds\n- [no other editable settings at this time]")
    next_action = input(f"\n{message}\n")
    if next_action == "s":
        set_settings()
    elif next_action == "p":
        run_test()
    else:
        print("Oops, that wasn't a readable command. Try again.")
        ready_to_play_q(message)
        

def run_test():
    print(f"\n\n=== {game_duration} second game ===\n\n")
    start_time = time.time()
    correct = 0
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
        except KeyboardInterrupt:
            break
    ending_message(correct)

def start():
    print("\n\n===\n\nWelcome to the Zetaterm: Zetamac in the terminal.")
    print(f"\nThe Arithmetic Game is a fast-paced speed drill where you're given {game_duration} seconds to solve as many arithmetic problems as you can.\n")
    ready_to_play_q("Press \"p\" to play, or \"s\" to adjust the settings.\n")


def ending_message(correct):
    print("Time's up!")
    print(f"\n\\ {correct} POINTS! \n")
    ready_to_play_q("Press \"p\" to play again, or \"s\" to edit the settings.\n")
    # next_action = input("\nPress \"p\" to play again, or \"s\" to edit the settings.\n")
    # if next_action == 'p':
    #     run_test()
    # elif next_action == 's':
    #     set_settings()


if __name__ == "__main__":
    start()