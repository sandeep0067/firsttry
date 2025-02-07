def program_in_set(program_name, program_set):
    return program_name in program_set

def main():
    # Define a set of known programs
    known_programs = {
        "Python",
        "Java",
        "C++",
        "JavaScript",
        "Ruby",
        "Go",
        "Swift"
    }

    # Get user input
    user_input = input("Enter the name of the program you want to check: ")

    # Check if the program is in the set
    if program_in_set(user_input, known_programs):
        print(f"{user_input} is in the set of known programs.")
    else:
        print(f"{user_input} is NOT in the set of known programs.")

if __name__ == "__main__":
    main()
    # hello 