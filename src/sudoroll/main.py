import argparse
import random
import sys

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources
    
def get_random_curse():
    """Reads the curses.txt file and returns a random line."""
    try:
        curses_file = (
            importlib_resources.files("sudoroll")
            .joinpath("curses.txt")
        )
        
        content = curses_file.read_text()
        
        curses = content.strip().splitlines()
        if not curses:
            return "Curse file was empty!"
        return random.choice(curses)
        
    except Exception as e:
        return f"Error finding curses: {e}"
      

def main():
    parser = argparse.ArgumentParser(
        description="A simple, slightly mean command-line dice roller."
    )
    
    parser.add_argument(
        "--sides",
        type=int,
        default=6,
        help="The number of sides on the die (default: 6)"
    )
    
    args = parser.parse_args()
    
    if args.sides <= 0:
        print("Error: --sides must be a positive number.")
        return

    roll = random.randint(1, args.sides)
    threshold = args.sides / 2
    
    print(f"Rolling a d{args.sides}...")
    
    if roll <= threshold:
        # Bad roll! Get a curse.
        curse = get_random_curse()
        print(f"You rolled a {roll}. Ouch.")
        print(f"{curse}")
    else:
        # Good roll!
        print(f"You rolled a {roll}. Phew, you're safe.")

if __name__ == "__main__":
    main()