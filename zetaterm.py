import random
import time

game_duration = 120

normal_game_mode = "Normal Game Mode"
decimal_game_mode = "Decimal Game Mode"
hard_game_mode = "Hard Game Mode"
cheat_mode = False
current_game_mode = normal_game_mode

normal_bounds = [2,12,100]
decimal_bounds = [0.01,1.00,2.00]
hard_bounds = [2,100,1000]
current_bounds = normal_bounds.copy()


while True:
    if current_game_mode == normal_game_mode:
        current_bounds = normal_bounds.copy()
        break
    elif current_game_mode == decimal_game_mode:
        current_bounds = normal_bounds.copy()
        break
    elif current_game_mode == hard_game_mode:
        break

# generates a problem, given certain bounds
def generate_problem(bounds):
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    # generates expressions for each of /,*,+,-. first checks if you're on decimal game mode (if so, generates random floats, rather than random integers).
    if current_game_mode != decimal_game_mode:
        if operation == '/':
            c = random.randint(bounds[0], bounds[1])
            b = random.randint(bounds[0], bounds[2])
            a = b*c
            expression = f"{a} / {b}"
            answer = eval(expression)
            return expression, answer
        elif operation == "*":
            a = random.randint(bounds[0], bounds[1])
            b = random.randint(bounds[0], bounds[2])
            expression = f"{a} {operation} {b}"
            answer = eval(expression)
            return expression, answer
        elif operation == "+" or operation == "-":
            a = random.randint(bounds[0], bounds[2])
            b = random.randint(bounds[0], bounds[2])
            expression = f"{a} {operation} {b}"
            answer = eval(expression)
            return expression, answer
    else:
        if operation == '/':
            c = round(random.uniform(bounds[0], bounds[1]),1)
            b = round(random.uniform(bounds[0], bounds[2]),2)
            a = b*c
            expression = f"{a} / {b}"
            answer = eval(expression)
            return expression, answer
        elif operation == "*":
            a = round(random.uniform(bounds[0], bounds[1]),1)
            b = round(random.uniform(bounds[0], bounds[2]),2)
            expression = f"{a} {operation} {b}"
            answer = eval(expression)
            return expression, answer
        elif operation == "+" or operation == "-":
            a = round(random.uniform(bounds[0], bounds[2]),2)
            b = round(random.uniform(bounds[0], bounds[2]),2)
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
    
    #function that lets the user set the "mode" of play (e.g. decimal-mode, normal-mode, hard-mode)
    def set_mode():
        global current_bounds, current_game_mode, cheat_mode
        desired_mode = input("\n\nWhat mode do you want to enter?\n\n\"nm\" — normal-mode (default settings)\n\"dm\" — decimal-mode (to drill arithmetic with decimals)\n\"hm\" — hard mode (3 digit numbers)\n\n").strip()
        if desired_mode == "nm":
            current_game_mode = normal_game_mode
            current_bounds = normal_bounds
        elif desired_mode == "dm":
            current_game_mode = decimal_game_mode
            current_bounds = decimal_bounds
        elif desired_mode == "hm":
            current_game_mode = hard_game_mode
            current_bounds = hard_bounds
        elif desired_mode == "cmT":
            cheat_mode = True
        elif desired_mode == "cmF":
            cheat_mode = False
        else:
            print("Oops, that wasn't a readable command. Try again.")
            set_mode()
        ready_to_play_q("Hit \"p\" to play, or \"s\" to fiddle around with the settings.")
        
    
    #function that asks the user which settings they want to change
    def desired_settings():
        desired_settings_change = input(f"\n\n===\n\nWhich settings do you want to change?\n\n\"d\" — duration of the game (currently {game_duration} seconds)\n\"m\" — change the game mode (normal, decimal, hard)\n\"p\" — stop messing around with settings and play the game ({game_duration} seconds)\n\n")
        if desired_settings_change == "d":
            set_duration()
        elif desired_settings_change == "m":
            set_mode()
        elif desired_settings_change == "p":
            run_test()
        else:
            print("Oops, that wasn't a readable command. Try again.")
            desired_settings()
            

    desired_settings()

    # add some settings
    #   [ ] which operations you want to include
    #   [ ] range of numbers
    #   [x] time duration
    #   [ ] decimal mode

#function that asks the user if they're ready to play
def ready_to_play_q(message):
    print(f"\nCurrent settings:\n- Game duration: {game_duration} seconds\n- Game mode: {current_game_mode}")
    next_action = input(f"\n{message}\n\n")
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
        expression, answer = generate_problem(current_bounds)
        try:
            while True:
                if cheat_mode:
                    print(answer)
                user_answer = input(f"{expression} = ")
                if elapsed >= game_duration:
                    break
                try:
                    if current_bounds == decimal_bounds:
                        user_answer = float(user_answer.strip())
                        if user_answer == answer:
                            correct += 1
                            print("correct!\n")
                            break
                    else:
                        user_answer = int(user_answer.strip())
                        if user_answer == answer:
                            correct += 1
                            print("correct!\n")
                            break
                except ValueError:
                    pass
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