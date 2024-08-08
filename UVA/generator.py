import sys
import os

def check_if_files_exist(input_file: str, output_file: str) -> None:
    if os.path.isfile(input_file):
        print(f"Input file {input_file} exists.")
        return
    if os.path.isfile(output_file):
        print(f"Output file {output_file} exists.")
        return

def get_and_write_inputs(input_file: str, output_file: str) -> None:
    # [TODO] Make the inputs multi-line (allow new character)
    try:
        inp = input("Insert input testcases: ")
        with open(input_file, 'w') as file:
            file.write(inp)

        out = input("Insert output testcases: ")
        with open(output_file, 'w') as file:
            file.write(out)

    except Exception as e:
        print(f"An error occurred: {e}")
        return

def ask_and_generate_code_template() -> None:
    input_type = input("Specify input type: ")
    match input_type.lower():
        case "default" | "def" | "d":
            print("Default it is")
        case "ints" | "int" | "i":
            print("ints")
        case "strings" | "strs" | "str" | "s":
            print("strings")
        case _:
            print("Invalid type")

    input_lines_specified = input("Does line 1 specify number of test cases?: ")
    match input_lines_specified.lower():
        case "yes" | "ye" | "y" | "true" | "t":
            print("Okay")
        case "no" | "n" | "false" | "f":
            print("Not Okay")

def generator(problem_number: str) -> None:
    input_file: str = f"UVA-{problem_number}-input.txt"
    output_file: str = f"UVA-{problem_number}-output.txt"
    check_if_files_exist(input_file, output_file)
    get_and_write_inputs(input_file, output_file)
    ask_and_generate_code_template()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generator.py <problem_number>")
        sys.exit(1)

    problem_number: str = sys.argv[1]
    generator(problem_number)
