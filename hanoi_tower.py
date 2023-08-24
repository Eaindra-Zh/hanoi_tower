# Defining a function for solving the hanoi problem
def hanoi_instructions(n_disks: int, source: str, spare: str, goal: str):
    """
    Given a number of disks, find the solution for the hanoi tower problem

    Args: 
        n_disks (int): the number of disks
        source (str): the initial rod
        spare (str): the spare rod
        goal (str): the final rod
    Return: 
        A list of sets for the instruction to move a number of disks
    """
    if n_disks == 1: 
        return [(source,goal)] 
    
    instructions = []
    instructions.extend(hanoi_instructions(n_disks - 1, source, goal, spare))
    instructions.append((source, goal))
    instructions.extend(hanoi_instructions(n_disks - 1, spare, source, goal))
    
    return instructions

# Defining a function for saving the instructions into a file. 
def saveHanoi(n_disks: int, filename: str):
    """
    Saves the instructions to solve the problem of Hanoi Tower into a .txt file

    Args: 
        filename (str) : the name of the file
        n_disks (int) : the number of the disks

    Returns: 
        None
    """
 
    instructions = hanoi_instructions(n_disks, 'A', 'B', 'C')

    with open(f"{filename}.txt", "w") as file:
        file.write("#" * 50 + "\n")
        file.write("# Tower of Hanoi Instructions\n")
        file.write("#" * 50 + "\n")
        file.write(f"# Number of disks = {n_disks}\n")
        file.write("# Source pile = A\n")
        file.write("# Spare pile = B\n")
        file.write("# Goal pile = C\n")
        file.write("#" * 50 + "\n")

        for move_num, (source, target) in enumerate(instructions, start=1):
            file.write(f"Move disk from pile {source} to pile {target} (Move {move_num})\n")

        print(f"Instructions saved to {filename}.txt")
    return  

def solve_hanoi(n_disks: int, save_filename: str):
    """
    Given a number of disks, solve the tower of hanoi and saves the instructions to solving it in a .txt file.

    Args:
        n_disk (int): The number of disks
        save_filename (str): Name of the file with instructions

    Returns:
        None
    """
    hanoi_instructions(n_disks, 'A', 'B', 'C')
    saveHanoi(n_disks, save_filename)
    return

user_n_disks = input("Hello there. To get a solution for your hanoi tower problem, please type in the number of disks you have: ")
if  user_n_disks.isdigit() == False: 
    user_n_disks = input("You have to put in an integer number: ")
user_filename = input("How would you like to save your file? ")

solve_hanoi(int(user_n_disks), str(user_filename))