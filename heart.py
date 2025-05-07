import time

def print_heart():
    heart = [
        "   ❤️❤️❤️   ❤️❤️❤️   ",
        " ❤️❤️❤️❤️❤️❤️❤️❤️❤️ ",
        "❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️",
        " ❤️❤️❤️❤️❤️❤️❤️❤️❤️ ",
        "   ❤️❤️❤️❤️❤️❤️❤️   ",
        "     ❤️❤️❤️❤️❤️     ",
        "       ❤️❤️❤️       ",
        "         ❤️         "
    ]
    for line in heart:
        print(line)

def pulse_heart():
    for _ in range(3):
        print_heart()
        time.sleep(0.5)
        print("\033[H\033[J", end="")  # Clear screen
        time.sleep(0.1)
        print_heart()
        time.sleep(0.5)
        print("\033[H\033[J", end="")  # Clear screen
        time.sleep(0.1)

# Run pulsing heart
pulse_heart()

# Final heart and message
print_heart()
print("    I ❤️ Python!    ")